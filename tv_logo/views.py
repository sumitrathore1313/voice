from time import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from SKR.logo import detect_logo, detect_text


class TextView(View):

    def get(self, request):

        return render(request, "channel.html")

    def post(self, request):
        file = request.FILES['audio_file']
        path = 'recording/' + str(time()) + file.name
        self.handle_uploaded_file(file, path)
        text = detect_text(path)
        return HttpResponse(text)

    def handle_uploaded_file(self, f, path):
        with open(path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


class LogoView(View):

    def get(self, request):

        return render(request, "logo.html")

    def post(self, request):
        file = request.FILES['audio_file']
        path = 'recording/' + str(time()) + file.name
        self.handle_uploaded_file(file, path)
        text = detect_logo(path)
        return HttpResponse(text)

    def handle_uploaded_file(self, f, path):
        with open(path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)