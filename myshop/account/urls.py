from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetDoneView
from django.conf import settings



app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_confirm'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_complete'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
