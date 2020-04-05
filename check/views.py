from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import JsonResponse
from main import main
# Create your views here.

'''
    Рендер страницы со статистикой сайта
'''
def main(request):
    data = main(request)
    return render(request, 'site/index.html', {'mark': data[0],'uncorrectword':data[1],'weightNLP':data[2],'badWord':data[3],'client':data[4],'operator':data[5]}))