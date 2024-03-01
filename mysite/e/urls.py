from django.urls import path
from e.views import *
urlpatterns = [
    path('',view,name='view'),
    path('delete/<int:pk>',delete,name='delete')

]