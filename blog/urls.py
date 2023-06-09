from django.urls import path
from blog.views import ContactsView, AboutView
from blog import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('test_page/', views.test_page, name="test-page"),
    # path('', ContactsView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]