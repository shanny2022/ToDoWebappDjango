from django.contrib import admin
from django.urls import path
from todo import views   # 👈 import your app's views

urlpatterns = [
    path('', views.index, name="todo"),                 # home page (list + add items)
    path('del/<str:item_id>', views.remove, name="del"),  # delete item by id
    path('admin/', admin.site.urls),
]
