import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import random
import json

def genSinWave(dur,freq):
	duration = float(dur)   # in seconds, may be float
	f = float(freq)        # sine frequency, Hz, may be float
	samples = ( np.sin(2*np.pi*np.arange(fs*duration)*f/fs) ).astype(np.float32)
	return samples

def genWaveEnvelope(fadeIn,sustain,fadeOut):
	fadeIn = np.arange(float(fadeIn) * fs) / (fs *fadeIn)
	sustain = np.ones(sustain* fs)
	fadeOut = np.arange(float(fadeOut) * fs,0,-1) / (fs * fadeOut)
	p1 = np.append(fadeIn,sustain)
	p2 = np.append(p1,fadeOut)
	return p2

def addToTotal(waveData,startPoint):
	global totalRes
	emptyBefore = np.zeros(startPoint * fs)
	emptyAfter = np.zeros(((totalDuration - startPoint) * fs) - len(waveData))
	addLayer = np.append(emptyBefore,waveData)
	addLayer = np.append(addLayer,emptyAfter)
	totalRes = np.add(totalRes,addLayer)

def genWave(freq,sustainVolume,fadeIn,sustain,fadeOut):
	return np.multiply(genSinWave(fadeIn+sustain+fadeOut,freq),genWaveEnvelope(fadeIn,sustain,fadeOut)) * float(sustainVolume)

def st(steps):
	return 2.0**(steps/12.0)

def notch(delay,sustainVolume, fadeOutTime,sustainTime,fadeInTime):
	global totalRes
	emptyBefore = np.ones(delay * fs)
	fadeOut = (np.arange(float(fadeOutTime) * fs,0,-1) / (fs * fadeOutTime) * float(1.0 - sustainVolume)) + sustainVolume
	sustain = np.ones(sustainTime* fs) * sustainVolume
	fadeIn = (np.arange(float(fadeInTime) * fs) / (fs *fadeInTime) * float(1.0 - sustainVolume)) + sustainVolume
	leftOverDurration = totalDuration - (delay + fadeOutTime + sustainTime + fadeInTime)
	emptyAfter = np.ones(leftOverDurration* fs)

	p1 = np.append(emptyBefore,fadeOut)
	p2 = np.append(p1,sustain)
	p3 = np.append(p2,fadeIn)
	p4 = np.append(p3,emptyAfter)
	totalRes = np.multiply(p4,totalRes)



timestamp = "12345"
fd = open("out/"+timestamp+"/notes.txt")
directions = json.loads(fd.readlines()[0])[2]
fd.close()

fd = open("out/"+timestamp+"/timemark.txt")
timeMarks = json.loads(fd.readlines()[0])

freqF = 87.307 # F.

fs = 44100       # sampling rate, Hz, must be integer
totalDuration = timeMarks[len(directions)*2+1]+5 # in seconds
totalRes = np.zeros(fs*totalDuration)



for i in range(len(directions)):
	fadeInTime = timeMarks[2*i+1] - timeMarks[2*i]
	sustainTime = timeMarks[2*i+2] - timeMarks[2*i+1]
	fadeOutTime = timeMarks[2*i+3] - timeMarks[2*i+2]
	startTime = timeMarks[2*i]
	style = directions[i]

	print i, timeMarks[2*i], timeMarks[2*i+1],timeMarks[2*i+2],timeMarks[2*i+3]
	print i, fadeInTime, sustainTime,fadeOutTime, startTime
	if style >0:
		style = style - 9
	print style
	for i in range(style+1):
		ip = i+1
		addToTotal(genWave(freqF*ip,.5*(1.0/(ip)),fadeInTime,sustainTime,fadeOutTime),startTime)

# notch(90,.2,30,30,30)



plt.plot(totalRes)
plt.savefig("out/"+timestamp+"/fig.png")

scaled = np.int16(totalRes/np.max(np.abs(totalRes)) * 32767)

write('out/'+timestamp+'/test.wav', 44100, scaled)
