from dataclasses import fields
from modeltranslation.translator import translator,TranslationOptions
from blog.models import *


class GeneralOptions(TranslationOptions):
    fields = ('site_title','adress',)
    

translator.register(GeneralSettings,GeneralOptions)



class CategoryOptions(TranslationOptions):
    fields = ('name',)
    

translator.register(Category,CategoryOptions)


class CountryOptions(TranslationOptions):
    fields = ('name','content',)
    

translator.register(Country,CountryOptions)


class FAQOptions(TranslationOptions):
    fields = ('question','answer')
    

translator.register(faq,FAQOptions)


class BlogOptions(TranslationOptions):
    fields = ('name','content')
    

translator.register(Blog,BlogOptions)





class ServiceOptions(TranslationOptions):
    fields = ('name','short_intro','content')
    

translator.register(Service,ServiceOptions)



class TestimonialOptions(TranslationOptions):
    fields = ('name','text',)
    

translator.register(Testimonial,TestimonialOptions)



class TeamOptions(TranslationOptions):
    fields = ('name','position',)
    

translator.register(Team,TeamOptions)



class StudentOptions(TranslationOptions):
    fields = ('name','country','major','content',)
    
translator.register(Student,StudentOptions)



