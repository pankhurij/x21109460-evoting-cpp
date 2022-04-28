from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.question_list, name ='question_list'),
	path('<int:question_id>/', views.question, name ='question'),
	path('<int:question_id>/results/', views.results, name ='results'),
	path('<int:question_id>/vote/', views.vote, name ='vote'),
]
