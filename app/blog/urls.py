from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('blog_detail/<slug>/',blog_detail, name="blog_detail"),
    path('service_detail/<slug>/',service_detail, name="service_detail"),
    path('country_detail/<slug>/',country_detail, name="country_detail"),
    path('about/',about, name="about"),
    path('export-emails/',export_emails_as_text, name="expor-emails"),
    path('contact-us/',contact, name="contact-us"),
    path('blogs/',blog, name="blogs"),
    path('events/',events,name="events"),
    path('event_detail/<slug>/',event_detail,name="event_detail"),
    path('students/',students,name="students"),
    path('student_detail/<slug>/',student_detail,name="student_detail")

]
