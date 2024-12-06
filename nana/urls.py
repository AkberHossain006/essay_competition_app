
from django.urls import path
from . import views

app_name = 'nana'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('system/', views.system, name='system'),


    path('competitions/', views.competitions, name='competitions'),
    path('competitions/<int:competition_id>/', views.competition, name='competition'),
    path('new_essay/<int:topic_id>/', views.new_essay, name='new_essay'),

]