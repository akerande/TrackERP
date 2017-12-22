from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render,redirect

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')

            # f.fullname = firstname + lastname
            instance.save()
            user = authenticate(username=username, password=raw_password)
            g = Group.objects.get(name='Labeller')
            g.user_set.add(user)
            u = User.objects.get(username=username)
            f = Employee.objects.get(user=u)
            #print(u)
            #print (str(f))
            f.fullname = firstname + " " + lastname
            f.save()

            auth.login(request, user)
            message = "Thank you for register with TrackerPRO,Kindly Login with your username and password."
            return redirect('/accounts/login',{message:'message'})
    else:
        form = RegistrationForm()
    return render(request,'registration/register.html', {'form' : form})