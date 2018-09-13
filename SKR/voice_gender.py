import os
import pickle
import numpy as np
from scipy.io.wavfile import read
import soundfile as sf
import python_speech_features as mfcc
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
from SKR import audiotranscode

def get_MFCC(sr,audio):
    features = mfcc.mfcc(audio,sr, 0.025, 0.01, 13,appendEnergy = False)
    feat     = np.asarray(())
    for i in range(features.shape[0]):
        temp = features[i,:]
        if np.isnan(np.min(temp)):
            continue
        else:
            if feat.size == 0:
                feat = temp
            else:
                feat = np.vstack((feat, temp))
    features = feat;
    features = preprocessing.scale(features)
    return features

def get_gender(path):
    # path to saved models
    modelpath = "SKR/data/gender/"

    gmm_files = [os.path.join(modelpath, fname) for fname in
                 os.listdir(modelpath) if fname.endswith('.gmm')]
    models = [pickle.load(open(fname, 'rb')) for fname in gmm_files]
    genders = [fname.split("/")[-1].split(".gmm")[0] for fname
               in gmm_files]


    audio, sr = sf.read(path)
    features = get_MFCC(sr, audio)
    scores = None
    log_likelihood = np.zeros(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(features))
        log_likelihood[i] = scores.sum()
    winner = np.argmax(log_likelihood)


    return genders[winner].split("_")[0]