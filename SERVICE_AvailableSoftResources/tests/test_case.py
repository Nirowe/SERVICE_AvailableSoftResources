import codecs
import requests


class TestBaseAPIFunctions:
    """
        Testing base API functions
    """

    def test_employee_soft_resource_list(self):
        """
            Testing EmployeeSoftResourceListView with param "id" in request
        """

        url = 'http://127.0.0.1:8000/api/employee_soft_resource_list/'
        etalon = 'etalons/employee_soft_resource_list_etalon'
        id = 1
        request = requests.get(url, params={'id': id})
        data = request.text
        with codecs.open(etalon,
                         'r',
                         encoding='utf-8') as etalon_file:
            etalon_data = etalon_file.read()
        assert etalon_data == data

    def test_employee_list(self):
        """
            Testing EmployeeSoftResourceListView without param "id" in request
        """

        url = 'http://127.0.0.1:8000/api/employee_soft_resource_list/'
        etalon = 'etalons/employee_list_etalon'
        id = 1
        request = requests.get(url)
        data = request.text
        with codecs.open(etalon,
                         'r',
                         encoding='utf-8') as etalon_file:
            etalon_data = etalon_file.read()
        assert etalon_data == data


    def test_soft_employee_documents_list(self):
        """
            Testing SoftEmployeeDocumentsListView with param "id" in request
        """

        url = 'http://127.0.0.1:8000/api/soft_employee_documents_list/'
        etalon = 'etalons/soft_employee_documents_list_etalon'
        id = 1
        request = requests.get(url, params={'id': id})
        data = request.text
        with codecs.open(etalon,
                         'r',
                         encoding='utf-8') as etalon_file:
            etalon_data = etalon_file.read()
        assert etalon_data == data

    def test_soft_list(self):
        """
            Testing SoftEmployeeDocumentsListView without param "id" in request
        """

        url = 'http://127.0.0.1:8000/api/soft_employee_documents_list/'
        etalon = 'etalons/soft_list_etalon'
        id = 1
        request = requests.get(url)
        data = request.text
        with codecs.open(etalon,
                         'r',
                         encoding='utf-8') as etalon_file:
            etalon_data = etalon_file.read()
        assert etalon_data == data

    def test_resource_soft_employee_list(self):
        """
            Testing ResourceSoftEmployeeListView with param "id" in request
        """
        url = 'http://127.0.0.1:8000/api/resource_soft_employee_list/'
        etalon = 'etalons/resource_soft_employee_list_etalon'
        id = 1
        request = requests.get(url, params={'id': id})
        data = request.text
        with codecs.open(etalon,
                         'r',
                         encoding='utf-8') as etalon_file:
            etalon_data = etalon_file.read()
        assert etalon_data == data

    def test_resource_list(self):
        """
            Testing ResourceSoftEmployeeListView without param "id" in request
        """
        url = 'http://127.0.0.1:8000/api/resource_soft_employee_list/'
        etalon = 'etalons/resource_list_etalon'

        request = requests.get(url)
        data = request.text
        with codecs.open(etalon,
                         'r',
                         encoding='utf-8') as etalon_file:
            etalon_data = etalon_file.read()
        assert etalon_data == data
