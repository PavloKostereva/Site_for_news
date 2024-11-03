from django.shortcuts import render
#from django.http import HttpResponse для простого тексту
def index(request):
    # data = {
    #     'title': 'Головна сторінка',
    #     'values': ['Some', 'Hello', '123'],
    #     'obj': {
    #         'car': 'BMW',
    #         'age': 18,
    #         'hobby': 'Football'
    #     }
    # }
    return render(request, 'main/index.html', {'title':'Головна сторінка'})
    # для нашого шаблону , який є в templates
    #return HttpResponse("<h4>Провірка роботи</h4>")

def about(request):
    return render(request, 'main/about.html')