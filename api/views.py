from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, JobPost, Applicant
import json

@csrf_exempt
def create_company(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(
            name=data['name'],
            location=data['location'],
            description=data['description']
        )
        return JsonResponse({'message': 'Company created', 'company_id': company.id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def post_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.get(id=data['company_id'])
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found'}, status=404)
        job = JobPost.objects.create(
            company=company,
            title=data['title'],
            description=data['description'],
            salary=data['salary'],
            location=data['location']
        )
        return JsonResponse({'message': 'Job posted', 'job_id': job.id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

def get_jobs(request):
    jobs = JobPost.objects.all()
    job_list = []
    for job in jobs:
        job_list.append({
            'id': job.id,
            'title': job.title,
            'company': job.company.name,
            'salary': job.salary,
            'location': job.location
        })
    return JsonResponse({'jobs': job_list})

@csrf_exempt
def apply_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            job = JobPost.objects.get(id=data['job_id'])
        except JobPost.DoesNotExist:
            return JsonResponse({'error': 'Job not found'}, status=404)
        applicant = Applicant.objects.create(
            name=data['name'],
            email=data['email'],
            resume_link=data['resume_link'],
            job=job
        )
        return JsonResponse({'message': 'Application submitted', 'applicant_id': applicant.id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

def get_applicants(request, job_id):
    try:
        job = JobPost.objects.get(id=job_id)
    except JobPost.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)
    applicants = Applicant.objects.filter(job=job)
    applicant_list = [{
        'name': a.name,
        'email': a.email,
        'resume': a.resume_link
    } for a in applicants]
    return JsonResponse({'applicants': applicant_list})
