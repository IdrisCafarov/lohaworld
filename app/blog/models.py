from django.db import models
from ckeditor.fields import RichTextField
from .helper import *
from django.urls import reverse



# Create your models here.

class GeneralSettings(models.Model):
    
    site_title = models.CharField(max_length=1500, verbose_name="Saytın başlığı")
    email = models.CharField(max_length=1500, verbose_name="Email", null=True,blank=True)
    number = models.CharField(max_length=1500, verbose_name="Nömrə", null=True,blank=True)
    adress = models.CharField(max_length=1500, verbose_name="Ünvan", null=True)
    working_hours = models.CharField(max_length=1000, null=True)

    facebook = models.CharField(max_length=1500, verbose_name="Facebook", blank=True)
    linkedin = models.CharField(max_length=1500, verbose_name="Linkedin", blank=True)
    instagram = models.CharField(max_length=1500, verbose_name="Instagram", blank=True)
    twitter = models.CharField(max_length=1500, verbose_name="Twitter", null=True, blank=True)
    slug = models.SlugField(editable=False, verbose_name="Slug")
    number_1 = models.CharField(max_length=100,verbose_name="Elaqe Nomresi",null=True)
    email = models.CharField(max_length=100,verbose_name="Email daxil edin",null=True,blank=True)


    def __str__(self):
        return ('%s') % (self.site_title)

    class Meta:
        verbose_name = "Tənzimləmə"
        verbose_name_plural = "Ümumi Tənzimləmələr"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = seo(self.site_title)
        super(GeneralSettings, self).save(*args, **kwargs)








class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    

class Country(models.Model):
    name = models.CharField(max_length=1000)
    image = models.FileField(upload_to="country_images")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="country")
    content = RichTextField(null=True)
    slug = models.SlugField(editable=False,null=True ,verbose_name="Slug")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = seo(self.name)
        super(Country, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('country_detail', kwargs={'slug': self.slug})
    



class faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
    


class Blog(models.Model):
    name = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="blog_image")
    slug = models.SlugField(editable=False,null=True ,verbose_name="Slug")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = seo(self.name)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})



class Service(models.Model):
    name = models.CharField(max_length=1000)
    short_intro = models.CharField(max_length=80, verbose_name="Short Intro size: 80",null=True)
    content = RichTextField()
    slug = models.SlugField(editable=False,null=True ,verbose_name="Slug")


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = seo(self.name)
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})
    



        
class Testimonial(models.Model):
    name = models.CharField(max_length=1000)
    text = models.TextField(max_length=400,null=True)

    def __str__(self):
        return self.name
    

class Email(models.Model):
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return self.email
    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
        return self.email
    


class Team(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=200)
    image = models.FileField()
    facebook = models.CharField(max_length=500,null=True,blank=True)
    twitter = models.CharField(max_length=500,null=True,blank=True)
    linkedin = models.CharField(max_length=500,null=True,blank=True)


    def __str__(self):
        return self.name
    

class Adress(models.Model):
    name = models.CharField(max_length=1000)
    adress = models.TextField()

    def __str__(self):
        return self.name
    
    
    
    