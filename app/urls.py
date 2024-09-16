# projects/urls.py

# projects/urls.py
from django.urls import path
from .views import ProjectListCreateAPIView, ProjectDetailAPIView

urlpatterns = [
    # URL for list and create (GET and POST)
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    
    # URL for detail view (GET, PUT, DELETE) by ID
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
]


