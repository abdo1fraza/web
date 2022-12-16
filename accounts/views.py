from django.shortcuts import render
from django.shortcuts import redirect
from .models import Profile
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate 
from django.contrib.auth import login


# Create your views here.


# def signup(request):
#     if request.method == 'POST':  # save form
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save() 
#             username=form.cleaned_data['username']
#             user = authenticate(username = username)
#             # login(request, user)
#             return redirect('/accounts/profile')

#     else :                        # show  form
#         form = SignupForm()

#     return render(request, 'registration/signup.html', {'form':form})


def signup(request):
    if request.method == 'POST':  # save form
        userform = UserForm(request.POST)
        profileform=ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save() 
            username=form.cleaned_data['username']
            user = authenticate(username = username)
            # login(request, user)
            return redirect('/accounts/profile')

    else :                        # show  form
        userform = UserForm()
        profileform=ProfileForm()

    return render(request, 'registration/signup.html', {'userform':userform ,'profileform': profileform})

def profile(request):
    pass
