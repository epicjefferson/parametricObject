from pylab import*
from scipy.io import wavfile

thickness = 160

sampFreq, snd = wavfile.read('440_sine.wav')
snd = abs((snd / (2.**15)*thikness))
s1 = snd[:,0]
levels = []
points = 40

step = 5060/40
avg = 0

for i in xrange(len(s1)/step):
    avg = 0
    begin = i * step
    end = ((i + 1) * step - 1)
    temp = s1[ begin : end]

    for j in xrange(len(temp)):
        avg += temp[j]
    avg = avg/len(temp)
    levels.append(avg)

file = open("sample.txt", "w")
for i in xrange(len(levels)):
    file.write(str(levels[i]))
    file.write('\n')
file.close()


