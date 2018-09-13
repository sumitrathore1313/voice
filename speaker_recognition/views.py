from time import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from SKR.speaker_recognition import get_speaker
# Create your views here.

class SpeakerRecognitionView(View):

    def get(self, request):

        return render(request, "speaker_recognition.html")

    def post(self, request):
        file = request.FILES['audio_file']
        path = 'recording/' + str(time()) + file.name
        self.handle_uploaded_file(file, path)
        gender = get_speaker(path)
        html = "<h1> system detected this voice as "+gender+" voice</h1>"
        return HttpResponse(html)

    def handle_uploaded_file(self, f, path):
        with open(path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


