from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    # path('',views.home, name='home'),
    # path('login/',login, {'template_name': 'accounts/login.html'})
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/',views.register, name='register'),
    path('profile/',views.view_profile, name='view_profile'),
    path('profile/<int:pk>/',views.view_profile, name='view_profile_with_pk'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
    path('change-password/',views.change_password, name='change_password'),
    path('reset-password/',PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='PasswordResetView'),
    path('reset-password/done',PasswordResetDoneView.as_view(),name='PasswordResetDoneView'),
    # path('reset-password/confirm',PasswordResetConfirmView.as_view(),name='PasswordResetConfirmView')
    path('reset-password/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # python -m smtpd -n -c DebuggingServer localhost:1025(to satrt mesg in cmd)
]