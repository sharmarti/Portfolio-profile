
from django.shortcuts import render
from index.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        concern=request.POST['concern']
        print(name,email,mobile,concern)
        obj=Contact(name=name,email=email,mobile=mobile,concern=concern)
        obj.save()
        
    return render(request,'contact.html')
