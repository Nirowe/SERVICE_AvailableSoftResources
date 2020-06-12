from rest_framework import serializers

from .models import Employee
from .models import Soft
from .models import Documents
from .models import Resource


class SoftListSerializer(serializers.ModelSerializer):
    """ Вывод списка софта"""

    class Meta:
        model = Soft
        fields = ('id', 'soft_name',)


class ResourceListSerializer(serializers.ModelSerializer):
    """ Вывод списка ресурсов """

    class Meta:
        model = Resource
        fields = ('id', 'name',)


class EmployeesSoftResourceListSerializer(serializers.ModelSerializer):
    """ Список доступного сотруднику софта и ресурсов"""
    employee_soft = SoftListSerializer(many=True)
    employee_resource = ResourceListSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class DocumentsListSerializer(serializers.ModelSerializer):
    """ Вывод списка документов"""

    class Meta:
        model = Documents
        fields = ('id', 'document',)


class EmployeeListSerializer(serializers.ModelSerializer):
    """ Вывод пользователей софта"""

    class Meta:
        model = Employee
        fields = '__all__'


class SoftEmployeeDocumentListSerializer(serializers.ModelSerializer):
    """
        Список сотрудников, которые имеют право работать с софтом,
        и документов, для работы с которыми нужен этот софт
    """
    employee = EmployeeListSerializer(read_only=True, many=True)
    documents = DocumentsListSerializer(read_only=True, many=True)

    class Meta:
        model = Soft
        fields = ('soft_name', 'employee', 'documents')


class EResourceSoftAndEmployeeListSerializer(serializers.ModelSerializer):
    """
        Список софта и сотрудников, имеющим доступ к электронному ресурсу
    """

    employee = EmployeeListSerializer(read_only=True, many=True)
    soft = SoftListSerializer(read_only=True,many=True)

    class Meta:
        model = Resource
        fields = ('id', 'name', 'employee', 'soft')

