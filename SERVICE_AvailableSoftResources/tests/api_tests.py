import pytest
import requests
import codecs

ADDR = 'http://127.0.0.1:8000'
ETALONS = 'etalons/'


# @vcr.use_cassette('cassettes/test_employee_soft_resource_list_cassettes.yaml')
@pytest.mark.vcr()
def test_employee_soft_resource_list():
    """
        Testing EmployeeSoftResourceListView with param "id" in request
    """
    url = '{}/api/employee_soft_resource_list/?id={}'
    id = 1
    request = requests.get(url.format(ADDR, id))
    data = request.text
    with codecs.open(
        ETALONS + 'employee_soft_resource_list_etalon',
        'r',
        encoding='utf-8'
    ) as etalon_file:
        etalon_data = etalon_file.read()
    assert etalon_data == data


@pytest.mark.vcr()
def test_soft_employee_documents_list():
    """
        Testing SoftEmployeeDocumentsListView with param "id" in request
    """
    url = '{}/api/soft_employee_documents_list/?id={}'
    id = 1
    request = requests.get(url.format(ADDR, id))
    data = request.text
    with codecs.open(
        ETALONS + 'soft_employee_documents_list_etalon',
        'r',
        encoding='utf-8'
    ) as etalon_file:
        etalon_data = etalon_file.read()
    assert etalon_data == data


@pytest.mark.vcr()
def test_resource_soft_employee_list():
    """
        Testing ResourceSoftEmployeeListView with param "id" in request
    """
    url = '{}/api/resource_soft_employee_list/?id={}'
    id = 1
    request = requests.get(url.format(ADDR, id))
    data = request.text
    print(data)
    with codecs.open(
        ETALONS + 'resource_soft_employee_list_etalon',
        'r',
        encoding='utf-8'
    ) as etalon_file:
        etalon_data = etalon_file.read()
    assert etalon_data == data


# using parametrize

test_case = [
    (
        'http://127.0.0.1:8000/api/employee_soft_resource_list/',
        '1',
        'etalons/employee_soft_resource_list_etalon'
    ),
    (
        'http://127.0.0.1:8000/api/soft_employee_documents_list/',
        '1',
        'etalons/soft_employee_documents_list_etalon'
    ),
    (
        'http://127.0.0.1:8000/api/resource_soft_employee_list/',
        '1',
        'etalons/resource_soft_employee_list_etalon'
    ),
]


@pytest.mark.parametrize(
    'url, id, etalon', test_case
)
def test_all_list(url, id, etalon):
    """
        Testing EmployeeSoftResourceListView with param "id" in request
        Testing SoftEmployeeDocumentsListView with param "id" in request
        Testing ResourceSoftEmployeeListView with param "id" in request
    """
    request = requests.get(url, params={'id': id})
    data = request.text
    print(data)
    with codecs.open(
        etalon,
        'r',
        encoding='utf-8'
    ) as etalon_file:
        etalon_data = etalon_file.read()
    assert etalon_data == data


test_case = [
    (
        'http://127.0.0.1:8000/api/employee_soft_resource_list/',
        'etalons/employee_list_etalon'
    ),
    (
        'http://127.0.0.1:8000/api/soft_employee_documents_list/',
        'etalons/soft_list_etalon'
    ),
    (
        'http://127.0.0.1:8000/api/resource_soft_employee_list/',
        'etalons/resource_list_etalon'
    ),
]


@pytest.mark.parametrize(
    'url, etalon', test_case
)
def test_request_without(url, etalon):
    """
        Testing EmployeeSoftResourceListView without param "id" in request
        Testing SoftEmployeeDocumentsListView without param "id" in request
        Testing ResourceSoftEmployeeListView without param "id" in request
    """
    request = requests.get(url)
    data = request.text
    with codecs.open(
        etalon,
        'r',
        encoding='utf-8'
    ) as etalon_file:
        etalon_data = etalon_file.read()
    assert etalon_data == data
