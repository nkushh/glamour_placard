from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
@login_required(login_url='login')
def new_account(request):
    return render(request, 'mysite/home.html')


@login_required(login_url='login')
def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            messages.success(request, "Success! Account detail successfully recorded.")
            return redirect('dashboard:accounts')
        else:
            messages.error(request, "Error! Looks like a username with that email or password already exists.")
            return redirect('dashboard:accounts')
    else:
        return redirect('dashboard:accounts')

@login_required(login_url='login')
def all_accounts(request):
  accounts = User.objects.all()
  context = {
    'accounts' : accounts,
  }
  return render(request, 'dashboard/accounts.html', context)

@login_required(login_url='login')
def deactivate_account(request, account):
  account = get_object_or_404(User, pk=account)
  account.is_active = False
  account.save()
  messages.success(request, 'Account successfully deactivated')
  return redirect('dashboard:accounts')

@login_required(login_url='login')
def activate_account(request, account):
  account = get_object_or_404(User, pk=account)
  account.is_active = True
  account.save()
  messages.success(request, 'Account successfully re-activated')
  return redirect('dashboard:accounts')


@login_required(login_url='login')
def delete_account(request, account):
  account = get_object_or_404(User, pk=account)
  account.delete()
  messages.success(request, 'Account successfully deleted')
  return redirect('dashboard:accounts')
