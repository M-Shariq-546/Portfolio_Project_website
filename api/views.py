from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProjectSerializers
from user_projects.models import Project, Review, Tag

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getProjects(request):
 #   print("USER", request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializers(projects, many=True) #many=True is in case we want all data to serialize otherwise it will be False
    return Response(serializer.data)



@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializers(project, many=False) 
    return Response(serializer.data)



@api_view(['GET'])
def getRoutes(request):
    
    route = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
        
    ]
    
    return Response(route)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getProjectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review , created = Review.objects.get_or_create(
        owner=user,
        project= project,
    )
    
    review.value= data['value']
    review.save()
    project.getVoteCount
    
    print("Data", data)
    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tags']
    projectId = request.data['projects']
    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)
    project.tag.remove(tag)
    return Response("The Tag was Deleted")