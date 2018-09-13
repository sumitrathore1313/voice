from time import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from SKR.voice_gender import get_gender
# Create your views here.

class GenderDetectionView(View):

    def get(self, request):

        return render(request, "gender_detection.html")

    def post(self, request):
        file = request.FILES['audio_file']
        path = 'recording/' + str(time()) + file.name
        self.handle_uploaded_file(file, path)
        gender = get_gender(path)
        html = "<h1> system detected this voice as "+gender+" voice</h1>"
        return HttpResponse(html)

    def handle_uploaded_file(self, f, path):
        with open(path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


