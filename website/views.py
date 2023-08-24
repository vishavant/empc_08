from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactUsForm, JoinUsForm


# from .forms import ContactUsForm

def homepage(request):
    return render(request, "website/homepage.html")

def display_courses(request):
    return render(request, "website/courses.html")


def about_us(request):
    return render(request, "website/about_us.html")


# def contact_us(request):
#     return render(request, "website/contact_us.html")

class ContactUs(CreateView):
    form_class = ContactUsForm
    # print(ContactUsForm)
    template_name = "website/contact_us.html"
    success_url = 'thanks' 


class JoinUs(CreateView):
    form_class = JoinUsForm
    # print(ContactUsForm)
    template_name = "website/join_us.html"
    success_url = 'thanks' 




def course_detail(request):
    return render(request, "website/course_detail.html")




class ThankYou(TemplateView):
    template_name = "website/thank_you.html"     


def starting_course_view(request):
    return render(request, "website/starting_detail_view.html")



def know_course_detail_view(request):
    return render(request, "website/know_detail_page.html")


def achieve_course_detail_view(request):
    return render(request, "website/achievment_detail_page.html")


def online_courses(request):
    return render(request, "website/online_course.html")    


def offline_courses(request):
    return render(request, "website/offline_courses.html")


