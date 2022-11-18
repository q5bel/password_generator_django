from django.shortcuts import render
from random import *

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def generate_password(length, chars):
    new_pass = ''
    for _ in range(int(length)):
        new_pass += choice(chars)
    return new_pass


def password(request):
    chars = ''
    length = request.GET.get('length')

    parameters = [True, request.GET.get('uppercase'), request.GET.get('numbers'), request.GET.get('special'), request.GET.get('illegal')]
    digits = ['abcdefghjkmnpqrstuvwxyz', 'ABCDEFGHJKMNPQRSTUVWXYZ', '23456789', '!#$%&*+-=?@^_', "il1Lo0O"]

    cnt = 0
    for i in parameters:
        if i:
            chars += digits[cnt]
        cnt += 1

    the_password = generate_password(length, chars)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')