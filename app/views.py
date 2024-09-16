# projects/views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import SchoolManagements
from .serializers import SchoolManagementsSerializer

# View for handling both GET (retrieve list) and POST (create new)
class ProjectListCreateAPIView(APIView):
    
    # GET method to retrieve all projects
    def get(self, request):
        projects = SchoolManagements.objects.all()  # Fetch all projects
        serializer = SchoolManagementsSerializer(projects, many=True)
        return Response(serializer.data)  # Return serialized data
    
    # POST method to create a new project
    def post(self, request):
        serializer = SchoolManagementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save project if data is valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View for handling GET, PUT, DELETE for a single project
class ProjectDetailAPIView(APIView):

    # Helper method to get a project object or return 404
    def get_object(self, pk):
        try:
            return SchoolManagements.objects.get(pk=pk)
        except SchoolManagements.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    # GET method to retrieve a single project by its ID
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = SchoolManagementsSerializer(project)
        return Response(serializer.data)
    
    # PUT method to update an existing project
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = SchoolManagementsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update project if data is valid
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE method to delete a project
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
