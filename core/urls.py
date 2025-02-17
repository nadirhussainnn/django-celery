from django.contrib import admin
from django.urls import path
from tasks.views import purchase_phone_number

urlpatterns = [
    path("admin/", admin.site.urls),
    path('charge_phone_number_bill/', purchase_phone_number, name='purchase_phone_number'),

]
