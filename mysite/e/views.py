from django.shortcuts import render,redirect
from e.models import Course

# Create your views here.

def view(request):
    courses = Course.objects.all()
    return render(request,'e/view.html',{'courses':courses})

def delete(request,pk):
    courses = Course.objects.get(pk=pk)
    if request.method == 'POST':
        courses.delete()
        return redirect('/')
    else:
        return render(request,'e/view.html',{'courses':courses})
