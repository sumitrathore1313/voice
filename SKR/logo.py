import os
from time import sleep

import cv2
from google.cloud import vision
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/sumit/Documents/sumit/gcp/My First Project-9067fbfb3502.json"

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    img = cv2.imread(path)
    img = img[250:290, 200:400]
    content = cv2.imencode('.jpg', img)[1].tobytes()
    # with io.open(path, 'rb') as image_file:
    #     content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print(texts[0].description)
    texts = texts[0].description
    print('Channel Number : {}, Channel Name : {}'.format(texts.split()[0], " ".join(texts.split()[1:])))
    channel_name = " ".join(texts.split()[1:])
    channel_num = texts.split()[0]
    return "channel num is "+channel_num+" <br> channel name is "+channel_name
    # for text in texts:
    #     print('\n"{}"'.format(text.description))
    #
    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))


# detect_text("/home/sumit/Desktop/image_mapping/SKR/data/1068/01-08-2018 12 44 04/15.jpg")
# path = "/home/sumit/Desktop/image_mapping/SKR/data/1068/01-08-2018 12 44 04/14.jpg"