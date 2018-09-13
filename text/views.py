from time import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from SKR.google_speech import get_text
# Create your views here.

class TextView(View):

    def get(self, request):

        return render(request, "text.html")

    def post(self, request):
        file = request.FILES['audio_file']
        path = 'recording/' + str(time()) + file.name
        self.handle_uploaded_file(file, path)
        text = get_text(path)
        return HttpResponse(text)

    def handle_uploaded_file(self, f, path):
        with open(path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


