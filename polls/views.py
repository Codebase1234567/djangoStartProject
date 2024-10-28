from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.urls import reverse

from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Article,School
from .forms import NameForm,ArticleForm,SchoolForm

def index(request):
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list,}
    #return HttpResponse("Hello,world. you are at the polls index")
    return HttpResponse(template.render(context,request))



def detail(request,question_id):
    q = Question.objects.get(pk=question_id)
    #q = Question.objects.filter(id =1)
    
    return HttpResponse("you are looking at question %s"% q.question_text)



def user(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/user.html")
    context = {"form":form,}
    #return HttpResponse("Hello,world. you are at the polls index")
    return HttpResponse(template.render(context,request))


def thanks(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("thanks registering")
    #else:
        



def article(request):
    article = Article.objects.get(pk=1)
    form= ArticleForm()
    
    template = loader.get_template("polls/article.html")
    context = {"form":form,}
    #return HttpResponse("Hello,world. you are at the polls index")
    return HttpResponse(template.render(context,request))



def school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/polls/school/")
    school = School.objects.get(pk=1)
    form= SchoolForm()
    template = loader.get_template("polls/school.html")
    context = {"form":form,}
    #return HttpResponse("Hello,world. you are at the polls index")
    return HttpResponse(template.render(context,request))
