import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
import librosa
import os



df = pd.read_csv('data2.csv')
df.drop(df.columns[0], inplace=True, axis=1)
y1=df['mfcc2_mean'][0:252]
x1=df['mfcc1_mean'][0:252]
y2=df['mfcc2_mean'][252:506]
x2=df['mfcc1_mean'][252:506]
y3=df['mfcc2_mean'][506:733]
x3=df['mfcc1_mean'][506:733]
y4=df['mfcc2_mean'][733:790]
x4=df['mfcc1_mean'][733:790]
# x = df.loc[:, df.columns != 'result']

def visual(audio):
    y, s = librosa.load(audio)
    audio, _ = librosa.effects.trim(y,top_db=30)

    mfcc = librosa.feature.mfcc(y=audio, sr=s,n_fft=1024)
    x=mfcc[0].mean()
    y=mfcc[1].mean()
    plt.scatter(x1,y1,label='Adham')
    plt.scatter(x2,y2,label='Ahmed')
    plt.scatter(x3,y3,label='Maha')
    plt.scatter(x4,y4,label='Mohmoud')
    plt.scatter(x,y,label='audio')
    plt.legend()
    plt.savefig("static/assets/Feature_visuals.png")


