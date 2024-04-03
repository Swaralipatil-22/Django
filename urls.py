from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListAPIView.as_view(), name='client-list'),
    path('clients/create/', views.create_client, name='create-client'),
    path('clients/<int:pk>/', views.ClientDetailAPIView.as_view(), name='client-detail'),
    path('clients/<int:pk>/update/', views.ClientUpdateAPIView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', views.ClientDestroyAPIView.as_view(), name='client-delete'),
    path('clients/<int:client_id>/projects/create/', views.create_project, name='create-project'),
    path('projects/', views.ProjectListAPIView.as_view(), name='project-list'),
]
