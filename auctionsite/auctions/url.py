from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.my_login, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("register", views.Register, name="register"),
    path("create_list", views.create, name="create_list"),
    path("watch_list", views.Watch, name="watch_list"),
    path("categories", views.categories, name="categories"),
    path("watch/<int:good_id>/", views.watch, name="watch"),
    path("close/<int:good_id>/", views.close, name="close"),
]
