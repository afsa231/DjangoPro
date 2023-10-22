from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator,LANGUAGES

# Create your views here.
def homepage(request):
    return HttpResponse("my home")

def about(request):
    return HttpResponse("my about")

def translator(request):
    return render(request,'home/home.html')

def transistor(request):

    return render(request, "home/sum.html")


# def translate(request):
#     text = request.GET.get('text')
#     lang = request.GET.get('lang')
#     print('text :',text,'lang :',lang)
#     return render(request, "home/translate.html")
from django.shortcuts import render
from googletrans import Translator, LANGUAGES

def translate(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')

    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest=lang).text

    return render(request, "home/translate.html", {'text': text, 'lang': lang, 'translated_text': translated_text})
