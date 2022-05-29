from django.db import models

# Create your models here.

# List Of all type of Courses class
class courses(models.Model) :
    course_name = models.CharField(max_length=50)
    course_intro = models.CharField(max_length=500)
    course_intro_link = models.CharField(max_length=50)
    full_course_link = models.CharField(max_length=50)

# cloud computing
class cloud_computing(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# software testing
class software_testing(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# Machine learning
class machine_learning(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# Android App learning
class android_App(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# Ios App learning
class ios_App(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# front_end learning
class front_end(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# back_end learning
class back_end(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)

# full stack development learning
class full_stack(models.Model) :
    language = models.CharField(max_length=50)
    language_info = models.CharField(max_length=500)
    reference_link = models.CharField(max_length=200)