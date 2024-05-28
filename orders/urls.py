from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    # path('update_status/<int:order_id>', views.update_order_status, name='update_order_status')
    path('update_status', views.update_order_status, name='update_order_status')
]
