from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect 
from django.urls import reverse
from django.template import loader

from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_discription = [
    "First Job Discription",
    "Second Job Discription",
    "Third Job Discription"
]

# Create your views here.

class TempClass:
    x = 5
    age = 19
def hello(request):
    list = ["Alpha", "Beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name" : "Django", "first_list" : list, "temp_object" : temp, "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)

def job_list(request):
    # jobs_data = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_details', args=(job_id,))
    #     jobs_data += f"<li><a href='{detail_url}'>{j}</a></li>"
    # jobs_data += "</ul>"
    # return HttpResponse(jobs_data)
    jobs = JobPost.objects.all()
    # context = {"job_title_list":job_title}
    context = {"jobs":jobs}
    return render(request, "app/index.html", context)

def job_details(request, id):
    # # return HttpResponse("Job Details")
    # site = "https://www.google.com"
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_discription[id]}</h3>"
        # return HttpResponse(return_html)
        # context ={"job_title": job_title[id], "job_discription":job_discription[id]}
        job = JobPost.objects.get(id=id)
        context = {"job":job}
        return render(request,"app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
    