from django.urls import path, include
from.import views, models

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('register', views.register),
    path('log', views.log),
    path('logout', views.logout),
    path('post_to_wall', views.message),
    path('wall', views.wall),
    path('post_comment/<int:val>', views.comments),
    path('destroy/<int:val>', views.delete)
]