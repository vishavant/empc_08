from django.db import models

# Create your models here.

STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattisgarh','Chhattisgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pradesh','Himachal Pradesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Kerala','Kerala'),
  ('Lakshadweep','Lakshadweep'),
  ('Madhya Pradesh','Madhya Pradesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalaya','Meghalaya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Punjab','Punjab'),
  ('Rajasthan','Rajasthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('West Bengal','West Bengal'),
)



QUERY_TYPE = [
    ('OFFLINE SPOKEN ENLISH CLASSES', 'Offline Spoken English Classes'),
    ('ONLINE SPOKEN ENGLISH CLASSES', 'Online Spoken Enlgish Classes'),
    ('ONLINE GROUP DISCUSSION CLASSES', 'Online Group Discussion Classes'),
    ('IELTS', 'IELTS'),
    ('OTHER', 'Other'),
]


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    query_type = models.CharField(max_length=100, choices=QUERY_TYPE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


APPLIED_FOR = (
    ('ONLINE SPOKEN ENGLISH TRAINER', 'Online Spoken English Trainer'),
    ('OFFLINE SPOKEN ENGLISH TRAINER', 'Offline Spoken English Trainer'),
    ('IELTS TRAINER', 'IELTS Trainer'),
)



class JoinUs(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    qualification = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    applied_for = models.CharField(max_length=100, choices=APPLIED_FOR)
    resume_file = models.FileField(upload_to="trainer_cv")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

