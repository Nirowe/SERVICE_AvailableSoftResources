from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee, Soft, Resource, Documents
from .serializers import EmployeesSoftResourceListSerializer
from .serializers import SoftEmployeeDocumentListSerializer
from .serializers import EResourceSoftAndEmployeeListSerializer
from .serializers import SoftListSerializer
from .serializers import EmployeeListSerializer
from .serializers import ResourceListSerializer


class EmployeeSoftResourceListView(APIView):
    """ Вывод доступного сотруднику софта и электронных ресурсов"""

    def get(self, request):
        try:
            employee = Employee.objects.get(id=request.GET.get('id'))
            serializer = EmployeesSoftResourceListSerializer(employee)
        except:
            employee = Employee.objects.all()
            serializer = EmployeeListSerializer(employee, many=True)

        return Response(serializer.data)


class SoftEmployeeDocumentationListView(APIView):
    """
    Вывод сотрудников, имеющих доступ к софту и документов,
    для работы с которыми нужен этот софт
    """

    def get(self, requests):
        try:
            soft = Soft.objects.get(id=requests.GET.get('id'))
            serializer = SoftEmployeeDocumentListSerializer(soft)
        except:
            soft = Soft.objects.all()
            serializer = SoftListSerializer(soft, many=True)

        return Response(serializer.data)


class ResourceSoftAndEmployeeListView(APIView):
    """
    Вывод списка софта и сотрудиков, которые имеют доступ к элетронному ресурсу
    """

    def get(self, requests):
        try:
            resource = Resource.objects.get(id=requests.GET.get('id'))
            serializer = EResourceSoftAndEmployeeListSerializer(resource)
        except:
            resource = Resource.objects.all()
            serializer = ResourceListSerializer(resource, many=True)

        return Response(serializer.data)


class GetTableView(APIView):
    """
    Скачать сводную таблицу
    """

    def get(self, requests):
        with open(settings.MEDIA_ROOT + 'test2.csv', 'w') as file:
            employee_title = []
            for e in Employee.objects.all():
                test = '{} {} ({})'
                employee_title.append(test.format(e.first_name, e.last_name, e.position))
            file.write(',')
            file.write(','.join(employee_title))
            file.write('\n')

            line = []
            for r in Resource.objects.all():
                line.append(r.name)
                soft_list = []
                for s in r.soft.all():
                    soft_list.append(s.soft_name)

                for e in Employee.objects.all():
                    e_soft_list = []
                    for s in e.employee_soft.all():
                        e_soft_list.append(s.soft_name)
                    result_item_soft = list(set(soft_list) & set(e_soft_list))
                    line.append(';'.join(result_item_soft))

                file.write(','.join(line))
                file.write('\n')
                line = []
        return Response('http://127.0.0.1:8000/media/table.csv')
