from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('jobseeker','JobSeeker')
    ]
    display_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER,max_length=120)
    profile_picture=models.ImageField(upload_to='media/profile_pic',null=True)
    def __str__(self):
        return self.display_name
    
class job_model(models.Model):

    job_title=models.CharField(max_length=100,null=True)
    company_name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    company_description=models.TextField(null=True)
    job_description=models.TextField(null=True)
    qualifications=models.TextField(null=True)
    deadline=models.CharField(max_length=100,null=True)
    create_at = models.DateTimeField(auto_now_add=True,null=True)
    update_at = models.DateTimeField(auto_now=True,null=True)
    profile_picture=models.ImageField(upload_to='media/profile_pic',null=True)
    job_creator = models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.job_title

class RecruiterProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='recruiterprofile')
    
    def __str__(self):
        return self.user.display_name
    

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='jobseekerprofile')
   
    skills=models.CharField(max_length=100,null=True)

    


