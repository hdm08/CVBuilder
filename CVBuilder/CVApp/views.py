from django.shortcuts import render, redirect,get_object_or_404
from . import models, forms
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def Home(request):
    return render(request, 'home.html')
# ______________________________________________________________________________________________________________________


def Register(request):
    form=forms.CreateUserForm()
    if request.method=='POST':
        form=forms.CreateUserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form1':form})
# ______________________________________________________________________________________________________________________


def Login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.username = request.POST.get('username')
            form.password = request.POST.get('password1')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'login.html', {'form2':form})
# ______________________________________________________________________________________________________________________


def Logout(request):
    logout(request)
    return redirect('/')
# ______________________________________________________________________________________________________________________


def Dashboard(request):
    return render(request, 'dashboard.html')
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def PersonalInfo(request):
    Resume = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo(instance=Resume)
    if request.method == 'POST':
        form = forms.PersonalInfo(request.POST,request.FILES,instance=Resume)
        if form.is_valid():
            form.save()
            # shop.save()
            return redirect('PersonalInfo1')
    return render(request, 'info/PersonalInfo.html', {'form': form})
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def PersonalInfo1(request):
    Resume1 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo1(instance=Resume1)
    if request.method == 'POST':
        form = forms.PersonalInfo1(request.POST,instance=Resume1)
        if form.is_valid():
            form.save()
            return redirect('PersonalInfo2')
    return render(request, 'info/PersonalInfo1.html', {'form1': form})
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def PersonalInfo2(request):
    Resume2 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo2(instance=Resume2)
    if request.method == 'POST':
        form = forms.PersonalInfo2(request.POST,instance=Resume2)
        if form.is_valid():
            form.save()
            return redirect('PersonalInfo3')
    return render(request, 'info/PersonalInfo2.html', {'form2': form})
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def PersonalInfo3(request):
    Resume3 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo3(instance=Resume3)
    if request.method == 'POST':
        form = forms.PersonalInfo3(request.POST,instance=Resume3)
        if form.is_valid():
            form.save()
            return redirect('PersonalInfo4')
    return render(request, 'info/PersonalInfo3.html', {'form3': form})
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def PersonalInfo4(request):
    Resume4 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo4(instance=Resume4)
    if request.method == 'POST':
        form = forms.PersonalInfo4(request.POST,instance=Resume4)
        if form.is_valid():
            form.save()
            return redirect('PersonalInfo5')
    return render(request, 'info/PersonalInfo4.html', {'form4': form})
# ______________________________________________________________________________________________________________________




@login_required(login_url='login')
def PersonalInfo5(request):
    Resume5 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo5(instance=Resume5)
    if request.method == 'POST':
        form = forms.PersonalInfo5(request.POST,request.FILES,instance=Resume5)
        files = request.FILES.getlist('certificates')

        if form.is_valid():
            for f in files:
                for x in request.FILES.getlist("certificates"):
                    def process(f):
                        with open('C:/Users/harsh/CVBuilder/media/document/'+str(request.user)+ '/' + str(x), 'wb+') as destination:
                            for chunk in f.chunks():
                                destination.write(chunk)
                    process(x)
            form.save()
            return redirect('PersonalInfo7')
    return render(request, 'info/PersonalInfo5.html', {'form5': form})
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def PersonalInfo7(request):
    Resume7 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo7(instance=Resume7)
    if request.method == 'POST':
        form = forms.PersonalInfo7(request.POST,instance=Resume7)
        if form.is_valid():
            form.save()
            return redirect('PersonalInfo6')
    return render(request, 'info/PersonalInfo7.html', {'form7': form})
# ______________________________________________________________________________________________________________________


from .utils import render_to_pdf
from django.http import HttpResponse

@login_required(login_url='login')
def PersonalInfo6(request):
    Resume6 = get_object_or_404(models.Resume, user=request.user)
    form=forms.PersonalInfo6(instance=Resume6)
    form3 = forms.PersonalInfo3(instance=Resume6)
    form4 = forms.PersonalInfo4(instance=Resume6)

    if request.method == 'POST':
        form = forms.PersonalInfo6(request.POST,instance=Resume6)
        form3 = forms.PersonalInfo3(request.POST,instance=Resume6)
        form4 = forms.PersonalInfo4(request.POST,instance=Resume6)
        files = request.FILES.getlist('certificates')
        context = {
            "context": request.user.resume,
            "form3":form3,
            "form4":form4,
        }
        if form.is_valid():
            if request.POST.get('skills'):
                models.Resume.skills = request.POST.get('skills')

            for f in files:
                for x in request.FILES.getlist("certificates"):
                    def process(f):
                        with open('C:/Users/harsh/CVBuilder/media/document/' + str(request.user) + '/' + str(x),
                                  'wb+') as destination:
                            for chunk in f.chunks():
                                destination.write(chunk)
                    process(x)
                form.save()
            pdf = render_to_pdf('pdf.html',context)
            return HttpResponse(pdf, content_type='application/pdf')
    return render(request, 'info/PersonalInfo6.html', {'form6': form,})
#_______________________________________________________________________________________________________________________


@login_required(login_url='login')
def pdf_view(request):

    pdf = render_to_pdf('pdf.html')
    return HttpResponse(pdf, content_type='application/pdf')
#_______________________________________________________________________________________________________________________


@login_required(login_url='login')
def ChangePassword(request):
    if request.method == 'POST':
        passform = PasswordChangeForm(request.user, request.POST)
        if passform.is_valid():
            user = passform.save()
            update_session_auth_hash(request, user)  # Important!
            #messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        #else: messages.error(request, 'Please correct the error below.')
    else:
        passform = PasswordChangeForm(request.user)
    return render(request, 'ChangePassword.html', {'passform': passform})
# ______________________________________________________________________________________________________________________


@login_required(login_url='login')
def Resume(request):
    x=request.user.resume.skills
    y=x.split(',')
    x=request.user.resume.certificates
    form3 = forms.PersonalInfo3()
    form4 = forms.PersonalInfo4()
    return render(request,'resume.html',{'s':y,'form3':form3,'form4':form4})
# ______________________________________________________________________________________________________________________


def Contact(request):
    form=forms.ContactUsForm()
    if request.method=='POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            form.From = request.POST.get('Form')

            form.save()
            return redirect('mail')

    return render(request,'contact.html',{'Cform':form})
# ______________________________________________________________________________________________________________________


def About(request):
    return render(request,'about.html')
# ______________________________________________________________________________________________________________________


from django.shortcuts import render
from .filter import UserFilter

def search(request):
    resume_list = models.Resume.objects.all()
    resume_filter = UserFilter(request.GET, queryset=resume_list)

    form=forms.CompanyForm()
    if request.method=='POST':
        form = forms.CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filterdone')

    return render(request, 'filter.html', {'filter': resume_filter,'Cform':form})
# ______________________________________________________________________________________________________________________


def sendmail(request):
    return render(request, 'mail.html')
# ______________________________________________________________________________________________________________________


def FilterDone(request):
    return render(request, 'Fdone.html')


