from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Breed, Cat
from django.urls import reverse_lazy

# Create your views here.


class CatListView(ListView):
	model=Cat
	template_name='cats/cat_list.html'
	
class BreedCreateView(CreateView):
	model = Breed
	fields = '__all__'
	success_url = reverse_lazy('index')
	def form_valid(self, form):
		form.instance.user = self.request.user 
		return super().form_valid(form)

class BreedListView(ListView):
	model = Breed
	context_object_name = 'Breed_list'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BreedUpdateView(UpdateView):
	model = Breed
	fields = '__all__'
	context_object_name = 'Breed_list'
	success_url = reverse_lazy('index')

class BreedDeleteView(DeleteView):
	model = Breed
	success_url = reverse_lazy('breedView')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['mybreed'] = self.get_object()
		return context

class CatCreateView(CreateView):
	model = Cat
	fields = '__all__'
	success_url = reverse_lazy('index')
	def form_valid(self, form):
		form.instance.user = self.request.user 
		return super().form_valid(form)

class CatListView(ListView):
    model = Cat
    context_object_name = 'cat_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_list = self.get_queryset()
        context['cat_list'] = cat_list
        return context



class CatUpdateView(UpdateView):
    model = Cat
    fields = '__all__'
    context_object_name = 'cat_list'
  


class CatDeleteView(DeleteView):
	model = Cat
	success_url = reverse_lazy('index')
	