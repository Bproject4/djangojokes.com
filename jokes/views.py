#from django.views.generic import ListView
#from django.views.generic import DetailView, ListView
#from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from .models import Joke
from django.urls import reverse_lazy

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']        

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')