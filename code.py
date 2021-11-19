import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

y, sr = librosa.load('xavi.wav', offset=360, duration=60)
# y, sr = librosa.load('piano_c4.wav')

D = librosa.stft(y)
# S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

img = librosa.display.specshow(np.abs(D), x_axis='time', y_axis='fft_note')
plt.colorbar(img, format="%+2.f dB")
plt.show()