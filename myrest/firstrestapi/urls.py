from django.urls import  path
from . import  views
emp=views.EmployeeList()

urlpatterns = [
    path("",views.EmployeeList().as_view(),name=""),
    #path("",views.index,name=""),
    path('<int:pk>/', views.EmployeeDetail.as_view(),name="update"),

]