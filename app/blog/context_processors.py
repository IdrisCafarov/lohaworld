from blog.models import *

def extras(request):
    context={}
    context['settings'] = GeneralSettings.objects.all()
    
    
    return context