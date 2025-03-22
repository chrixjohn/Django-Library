from django.shortcuts import render,redirect,get_object_or_404
from .forms import Formi
from .models import FormModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    if request.POST:
        frm = Formi(request.POST, request.FILES)  
        if frm.is_valid():
            print(request.POST.get('title'))
            frm.save()
            return HttpResponse("Thank you!")
        else:
            print(frm.errors)
    else:
        frm = Formi()

    return render(request, "index.html", {'frm': frm})

@login_required(login_url='/user/login/')
def display(request):
    content = FormModel.objects.all()
    return render(request, "display.html", {'books': content})

def edit(request, pk):
    # Retrieve the specific instance of FormModel or return a 404 error if not found
    instance = get_object_or_404(FormModel, pk=pk)
    
    # Handle POST request: process form submission
    if request.method == 'POST':
        frm = Formi(request.POST, request.FILES, instance=instance)
        if frm.is_valid():
            frm.save()
            return redirect('display')  # Redirect to the display page
    else:
        # Handle GET request: initialize the form with the existing instance
        frm = Formi(instance=instance)
    
    return render(request, "index.html", {'frm': frm})
    

# def edit(request,pk):
#     instance=FormModel.objects.filter(pk=pk)
#     print(instance)
#     frm=FormModel(request.POST,request.FILES,instance=instance)
#     return render(request, "index.html", {'frm': frm}) 


def delete(request,pk):
    instan=FormModel.objects.get(pk=pk)
    instan.delete()
    content = FormModel.objects.all()
    return redirect('display')
