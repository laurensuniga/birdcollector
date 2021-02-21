from django.shortcuts import render

from django.http import HttpResponse

class Bird:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

birds = [
    Bird('Charles', 'Falcon', 'fast flyer', 2),
    Bird('Rick', 'Pigeon', 'loves letters', 1),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'birds/index.html', {'birds': birds})
