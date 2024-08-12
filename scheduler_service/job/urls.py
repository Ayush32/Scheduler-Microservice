
from django.urls import path,include
from .views import JobListAPIView, JobDetailAPIView, JobCreateAPIView

urlpatterns = [
   path('jobs/',JobListAPIView.as_view(),name = 'list_jobs'),
   path('jobs/<int:job_id>/',JobDetailAPIView.as_view(),name = 'job_details'),
   path('jobs/new/',JobCreateAPIView.as_view(),name = 'create_job')
]
