from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path("<int:question_id>/", views.detail,name="detail"),
    path("user/", views.user,name=""),
    path("article/", views.article,name=""),
    path("school/", views.school,name="school"),

]