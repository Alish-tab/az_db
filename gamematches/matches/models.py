from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length = 50)
    number_of_team  = models.PositiveIntegerField(default = 0)
    created_by = models.CharField(max_length = 50)
    creatred_at = models.DateTimeField(auto_now_add =True)
    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    number_of_player  = models.PositiveIntegerField(default = 0)
    creatred_at = models.DateTimeField(auto_now_add =True)
    def __str__(self) -> str:
        return self.name


class Gamer(AbstractUser):
   country = models.CharField(max_length=50 ,null=True,blank=True)
   team = models.ForeignKey(Team, null =True , blank = True , on_delete=models.CASCADE)
   creatred_at = models.DateTimeField(auto_now_add =True)


class Host(models.Model):
    count_name= models.CharField(max_length=50)
    stud_name = models.CharField(max_length=50)
    creatred_at = models.DateTimeField(auto_now_add =True)
    def __str__(self) -> str:
        return self.stud_name


class Match(models.Model):
    
    STATUS =(('D','done'),
    ('Q','In Queue'),
    ('P','In Process'))
    team_A = models.ForeignKey(Team,related_name='teamA' ,on_delete=models.CASCADE)
    score_A= models.IntegerField(default= 0,blank=True ,null =True)
    team_B = models.ForeignKey(Team,related_name='teamB', on_delete=models.CASCADE)
    score_B= models.IntegerField(default= 0,blank=True ,null =True)
    game = models.CharField(max_length=50 )
    title = models.CharField(max_length=50,blank=True ,null =True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    status  = models.CharField(max_length=1 ,choices = STATUS)
    time  = models.DateTimeField(default=timezone.now)
    winner = models.OneToOneField(Team ,blank=True ,null =True,on_delete=models.CASCADE)
    is_equal = models.BooleanField(default=False)
    creatred_at = models.DateTimeField(auto_now_add =True)
    def __str__(self) -> str:
        return f'{self.game} | {self.host}'


class Dota2(models.Model):
    team  = models.ForeignKey(Team , on_delete=models.CASCADE)
    point = models.IntegerField(default= 0)
    total_game = models.PositiveIntegerField(default = 0)
    win = models.IntegerField(default= 0)
    lose = models.IntegerField(default= 0)
    class Meta:
        ordering = ["point",]
    def __str__(self) -> str:
        return f'{self.team}'


class CSGO(models.Model):
    team  = models.ForeignKey(Team, on_delete=models.CASCADE)
    point = models.IntegerField(default= 0)
    total_game = models.PositiveIntegerField(default = 0)
    equal  = models.IntegerField(default= 0)
    win = models.IntegerField(default= 0)
    lose = models.IntegerField(default= 0)
    def __str__(self) -> str:
        return f'{self.team}'
    class Meta:
        ordering = ["point",]
        
class FIFA(models.Model):
    team  = models.ForeignKey(Team, on_delete=models.CASCADE)
    point = models.IntegerField(default= 0)
    total_game = models.PositiveIntegerField(default = 0)
    equals  = models.IntegerField(default= 0)
    wins = models.IntegerField(default= 0)
    goals = models.IntegerField(default= 0)
    lose = models.IntegerField(default= 0)
    recgoals = models.IntegerField(default= 0)
    def __str__(self) -> str:
        return f'{self.team}'
    class Meta:
        ordering = ["point",]



class Tournoment(models.Model):
    STATUS =(('D','done'),
    ('Q','In Queue'),
    ('P','In Process'))
    title = models.CharField(max_length=50,blank=True ,null =True)     
    game = models.CharField(max_length=50)
    status  = models.CharField(max_length=1 ,choices = STATUS)
    time  = models.DateTimeField(default=timezone.now)
    creatred_at = models.DateTimeField(auto_now_add =True)
    matches = models.ManyToManyField(Match)
    
class Part(models.Model):
    gamer =  models.ForeignKey(Gamer, on_delete=models.CASCADE)
    team =  models.ForeignKey(Team, on_delete=models.CASCADE)
    creatred_at = models.DateTimeField(auto_now_add =True)
    game =  models.ForeignKey(Game, on_delete=models.CASCADE)
