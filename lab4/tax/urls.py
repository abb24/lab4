from django.urls import path 
from . import views 
urlpatterns=[
    path ("", views.index,name='index'),
    path ('<int:num>', views.anyNumber, name='taxcalc'),
    path ('taxrate', views.taxrate,name= 'taxrate')
]