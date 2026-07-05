from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_coding, name='all_coding'),

    path('<int:coding_id>/', views.coding_detail, name='coding_detail'),

    path('code_store/', views.code_store, name='code_store'),

]
