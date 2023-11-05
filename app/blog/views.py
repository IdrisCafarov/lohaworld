from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse



# Create your views here.


def index(request):
    context = {}

    categories = Category.objects.all()
    faqs = faq.objects.all().order_by("id")
    blogs = Blog.objects.all().order_by("-date")
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()


    if request.method == 'POST':
        form = CreateEmailForm(request.POST or None)
        if form.is_valid():
            form.save()
            # messages.success(request,'Congratulations,you successfully updated your informations!')
            return JsonResponse({'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'message': 'This Email already registered'})
    else:
        form = CreateEmailForm()












    context["categories"] = categories
    context["faqs"] = faqs
    context["blogs"] = blogs
    context["services"] = services
    context["testimonials"] = testimonials
    context["form"] = form

    return render(request,"index.html",context)


def blog_detail(request,slug):
    context = {}

    blog = get_object_or_404(Blog,slug=slug)

    context["blog"] = blog

    return render(request,"blog_detail.html",context)


def service_detail(request,slug):
    context = {}

    service = get_object_or_404(Service,slug=slug)

    services = Service.objects.all()

    context["services"] = services
    context["service"] = service

    return render(request,"service_detail.html",context)



def country_detail(request,slug):
    context = {}

    country = get_object_or_404(Country,slug=slug)

    countries = Country.objects.all()

    context["country"] = country
    context["countries"] = countries

    return render(request,"country_detail.html",context)


def about(request):
    context = {}

    teams = Team.objects.all()

    context["teams"] = teams
    return render(request,"about.html",context)


def export_emails_as_text(request):
    if request.user.is_authenticated:
        emails = Email.objects.all()
        email_text = "\n".join(f"{email.email}" for email in emails)
        response = HttpResponse(email_text, content_type="text/plain")
        response['Content-Disposition'] = 'attachment; filename="emails.txt"'
        return response
    else:
        return redirect("index")
    


def contact(request):

    context = {}

    if request.method == 'POST':
        form = CreateContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            # messages.success(request,'Congratulations,you successfully updated your informations!')
            return JsonResponse({'message': 'Form submitted successfully'})
    else:
        form = CreateContactForm()


    adresses = Adress.objects.all()


    context["form"] = form
    context["adresses"] = adresses



    return render(request,"contact.html",context)


def blog(request):

    context = {}
    blogs = Blog.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(blogs, 2)
    
    try:
        blogs=paginator.page(page)
    
    except PageNotAnInteger:
        blogs= paginator.page(1)
    except EmptyPage:
    
        blogs=paginator.page(paginator.num_pages)



    context["blogs"] = blogs


    return render(request,"blog.html",context)
