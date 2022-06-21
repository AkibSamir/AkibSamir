from enum import unique
from os import name
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200, blank=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedIn = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='hero', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "hero"

class About(models.Model):
    title1 = models.CharField(max_length=100, blank=True, null=True)
    title2 = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(auto_now_add=False)
    age = models.IntegerField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='profile', blank=True)
    degree = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    city = models.CharField(max_length=200, blank=True)
    freelance = models.CharField(max_length=100, blank=True)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name_plural = "about"


class Skills(models.Model):
    title = models.CharField(max_length=200, blank=True)
    percentage = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "skills"


class Education(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    period = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=200, blank=True)
    description = models.TextField( blank=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = "education"


class Certification(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    period = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=200, blank=True)
    description = models.TextField( blank=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = "certification"


class Contact(models.Model):
    location = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    call = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "contact"

class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "contactform"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "category"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "tag"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    created_on = models.DateField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='blog', null=True, blank=True)
    body = RichTextUploadingField()
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title + "|" + str(self.author)

    class Meta:
        verbose_name_plural = "blogpost"


# class Comment(models.Model):
#     post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     date = models.DateTimeField(auto_now_add=True)
#     body = models.TextField()

#     def __str__(self):
#         return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=200, blank=True)
    category = models.ManyToManyField(Category)
    client = models.CharField(max_length=200, blank=True)
    project_date = models.DateField(auto_now_add=False)
    project_url = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to="portfolio")
    image2 = models.ImageField(upload_to="portfolio", blank=True, null=True)
    image3 = models.ImageField(upload_to="portfolio", blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = "portfolio"