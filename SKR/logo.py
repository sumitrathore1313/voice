import os
from time import sleep
import os
import numpy as np
import cv2
from google.cloud import vision
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/sumit/Documents/sumit/gcp/My First Project-9067fbfb3502.json"

logo_path = "SKR/data/logo"
logo_path =  list(map(lambda s: logo_path+"/"+s, os.listdir(logo_path)))

def get4corner(image):
    x_size, y_size, _= image.shape
    img1 = image[:int(x_size/3), :int(y_size/3)]
    img2 = image[int(x_size*2/3):, :int(y_size/3)]
    img3 = image[:int(x_size/3), int(y_size*2/3):-1]
    img4 = image[ int(x_size*2/3):, int(y_size*2/3):-1]
    img = np.concatenate((img1, img2, img3, img4), axis=1)

    return img

def slide(image, logo):
    temp = []
    for i in range(0, len(image)-len(logo)):
        for j in range(0, len(image[0])-len(logo[0])):
            img = image[i:i+len(logo), j:j+len(logo[0])]

            temp.append(mse(img, logo))
            # temp.append(compare_ssim(img, logo, multichannel=True))

    return np.min(temp)


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

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

def detect_logo(path):
    logos = []
    for temp in logo_path:
        logos.append(cv2.imread(temp))
    img = cv2.imread(path)
    img_corner = get4corner(img)
    val = []
    print(len(logos))
    for logo in logos:
        # compare_images(img_corner, logo)
        val.append(slide(img_corner, logo))
    print(val)
    winner = np.argmin(val)

    return logo_path[winner].split('/')[-1].split('.')[0]
