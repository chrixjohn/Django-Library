from django.shortcuts import render
from django.http import HttpResponse
from .forms import Form
from lib.models import FormModel

# Create your views here.
def member(request):
   
    if request.method == "POST":
        
        form = Form(request.POST)
        print(form)
       
        if form.is_valid():
            form.save()
            selected_category = form.cleaned_data['category']
            queryset=FormModel.objects.all()
            print(queryset)
            for book in queryset:

                if str(book.title) == str(selected_category):
                    print(book.title)
                    book.status=False
                    book.save()
            print("chrois",selected_category)
            return HttpResponse("thanku")

   
    else:
        form = Form()

    return render(request, "member.html", {"form": form})