from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView

# def say_hello(request):
#     return render(request, 'hello.html', { 'name': 'Glenn'})
class HomeView(TemplateView):
    template_name='home.html'

class AboutView(TemplateView):
    template_name='about.html'