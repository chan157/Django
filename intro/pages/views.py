from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    hello = 'hello :-)'
    lunch = "라멘"
    context = {
        'hello':hello,
        'l':lunch
    }
    return render(request, 'index.html', context)

def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'hello.html', context)

def calculate(request, num1, num2):
    context = {
        'multiple' : int(num1) * int(num2),
        'num1' : num1,
        'num2' : num2
    }
    return render(request, 'calculate.html', context)

def dtl(request):
    foods = ["자장면", '탕수육', '짬뽕', '양장피']
    sentence = "Life is short, you need python"
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'foods' : foods,
        'sentence' : sentence,
        'fruits' : fruits,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'dtl.html', context)

def bday(request):
    # 1. 오늘 날짜 가져오기
    today = datetime.now()
    # 2. month, day 가져와서 비교하기
    result = (today.month, today.day) == (1, 4)
    context = {
        'bday' : result
    }
    return render(request, 'bday.html', context)