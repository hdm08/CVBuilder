from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (formset_factory, modelformset_factory)
from django.forms import ClearableFileInput
from django_select2.forms import Select2MultipleWidget

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']


class PersonalInfo(forms.ModelForm):
    birth_date=forms.CharField()
    picture = forms.FileField(widget=forms.FileInput)
    class Meta:
        model=models.Resume
        fields=['picture','first_name','middle_name','last_name','gender','birth_date',

                # 'email','Address','city','state','Postal_Zip_Code','Phone_Number',
                #
                # 'ssc_school','ssc_board','ssc_year_of_passing','ssc_percentage', 'hsc_school','hsc_board','hsc_year_of_passing','hsc_percentage',
                #
                # 'ug_college','ug_university','ug_collage_cgpa','ug_degree','pg_college','pg_university','pg_collage_cgpa','pg_degree',
                #
                # 'skills','any_other_qualification','internship_experience',
                #
                # 'certificates','about_you'

                ]




class PersonalInfo1(forms.ModelForm):
    class Meta:
        model=models.Resume
        fields=['email','Address','city','state','Postal_Zip_Code','Phone_Number']


class PersonalInfo2(forms.ModelForm):
    class Meta:
        ssc_year_of_passing=forms.IntegerField()
        model=models.Resume
        fields=['ssc_school','ssc_year_of_passing','ssc_percentage', 'hsc_school','hsc_year_of_passing','hsc_percentage',]

class PersonalInfo3(forms.ModelForm):
    pg_college=forms.CharField(label='Post Graduation', required=False)
    class Meta:
        model=models.Resume
        fields=['ug_college','ug_collage_cgpa','ug_degree','pg_college','pg_collage_cgpa','pg_degree',]




class PersonalInfo4(forms.ModelForm):
    any_other_qualification=forms.CharField(label='Other Qualifications',widget=forms.Textarea() ,required=False)
    class Meta:
        model=models.Resume
        fields=['any_other_qualification',]


class PersonalInfo5(forms.ModelForm):
    about_you = forms.FileField(widget=forms.FileInput)
    internship_experience = forms.CharField( widget=forms.Textarea(), required=False)

    class Meta:
        model=models.Resume
        fields=['about_you','internship_experience']


class PersonalInfo6(forms.ModelForm):
    certificates = forms.FileField(widget=forms.FileInput)

    class Meta:
        model=models.Resume

        fields=['skills','certificates']
        widgets = {
        # 'certificates': forms.FileField(attrs={'class': 'formset-field'}),

            'certificates': ClearableFileInput(attrs={'multiple': True})
        }


class PersonalInfo7(forms.ModelForm):

    class Meta:
        model=models.Resume
        fields=['Github','linkedin','facebook']



class ContactUsForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    From = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Your Email'}))
    Subject=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Subject'}))
    Message=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Message'}))
    class Meta:
        model=models.ContactUs
        fields=['username','From','Subject','Message']



class CompanyForm(forms.ModelForm):

    class Meta:
        model=models.Company
        fields=['company_name','job_title','location']


