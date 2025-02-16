from django.contrib import admin
from django.urls import path
from tasks.views import trigger_task

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add/', trigger_task, name='trigger_task'),

]
