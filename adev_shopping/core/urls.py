
from django.urls import path,include
from . import views
from .views import Home,DetailItem


app_name='core'

urlpatterns = [
  path('',Home.as_view(),name='home'),
  path('detail/<int:pk>/',DetailItem,name='detail_item')


]

