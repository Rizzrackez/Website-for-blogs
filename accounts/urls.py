from django.urls import path, include
from accounts.views import *
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'accounts'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('user_profile/<int:pk>', user_profile, name='user_profile'),
    path('profile/settings/', profile_settings, name='profile_settings'),
    path('password_reset/', auth_views.PasswordResetView.as_view( template_name='accounts/password_reset.html', success_url = reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'accounts/password_reset_confirm.html'), name='password_reset_confirm'),
]
