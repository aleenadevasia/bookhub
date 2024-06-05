# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user-delete'),
    path('login/', views.CustomLoginAPIView.as_view(), name='login'),
]
