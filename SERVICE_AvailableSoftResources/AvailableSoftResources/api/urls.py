from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'employee_soft_resource_list/',
        views.EmployeeSoftResourceListView.as_view()
    ),
    path(
        'soft_employee_documents_list/',
        views.SoftEmployeeDocumentationListView.as_view()
    ),
    path(
        'resource_soft_employee_list/',
        views.ResourceSoftAndEmployeeListView.as_view()
    ),
    path(
        'table_file/',
        views.GetTableView.as_view()
    )

]

