from django import forms
from django.forms.widgets  import *
from .models import Article,School
class NameForm(forms.Form):
    your_fname = forms.CharField(label="Your first name",max_length=100)
    your_lname = forms.CharField(label="Your last name",max_length=100)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =["pub_date","headline","content","reporter"]

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields =["state","principal","phonenumber"]
        widgets ={
            "phonenumber": RadioSelect(),
            "state":Textarea(attrs={"cols":80,"rows":20})
        }