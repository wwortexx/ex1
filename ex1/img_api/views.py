from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import MImg


def index(request):
    return render(request, 'index.html')


def get_name(request, name):
    if request.method == 'GET':
        try:
            MImg.objects.all().get(name=name)
            return HttpResponse('true')
        except Exception:
            return HttpResponse('false')
    return 'false'


class ImgHandler(View):

    def get(self, request, name):
        img = get_object_or_404(MImg, name=name)
        name = name + '.jpg'
        return render(request, 'image.html', {'nme': name})

    def post(self, request, name):
        img = request.FILES['file']
        img.name = name + '.jpg';
        try:
            sv = MImg(name=name, content=img)
            sv.save()
        except:
            sv = get_object_or_404(MImg, name=name)
            sv.content = img
            sv.save()
        return render(request, 'image.html', {'nme': name + '.jpg'})

    def put(self, request, name):
        img = request.FILES['file']
        sv = MImg(name=name, content=img)
        sv.save()
        return render(request, 'image.html', {'nme': name + '.jpg'})
