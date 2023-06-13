from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def get_contacts():
    return "Контактная информация"


def get_about():
    return "О нас"


class ContactsView(View):
    def get(self, request):
        contacts = get_contacts()
        return HttpResponse(contacts)


class AboutView(View):
    def get(self, request):
        about = get_about()
        return HttpResponse(about)

