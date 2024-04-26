from django.urls import path
from linky.views import index, create, root_link

urlpatterns = [
    path('', index, name="home"),
     path('create', create, name="create"),
     path('<str:link_slug>', root_link, name="root-link"),
]