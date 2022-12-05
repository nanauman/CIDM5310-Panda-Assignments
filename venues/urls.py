from django.urls import path
from . import views

urlpatterns = [
    path('drvenue/', views.DrvenuePageView.as_view(), name='drvenue'),
    path('brats/', views.BratsPageView.as_view(), name='brats'),
    path('majestic/', views.MajesticPageView.as_view(), name='majestic'),
    path('bowl/', views.BowlPageView.as_view(), name="bowl"),
    path('sylvee/', views.SylveePageView.as_view(), name="sylvee"),
    path('orpheum/', views.OrpheumPageView.as_view(), name="orpheum"),
    path('venue_form', views.Venue_formPageView.as_view(), name='venue_form'),


]
