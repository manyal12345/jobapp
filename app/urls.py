from django.urls import path

# from app.views import hello, job_details
from app import views 

urlpatterns = [
    path('',views.job_list, name='jobs_home'),
    path('hello/',views.hello, name='hello'),
    path('job/<int:id>',views.job_details, name='jobs_details'),
    # path('job/<str:id>',views.job_details),

]  