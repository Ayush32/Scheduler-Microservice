from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .scheduler import schedule_job
from .serializers import JobSerializer

class JobListAPIView(APIView):
    """
        Retrieve all Job objects from the database and serialize them using JobSerializer.
        
        Args:
        request: HTTP request
        
        Returns:
        Response containing serialized data of all Job objects
    """
    def get(self,request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs,many = True)
        return Response(serializer.data)
    
class JobDetailAPIView(APIView):
    """
    Retrieve a job by its ID.

    Args:
        request (Request): The HTTP request object.
        job_id (int): The ID of the job to retrieve.

    Returns:
        Response: A Response object containing the serialized job data if found,
                  or an error message with a 404 status if the job does not exist.
    """
    def get(self,request,job_id):
        try:
            job = Job.objects.get(id = job_id)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response({"error" : "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        
class JobCreateAPIView(APIView):
    """
        Handle POST request to create a new job.

        This method deserializes the incoming request data using JobSerializer.
        If the data is valid, it saves the job, schedules it, and returns a 
        response with the serialized job data and a 201 Created status.
        If the data is invalid, it returns a response with the errors and a 
        400 Bad Request status.
    """
    def post(self,request):
        serializer = JobSerializer(data = request.data)
        if serializer.is_valid():
            job = serializer.save()
            schedule_job(job.id,job.job_name,job.schedule)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)