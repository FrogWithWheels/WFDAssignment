from django.urls import path

from . import views

# pages
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:candidate_id>/", views.account, name="account")
]