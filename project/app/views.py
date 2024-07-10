from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .models import CustomeUser,medicine

from django.urls import reverse
from django.contrib import messages

# Create your views here.

def index(request):
     return redirect(home)
    #   return render(request,'user/home.html')
def home(request):
      return render(request,'home.html')
# ***************main login******
        
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')  # Redirect to the admin dashboard
            else:
                if user.usertype == "user":
                    return redirect('user_home')  # Redirect to the user profile
                elif user.usertype == "pharmacy" and user.status == "pending":
                    return redirect('pharm_home')  # Redirect to the pharmacy profile
                elif user.usertype == "admin":
                    return redirect('/admin/')  # Redirect to the admin dashboard
                else:
                    return HttpResponse("error")
        else:
            context = {
                'message': "Invalid credentials"
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect(Login)



#*************user**************

def user_register(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['Email']
            if CustomeUser.objects.filter(email=email).exists():
             return render(request,'user/register.html',{'error':'email already exists'})
            address = request.POST['Address']
            DOB = request.POST['DOB']
            phoneno = request.POST['Phonenumber']
            if CustomeUser.objects.filter(phone_number=phoneno).exists():
             return render(request,'user/register.html',{'error':'Phonenumber already exists'})
            age = request.POST['Age']
            username = request.POST['UserName']
            if CustomeUser.objects.filter(username=username).exists():
             return render(request,'user/register.html',{'error':'username already exists'})
            # password = make_password(request.POST['Password'])
            password =request.POST['Password']
            Confirmpassword=request.POST['Confirmpassword']
            if password!=Confirmpassword:
             return render(request,'user/register.html',{'error':'password not matching'})
            data=CustomeUser.objects.create_user(first_name=name,email=email,address=address,age=age,phone_number=phoneno,dob=DOB,password=password,username=username,usertype='user')
            data.save()
            # return HttpResponse('sucess')
            return render(request,'login.html')
        
            # return redirect(userhome)
        else:
            return render(request,'user/register.html')
            # return HttpResponse('sucess it')

def user_home(request):
      return render(request,'user/userhome.html')
def search(request):
    if request.method=='POST':
        Search=request.POST['search']
        user = CustomeUser.objects.filter(usertype='user',first_name__icontains=Search)
        return render(request,'user/userhome.html',{'users': user})
    else:
        return redirect(user_home)

def userprofile(request):
    users=CustomeUser.objects.get(id=request.user.id)
    return render(request,'user/profile.html',{'data':users})

def edit_profile(request):
    data=CustomeUser.objects.get(id=request.user.id)
    if request.method=='POST':
        data.first_name=request.POST['Name']
        data.age=request.POST['age']
        data.Phonenumber=request.POST['Phonenumber']
        data.DOB=request.POST['DOB']
        data.Address=request.POST['Address']
        data.email=request.POST['Email']  
        data.username=request.POST['UserName']
        data.save()
        return redirect(userprofile)
    else:
        return render(request,'user/editprofile.html',{'datas':data})
       
       
       
       
#        #***********pharmacy**********
       
def pharm_register(request):
    if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['Email']
            if CustomeUser.objects.filter(email=email).exists():
             return render(request,'pharmacy/registerp.html',{'error':'email already exists'})
            address = request.POST['Address']
           
            phoneno = request.POST['Phonenumber']
            if CustomeUser.objects.filter(phone_number=phoneno).exists():
             return render(request,'pharmacy/registerp.html',{'error':'username already exists'})
            username = request.POST['UserName']
            if CustomeUser.objects.filter(username=username).exists():
             return render(request,'pharmacy/registerp.html',{'error':'username already exists'})
            password = request.POST['Password']
            Confirmpassword=request.POST['Confirmpassword']
            if password!=Confirmpassword:
             return render(request,'pharmacy/registerp.html',{'error':'password not matching'})
            data=CustomeUser.objects.create_user(first_name=name,email=email,address=address,phone_number=phoneno,password=password,username=username,usertype='pharmacy')
            data.save()
            return render(request,'login.html')
    else:
           return render(request,'pharmacy/registerp.html')
            # return HttpResponse('sucess it')
            #  return render(request,'login.html')

def pharm_profile(request):
    user=CustomeUser.objects.get(id=request.user.id)
    return render(request,'pharmacy/profilep.html',{'data':user})


def edit_pharm(request):
    data=CustomeUser.objects.get(id=request.user.id)
    if request.method=='POST':
        data.first_name=request.POST['Name']
        data.age=request.POST['age']
        data.Phonenumber=request.POST['Phonenumber']
        data.DOB=request.POST['DOB']
        data.Address=request.POST['Address']
        data.email=request.POST['Email']  
        data.username=request.POST['UserName']
        data.save()
        return redirect(userprofile)
    else:
        return render(request,'pharmacy/edit profilep.html',{'datas':data})
    
def pharm_home(request):
#       return render(request,'pharmacy/homep.html')
    medicines = medicine.objects.filter(pharmacy_id=request.user)
    return render(request, 'pharmacy/homep.html', {'medicines': medicines})

def add_medicine(request):
    if request.method == 'POST':
        name = request.POST['medicineName']
        price = request.POST['pricePerUnit']
        description = request.POST['description']
        manufacturer = request.POST['manufacturer']
        quantity = request.POST['quantity']
        expiry_date = request.POST['expiryDate']
        brandname=request.POST['brandName']
        genericName=request.POST['genericName']
        strength=request.POST['strength']
        medicine_data = medicine.objects.create( pharmacy_id=request.user,name=name,price=price,strength=strength,brandname=brandname,genericname=genericName,description=description,manufacturer=manufacturer,quantity=quantity,expiry_date=expiry_date)
        medicine_data.save()
        return redirect('pharm_home')
        # return HttpResponse ('medicine_view')
    else:
        return render(request, 'pharmacy/medicine.html')
        # return HttpResponse('sucessfuly')

def edit_medicine(request,id):
    data=medicine.objects.get(id=id)
    if request.method=='POST':
        data.name=request.POST['medicineName']
        data. price = request.POST['pricePerUnit']
        data.description = request.POST['description']
        data.manufacturer = request.POST['manufacturer']
        data.quantity = request.POST['quantity']
        data.expiry_date = request.POST['expiryDate']
        data.brandname=request.POST['brandName']
        data.genericName=request.POST['genericName']
        data.strength=request.POST['strength']
        data.save()
        return redirect(pharm_home)
    else:
        return render(request,'pharmacy/edit_medicine.html',{'datas':data})
def delete_med(reuest,id):
    del_med=medicine.objects.get(id=id)
    del_med.delete()
    return redirect(pharm_home)


def medicine_view(request):
    addmedicine=medicine.objects.get(pharmacy_id=request.user)
    return render(request, 'pharmacy/viewmedicine.html',{'data':addmedicine})
    # return HttpResponse('sucess',{'data':addmedicine})