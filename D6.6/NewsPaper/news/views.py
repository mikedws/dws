# from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView # импортируем класс ListView, который говорит нам о том, 
# что в этом представлении мы будем выводить список объектов из БД
# импортируем класс DetailView получения деталей объекта
from .models import Post
# from datetime import datetime
 
 
class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, 
    # в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, 
    # его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation') # сортировка по дате публикации, сначала более новые


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html' # название шаблона будет product.html
    context_object_name = 'post' # название объекта
