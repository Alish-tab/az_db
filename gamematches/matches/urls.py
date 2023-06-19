from rest_framework.routers import SimpleRouter

from .views import (CSGOViewSet, Dota2ViewSet, FIFAViewSet, GamerViewSet,
                    GameViewSet, HostViewSet, MatchViewSet, PartViewSet,
                    TeamViewSet, TournomentViewSet)

router = SimpleRouter()

router.register("game", GameViewSet)
router.register("gamer", GamerViewSet)
router.register("match", MatchViewSet)
router.register("tour",TournomentViewSet)
router.register("fifa", FIFAViewSet)
router.register("csgo", CSGOViewSet)
router.register("dota2", Dota2ViewSet)
router.register("team", TeamViewSet)
router.register("host", HostViewSet)
router.register("part", PartViewSet)

urlpatterns= []

urlpatterns += router.urls 
