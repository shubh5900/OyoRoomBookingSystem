from django.shortcuts import render,redirect

from .models import Customer

# Create your views here.

def home(request):
    cus=Customer.objects.all()

    return render(request,"oyo/home.html",{'cus':cus})

def add_customer(request):
    if request.method == "POST":
        roll=request.POST['roll']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Address = request.POST['Address']
        Customer(roll=roll,name=name,email=email,phone=phone,Address=Address).save()
        return redirect('oyo/home.html')
    
    return render(request,'oyo/add_customer.html',)

def delete_customer(request,id):
    c=Customer().objects.get(id=id)
    c.delete()
    return redirect("oyo/home")
    

def update_customer(request,id):
    c=Customer().objects.get(id=id)
    return redirect("oyo/update_oyo",{'c':c})


    


