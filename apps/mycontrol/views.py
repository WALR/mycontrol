from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView



class MainView(TemplateView):
    
    template_name = 'index.html'
    