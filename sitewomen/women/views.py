from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.urls import reverse

from women.models import Women

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Биография Анджелины Джоли</h1> Анджели́на Джоли́ (англ. Angelina Jolie, произносится /dʒoʊˈliː/; 
    при рождении — Анджели́на Джоли́ Войт, англ. Voight; род. 4 июня 1975, Лос-Анджелес, США) — американская актриса кино, телевидения и озвучивания, 
    кинорежиссёр, сценаристка, продюсер, фотомодель и общественный деятель. Обладательница множества наград, включая «Оскар», «Тони» и три «Золотых глобуса». 
    Неоднократно признавалась самой высокооплачиваемой актрисой Голливуда. Её первые шаги в кино состоялись ещё в детстве, когда она снялась вместе с отцом, 
    Джоном Войтом, в фильме «В поисках выхода» (1982). Однако полноценная актёрская карьера началась лишь спустя десятилетие с малобюджетной 
    картины «Киборг 2» (1993), после чего последовала её первая главная роль в фильме «Хакеры» (1995).''', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

cats_db = [
    {'id':1, 'name': 'Актрисы'},
    {'id':2, 'name': 'Певицы'},
    {'id':3, 'name': 'Спортсменки'},
]

def index(request):
    posts = Women.objects.filter(is_published=1)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', data)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)

# def page_not_found(request, exeption):
#     return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# def server_error(request):
#     return HttpResponseServerError("<h1>Страница ваще бля не найдена</h1>")