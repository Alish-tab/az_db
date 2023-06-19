from rest_framework.viewsets import ModelViewSet

from .models import (CSGO, FIFA, Dota2, Game, Gamer, Host, Match, Part, Team,
                     Tournoment)
from .serializers import (GamerSerializer, GameSerializer, HostSerializer,
                          InputCSGOSerializer, InputDota2Serializer,
                          InputFIFASerializer, InputMatchSerializer,
                          InputTournomentSerializer, OutputCSGOSerializer,
                          OutputDota2Serializer, OutputFIFASerializer,
                          OutputMatchSerializer, OutputTournomentSerializer,
                          PartSerializer, TeamSerializer)


class GamerViewSet(ModelViewSet):
    queryset= Gamer.objects.all()
    serializer_class = GamerSerializer

    
class GameViewSet(ModelViewSet):
    queryset= Game.objects.all()
    serializer_class = GameSerializer


class PartViewSet(ModelViewSet):
    queryset= Part.objects.all()
    serializer_class = PartSerializer

        
class TeamViewSet(ModelViewSet):
    queryset= Team.objects.all()
    serializer_class = TeamSerializer


class HostViewSet(ModelViewSet):
    queryset= Host.objects.all()
    serializer_class = HostSerializer



class TournomentViewSet(ModelViewSet):
    queryset= Tournoment.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutputTournomentSerializer
        else:
            return InputTournomentSerializer



class MatchViewSet(ModelViewSet):
    queryset= Match.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutputMatchSerializer
        else:
            return InputMatchSerializer



class CSGOViewSet(ModelViewSet):
    queryset= CSGO.objects.all()
    

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutputCSGOSerializer
        else:
            return InputCSGOSerializer


class Dota2ViewSet(ModelViewSet):
    queryset= Dota2.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutputDota2Serializer
        else:
            return InputDota2Serializer

class FIFAViewSet(ModelViewSet):
    queryset= FIFA.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutputFIFASerializer
        else:
            return InputFIFASerializer

