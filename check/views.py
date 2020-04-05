from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import JsonResponse
# Create your views here.

def main(request):
    return render(request, 'site/index.html')