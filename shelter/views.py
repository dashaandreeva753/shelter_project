from django.shortcuts import render
from shelter.models import Pet


def index(request):  # главная страница
    return render(request, "shelter/index.html")


def cat_list(request):  # список котов
    cats = Pet.objects.all()
    context = {
        'cat_list': cats,
    }
    return render(request, 'shelter/pet_list.html', context)


def cat_detail(request, pk):
    cat = Pet.objects.get(pk=pk)
    context = {
        'cat': cat,
    }
    return render(request, 'shelter/pet_detail.html', context)


def shelter_detail(request,):
    return render(request, 'shelter/shelter_detail.html')


def help_detail(request):
    return render(request, 'shelter/help.html')
