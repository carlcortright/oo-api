from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_classroom', views.create_classroom, name='create_classroom'),
    url(r'^list_questions', views.list_questions, name='list_questions'),
    url(r'^display_classroom', views.display_classroom, name='display_classroom'),
]