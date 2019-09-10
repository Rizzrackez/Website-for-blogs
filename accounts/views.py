from django.shortcuts import render
from django.shortcuts import redirect
from accounts.forms import (
    UserUpdateForm,
    UserRegisterForm,
    ProfileUpdateForm,

)
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/reg_form.html', {'form': form})


# @login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your accounts hac been updated!')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'users': User.objects.all(),
    }

    return render(request, 'accounts/profile.html', context)


# @login_required
def change_password(request):

        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')

        else:
            form = PasswordChangeForm(user=request.user)
            messages.success(request, 'Your new password has been saved')

        args = {'form': form}
        return render(request, 'accounts/change-password.html', args)


