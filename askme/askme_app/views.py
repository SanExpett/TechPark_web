import random

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


el_on_one_pg = 7
def paginate(objects_list: list, page: int, e_on_p: int = el_on_one_pg):
    start_index = (page - 1) * e_on_p
    end_index = start_index + e_on_p
    return objects_list[start_index:end_index]


class Index(View):
    def get(self, request, page=1):
        questions = [{
            'id': i,
            'title': 'title ' + str(i),
            'text': 'text' + str(i),
            'like_count': random.randint(0, 100)
        } for i in range(35)]

        pages = len(questions) // el_on_one_pg
        questions = paginate(questions, page)

        context = {
            'pages': range(1, pages + 1),
            'questions': questions
        }

        return render(request, 'index.html', context)


class Question(View):
    def get(self, request):
        new = request.GET.get('new', False)
        if new:
            return render(request, 'ask.html')

        page = request.GET.get('page', 1)

        comments = [{
            'id': i,
            'content': 'title ' + str(i),
            'likes_count': random.randint(0, 100)
        } for i in range(35)]
        pages = len(comments) // 7
        comments = paginate(comments, page, e_on_p=7)
        context = {
            'comments': comments,
            'pages': range(1, pages + 1)
        }
        return render(request, 'question.html', context=context)

    def post(self, request):
        return HttpResponse(200)



class Settings(View):
    def get(self, request):
        return render(request, 'settings.html')


class Tag(View):
    def get(self, request):
        return render(request, 'tag.html')


class Signup(View):
    def get(self, request):
        return render(request, 'sign_up.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')




