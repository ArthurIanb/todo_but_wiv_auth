from django.urls import path
from .views import home_page, new_task, change_state, remove_task

urlpatterns = [
    path('', home_page, name='home'),
    path('new_task/', new_task, name='new_task'),
    path('change_state/<int:pk>/', change_state, name='change_state'),
    path('remove_task/<int:pk>/', remove_task, name='remove_task')
]
