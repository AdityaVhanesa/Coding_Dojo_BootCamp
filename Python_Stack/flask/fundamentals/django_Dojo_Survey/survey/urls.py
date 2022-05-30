from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('process', views.Process_Form.as_view(), name='process'),
    path('result', views.Result, name='redirect_result'),
    path('back_submit', views.BackSubmit, name='redirect_index')
]
