from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_log:home'))
