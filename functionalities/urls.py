from django.urls import path
from . import views


urlpatterns = [

    path('', views.FunctionalitiesListView.as_view(), name='func_list'),
    path('detail/', views.FunctionalitiesListView.as_view(), name='func_list')
]
