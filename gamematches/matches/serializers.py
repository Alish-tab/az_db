from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Match ,Game ,Gamer ,Dota2 ,CSGO , FIFA ,Host ,Team , Part , Tournoment

        
class GamerSerializer(ModelSerializer):
    class Meta:
        model = Gamer
        fields = '__all__' 

class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__' 
        


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__' 

class HostSerializer(ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__' 


class OutputMatchSerializer(ModelSerializer):
    team_A = TeamSerializer()
    team_B= TeamSerializer()
    status = serializers.CharField(source="get_status_display")
    host =HostSerializer()
    winner = TeamSerializer()
    class Meta:
        model = Match
        fields = '__all__' 

class InputMatchSerializer(ModelSerializer):
   
    class Meta:
        model = Match
        fields = '__all__' 
        
class OutputDota2Serializer(ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Dota2
        fields = '__all__' 

class InputDota2Serializer(ModelSerializer):
    class Meta:
        model = Dota2
        fields = '__all__' 
class InputFIFASerializer(ModelSerializer):
 
    class Meta:
        model = FIFA
        fields = '__all__' 


class InputCSGOSerializer(ModelSerializer):
   
    class Meta:
        model = CSGO
        fields = '__all__' 


class OutputFIFASerializer(ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = FIFA
        fields = '__all__' 


class OutputCSGOSerializer(ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = CSGO
        fields = '__all__' 

class PartSerializer(ModelSerializer):

    class Meta:
        model = Part
        fields = '__all__' 

class InputTournomentSerializer(ModelSerializer):
    class Meta:
        model = Tournoment
        fields = '__all__' 



class OutputTournomentSerializer(ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    matches =OutputMatchSerializer(many=True)
    class Meta:
        model = Tournoment
        fields = '__all__' 
