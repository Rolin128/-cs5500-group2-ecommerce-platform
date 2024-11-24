from django.urls import path

from . import views


urlpatterns = [

    path('checkout', views.checkout, name='checkout'),


    path('complete-order', views.complete_order, name='complete-order'),


    path('payment-success', views.payment_success, name='payment-success'),

    path('payment-failed', views.payment_failed, name='payment-failed'),

    path('mock-payment', views.mock_payment, name='mock-payment'),

    path('mock-payment-process', views.mock_payment_process, name='mock-payment-process'),

]
