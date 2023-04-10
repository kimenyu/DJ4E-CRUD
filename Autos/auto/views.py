from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import Createform
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from auto.models import Make
from django.urls import reverse_lazy
from django.views.generic.list import ListView




# Create your views here.

def home(request):
	return render(request, 'auto/main.html')

def index(request):
	return render(request, 'auto/crud.html')

def registerpage(request):
	form = Createform(request.POST or None)
	context = {'form': form}
	if form.is_valid():
		user = form.save()
		return redirect('login')
	return render(request, 'auto/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'auto/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


def view_make(request):
	return render(request, 'auto/autos.html')

class MakeCreateView(CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos')
    def form_valid(self, form):
    	form.instance.user = self.request.user 
    	return super().form_valid(form)

def list_makes(request):
	return render(request, 'auto/list_autos.html')

class MakeListView(ListView):
	model = Make
	context_object_name = 'make_list'#This sets the name of the variable that will be used in the template to access the list of objects retrieved from the model.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context



class MakeDeleteView(DeleteView):
    model = Make
    success_url = reverse_lazy('autos')

class MakeUpdateView(UpdateView):
    model = Make
    fields = '__all__'
    context_object_name = 'make_list'
    success_url = reverse_lazy('autos')