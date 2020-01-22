from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def studentList(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    print("in detail", request, pk)
    try:
        student = Students.objects.get(id=pk)
        print("student is:", student)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
