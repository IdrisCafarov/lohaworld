from django.contrib import admin
from .models import *

# Register your models here.



MAX_OBJECTS = 1

@admin.register(GeneralSettings)
class AdminGeneralSettings(admin.ModelAdmin):

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)


admin.site.register(Category)
admin.site.register(Country)
admin.site.register(faq)
admin.site.register(Blog)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Email)
admin.site.register(Contact)
admin.site.register(Team)
admin.site.register(Adress)