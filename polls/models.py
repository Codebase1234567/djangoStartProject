from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Article(models.Model):
    pub_date=models.CharField(max_length=200)
    headline=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    reporter=models.CharField(max_length=200)
    
    def __str__(self):
        return self.content



class School(models.Model):
    school = {
        "u":"unec",
        "h":"his grace",
        "c":"cic",
        "co":"command",
    }
    state=models.CharField(max_length=200)
    principal=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200,choices=school)
    
    def __str__(self):
        return self.state