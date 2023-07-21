from django.shortcuts import render
from testapplication1.forms import formpAge

# Create your views here.
def homeView(request):
    form = formpAge()
    if request.method == 'POST':
        form = formpAge(request.POST)
        if form.is_valid():
            form.save()
        return listView(request)
    return render(request, 'html/home.html', {'form': form})


def listView(request):
    name = request.POST['name']
    request.session['name'] = name
    number = request.POST['number']
    request.session['number'] = number
    return render(request, 'html/list.html', {'name': name, 'number': number})