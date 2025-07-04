import librosa
 
 → port numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load("audio.wav", sr=16000)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

print("MFCC shape:", mfcc.shape)
plt.imshow(mfcc, cmap='hot', interpolation='nearest')
plt.title("MFCC")
plt.show()
