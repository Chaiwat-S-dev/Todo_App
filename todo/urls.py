from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<task_id>', views.completeTodo, name='complete'),
    path('deleteComplete', views.deleteComplete, name='deleteComplete'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
]
