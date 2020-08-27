from django.urls import  path
from . import  views
emp=views.EmployeeList()

urlpatterns = [
    path("",emp.get,name=""),
    path('<int:pk>/', views.EmployeeDetail.as_view(),name="update"),

]