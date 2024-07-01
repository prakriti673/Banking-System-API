from django.contrib import admin
from django.urls import path, include

from .views import BankAPIView, BranchAPIView, BranchDetailAPIView, BankDetailAPIView

urlpatterns = [
    path('banks/', BankAPIView.as_view(), name='banks'),
    path('bank/<int:pk>/', BankDetailAPIView.as_view(), name='bank-detail'),
    path('branches/', BranchAPIView.as_view(), name='branches'),
    path('branch/<int:pk>/', BranchDetailAPIView.as_view(), name='branch-detail'),
]
