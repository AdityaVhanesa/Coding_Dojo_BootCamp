from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('player_name_record', views.PlayerNameRecord.as_view(), name='player_name_record'),
    path('game', views.PlayGame.as_view(), name='play_game'),
    path('process_number', views.ProcessNumber.as_view(), name='process_data'),
    path('game_complete', views.CompleteGame, name='complete_game')
]