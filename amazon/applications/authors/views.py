from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Profile


class UserCreateView(generic.CreateView):
    model = User
    template_name = 'users/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main-page')
    
    def form_valid(self, form):
        valid = super(UserCreateView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid


class UserProfileView(generic.DetailView):
    model = Profile
    template_name = "users/profile.html"
    context_object_name = 'profile'
    
    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return get_object_or_404(Profile, user=user)

    
class UserUpdateView(generic.UpdateView):
    model = Profile
    template_name = "users/update.html"
    context_object_name ="update"
    form_class = UserCreationForm

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return get_object_or_404(Profile, user=user)

    