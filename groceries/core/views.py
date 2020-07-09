from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your tests here
from django.shortcuts import render, redirect

from core.models import Customer, User


def front_page(request):
    return render(request, 'front.html')


def signin(request):
    if request.method == 'POST':
        print(2)
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        print(1)
        print(5)
        user = authenticate(request, username=username, password=password)
        if not user:
            return HttpResponse('<h1>Invalid Customer</h1>')
        else:
            login(request, user)
            return redirect("front/")
    else:
        print(3)
        return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', "")
        username = request.POST.get('username', "")
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        password = request.POST.get('psw', "")
        mobile_number = request.POST.get('phone', "")
        gender = request.POST.get("gender", None)
        x = Customer.objects.create_user(password=password, username=username, first_name=first_name,
                                         last_name=last_name,
                                         email=email, phone=mobile_number, gender=gender)
        x.save()
        return HttpResponse('<h1>Thanks</h1>')

    else:
        return render(request, 'signup.html')


def front(request):
    user_front = request.user.username
    cust_object = User.objects.get(username=user_front)
    firstname = cust_object.first_name
    lastname = cust_object.last_name
    email = cust_object.email
    phone = cust_object.phone

    return render(request, 'first_page.html', {'h': user_front, 'name': firstname, 'lastname': lastname,
                                               'email': email, 'phone': phone})


def edit(request):
    if request.method == 'GET':
        user_front = request.user.username
        cust_object = User.objects.get(username=user_front)
        firstname = cust_object.first_name
        lastname = cust_object.last_name
        email = cust_object.email
        phone = cust_object.phone
        if phone == '':
            phone = 'NotUpdated'
        return render(request, 'editform.html', {'username': user_front, 'name': firstname, 'lastname': lastname,
                                                 'email': email, 'phone': phone, })
    else:
        user_front = request.user.username
        cust_object = User.objects.get(username=user_front)
        cust_object.firstname = request.POST.get('first_name', '')
        cust_object.lastname = request.POST.get('last_name', '')
        cust_object.hrdd = request.POST.get('email', '')
        if cust_object.hrdd == "":
            print("NOT UPdate")
        else:
            cust_object.email = cust_object.hrdd
        cust_object.phone1 = request.POST.get('phone', '')
        if cust_object.phone1 == '':
            print('Not Update')
        else:
            cust_object.phone = cust_object.phone1

        cust_object.save()
        return HttpResponse('<h1>DATA Updated Sucessfull</h1>')
