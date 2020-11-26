from django.urls import path

from . import views

urlpatterns = [
    # ex: /debts/
    path('', views.index, name='index'),
    # ex: /debts/5/
    path('<int:debt_id>/', views.detail, name='detail'),
    # ex: /debts/5/results/
    path('<int:debt_id>/results/', views.results, name='results'),
    # ex: /debts/5/vote/
    path('<int:debt_id>/vote/', views.vote, name='vote'),
]