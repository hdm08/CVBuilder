from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),

    path('', views.Home, name='home'),
    path('logout/', views.Logout, name="logout"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('ChangePassword', views.ChangePassword, name="ChangePassword"),
    # path('index/', views.Index, name='index'),
    path('resume/', views.Resume, name='resume'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('filter/', views.search, name='filter'),
    path('filterdone/', views.FilterDone, name='filterdone'),

    path('PersonalInfo/', views.PersonalInfo, name="PersonalInfo"),
    path('PersonalInfo1/', views.PersonalInfo1, name="PersonalInfo1"),
    path('PersonalInfo2/', views.PersonalInfo2, name="PersonalInfo2"),
    path('PersonalInfo3/', views.PersonalInfo3, name="PersonalInfo3"),
    path('PersonalInfo4/', views.PersonalInfo4, name="PersonalInfo4"),
    path('PersonalInfo5/', views.PersonalInfo5, name="PersonalInfo5"),
    path('PersonalInfo6/', views.PersonalInfo6, name="PersonalInfo6"),
    path('PersonalInfo7/', views.PersonalInfo7, name="PersonalInfo7"),
    path('mail/', views.sendmail, name='mail'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reset/password_reset.html',
             subject_template_name='reset/password_reset_subject.txt',
             email_template_name='reset/password_reset_email.html',
             success_url='done'
         ),name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='reset/password_reset_done.html'
         ),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reset/password_reset_confirm.html'
         ),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='reset/password_reset_complete.html'
         ),name='password_reset_complete'),

]