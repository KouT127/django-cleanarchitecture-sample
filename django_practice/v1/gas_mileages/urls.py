from django.conf.urls import url
from django.urls import path
from django_practice.v1.gas_mileages import views

app_name = 'gas_mileages'
urlpatterns = [
    path('mileage/', views.V1GasMileageView.as_view(), name='gas_mileage'),
    path('mileage/<int:pk>/', views.V1GasMileageDetailView.as_view()),
    path('user', views.V1UserView.as_view(), name='user'),
]
