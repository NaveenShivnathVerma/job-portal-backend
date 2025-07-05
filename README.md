# 🧑‍💻 Job Portal API — Django (Without DRF)

This is a simple Job Portal backend built using Django (without Django REST Framework).  
It allows companies to post jobs and applicants to apply for them using basic function-based API endpoints.

---

## 🔧 Setup Instructions

1. Clone the repository  
```bash
git clone https://github.com/NaveenShivnathVerma/job-portal-backend.git

Create virtual environment and install Django
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
pip install django

Run migrations and start server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

 Create Company
POST /api/create-company/
```json
{
  "name": "Google",
  "location": "Bangalore",
  "description": "Tech company"
}

Post Job
POST /api/post-job/
```json
{
  "company_id": 1,
  "title": "Backend Developer",
  "description": "Experience with Django",
  "salary": 60000,
  "location": "Remote"
}

List All Jobs
GET /api/jobs/

 Apply to a Job
POST /api/apply/
{
  "name": "John Doe",
  "email": "john@example.com",
  "resume_link": "https://example.com/resume.pdf",
  "job_id": 1
}

List Applicants for a Job
GET /api/applicants/1/

⚙️ Tech & Constraints
✅ Django (core only, no DRF)
✅ Function-based views
✅ JsonResponse for API responses
✅ SQLite database used

Sample Data Used
Company
{
  "name": "Google",
  "location": "Bangalore",
  "description": "Tech company"
}

Job
{
  "company_id": 1,
  "title": "Backend Developer",
  "salary": 60000,
  "location": "Remote"
}

Applicant
{
  "name": "John Doe",
  "email": "john@example.com",
  "resume_link": "https://example.com/resume.pdf",
  "job_id": 1
}

🙋‍♂️ Author
Naveen Shivnath Verma
