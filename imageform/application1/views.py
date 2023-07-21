from django.shortcuts import render, redirect
from application1.forms import HotelForm

# Create your views here.
def homeView(request):
    return render(request, 'html/home.html')

def formView(request):
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/getform/page3/')
    return render(request, 'html/form1.html', context={'form': form})

def lastView(request):
    return render(request, 'html/last.html')