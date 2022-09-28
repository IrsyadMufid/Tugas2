from django.urls import path
from todolist.views import show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import create_task #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import task_toggle #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import task_delete #sesuaikan dengan nama fungsi yang dibuat


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', create_task, name='create_task'),
    path('toggle-task/<int:pk>', task_toggle, name='toggle_task'),
    path('delete-task/<int:pk>', task_delete, name='delete_task'),
]