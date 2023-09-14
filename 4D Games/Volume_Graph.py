
# https://colab.research.google.com/drive/1-Ilo-MFRbiCxiQEgAIcaU8TjvpHmMx-J#scrollTo=c0Mekc6Jw3ir

import librosa, winsound
import matplotlib.pylab as plt

def save_plot(filename):
    y, sr = librosa.load(filename)        
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(y)
    plt.savefig('output/Dior.png')
    return y, sr

y, sr = save_plot('input/Dior.mp3')
# https://youtu.be/S0nOYs0PRak

with open('output/Dior.txt', 'w') as f:
    for i, j in enumerate(y[::sr]):
        # try:
        #     duration = 1000 # 1 sec
        #     frequency = int(10000*j)

        #     winsound.Beep(frequency, duration)
        #     print(i, 10000*j)

        # except:
        #     pass
        f.write(f'{j}, ')

print(y[::sr], len(y)/sr, 'seconds')
# ValueError: frequency must be in 37 thru 32767

# The variable sr contains the sampling rate of y , 
# that is, the number of samples per second of audio.
