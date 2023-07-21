from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages

# Create your views here.
def ContentPage(request):
    return render(request, 'html/content_page.html')

def ContactDetails(request):
    return render(request, 'html/contact_detail.html')

def RegisterLogin(request):
    return render(request, 'html/register_login.html')


def register_request(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            login.save()
            messages.success(request, 'Registration successful.')
        return HttpResponseRedirect('/accounts/login/')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    return render(request=request, template_name='html/register.html', context={'register_form': form})