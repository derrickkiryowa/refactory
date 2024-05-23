from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddBabyForm, AddSitterForm, DollForm, ProcurementForm, AssignProcurementForm, DollSalesForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# from django import forms
from django.contrib.auth.decorators import login_required
from .models import *

#django messages
from django.contrib import messages

# Create your views here.
def home(request):


    return render(request,'webapp/index.html')


# register a user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Account created successfully!')

            return redirect('my_login')
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


# login a user
def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
    
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')
    context = {'form': form}

    return render(request, 'webapp/my_login.html', context=context)


# dashboard

@login_required(login_url='my_login')
def dashboard(request):
    return render(request, 'webapp/dashboard.html')


@login_required(login_url='my_login')
def baby(request):

    my_babylist = Baby.objects.all()
    context = {'babies': my_babylist}

    return render(request, 'webapp/baby.html', context=context)

# add /create new baby
@login_required(login_url='my_login')
def baby_reg(request):
    form = AddBabyForm()
    if request.method == 'POST':
        form = AddBabyForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, ' Your baby has been added successfully!')

            return redirect('baby')
    context = {'form': form}
    return render(request, 'webapp/baby_reg.html', context=context)

#edit baby
@login_required(login_url='my_login')
def babyedit(request, pk):
    baby = Baby.objects.get(id=pk)
    form = AddBabyForm(instance=baby)
    if request.method == 'POST':
        form = AddBabyForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()

            messages.success(request, ' Updated successfully!')

            return redirect('baby')
    context = {'form': form}
    return render(request, 'webapp/babyedit.html', context=context)


#view singular form
def baby_view(request, pk):
    babylist = Baby.objects.get(id=pk)
    context = {'baby': babylist}
    return render(request, 'webapp/baby_view.html', context=context)


# delete data

@login_required(login_url='my_login')
def baby_delete(request, pk):
    baby = Baby.objects.get(id=pk)
    baby.delete()

    messages.success(request, 'Deleted successfully!')
    
    return redirect('baby')






# sitters
@login_required(login_url='my_login')
def sitter(request):

    my_sitterlist = Sitter.objects.all()
    context = {'sitters': my_sitterlist}

    return render(request, 'webapp/sitter.html', context=context)


# add /create new sitter
@login_required(login_url='my_login')
def sitter_reg(request):
    form = AddSitterForm()
    if request.method == 'POST':
        form = AddSitterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, ' Your sitter has been added successfully!')


            return redirect('sitter')
    context = {'form': form}
    return render(request, 'webapp/sitter_reg.html', context=context)


#edit sitter
@login_required(login_url='my_login')
def sitteredit(request, pk):
    sitter = Sitter.objects.get(id=pk)
    form = AddSitterForm(instance=sitter)
    if request.method == 'POST':
        form = AddSitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()

            messages.success(request, 'Sitter record Updated successfully!')

            return redirect('sitter')
    context = {'form': form}
    return render(request, 'webapp/sitteredit.html', context=context)

#view singular form
def sitter_view(request, pk):
    sitterlist = Sitter.objects.get(id=pk)
    context = {'sitter': sitterlist}
    return render(request, 'webapp/sitter_view.html', context=context)


# delete data
@login_required(login_url='my_login')
def sitter_delete(request, pk):
    sitter = Sitter.objects.get(id=pk)
    sitter.delete()
    
    messages.success(request, 'Sitter Deleted successfully!')
    
    return redirect('sitter')



@login_required(login_url='my_login')
def doll(request):
    form = DollForm()
    if request.method == 'POST':
        form = DollForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('doll')
    
    return render(request, 'webapp/doll.html')



@login_required(login_url='my_login')
def procure(request):
    form = ProcurementForm()
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('procure')

    

    return render(request, 'webapp/procurement.html')



@login_required(login_url='my_login')
def assignprocure():
    form = AssignProcurementForm()
    if request.method == 'POST':
        form = AssignProcurementForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('assignprocure')



    return render(request, 'webapp/assignprocure.html')



@login_required(login_url='my_login')
def dollsale(request):
    form = DollSaleForm()
    if request.method == 'POST':
        form = DollSaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dollsale')


    return render(request, 'webapp/dollsale.html')










# logout a user
def user_logout(request):
    auth.logout(request)

    messages.success(request, 'Logout success!')

    return redirect('my_login')



            
