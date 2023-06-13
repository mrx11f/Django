from django.urls import path
from blog import views
# from exemples import test_page

urlpatterns = [
    path("", views.index, name="index-page"),
    path("tes-page/", views.test_page, name="test-page"),
]
