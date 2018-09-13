from time import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from SKR.google_speech import get_language
# Create your views here.

class LanguageDetectionView(View):

    def get(self, request):

        return render(request, "laguage_detection.html")

    def post(self, request):
        file = request.FILES['audio_file']
        path = 'recording/' + str(time()) + file.name
        self.handle_uploaded_file(file, path)
        language_text = get_language(path)
        html = "<h1> system detected this voice language as "+language_text+" language</h1>"
        return HttpResponse(html)

    def handle_uploaded_file(self, f, path):
        with open(path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


