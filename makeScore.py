import json
import random
import os

def lilyPitchFromString(p):
	if p == 0:
		return "r"
	p = p-10
	return ["f","a","c'","e'","g'"][p]

def outputLilyStrings(lilyStrings,timestamp,dedication):
	print lilyStrings
	print timestamp
	orig = open("Score.ly",'r')
	fd = open('out/'+timestamp+'/out.ly','w')
	partCount = 0
	for l in orig.readlines():
		if "%name" in l:
			l = "generated for "+dedication
		if "%part" in l:
			l = " ".join(lilyStrings[1-partCount])+"\n"
			partCount+=1
		fd.write(l)
	fd.truncate()
	fd.close()
	os.chdir('out/'+timestamp)
	os.system("lilypond out.ly > /dev/null 2>&1  & ")
	os.chdir("../../")


def isDeleteable(voices,v,p):
	if p == 0 or p ==len(voices[v])-1:
		return False
	if voices[v][p] == 0:
		return True
	if voices[v][p] == voices[v][p-1]  and voices[v][p]== voices[v][p+1]:
		return True
	return False


def formatForTime(sec):
	secString = str(sec%60)
	if len(secString) == 1:
		secString = "0"+secString
	return str(sec/60)+":"+secString

def convertVoicesToLily(voices,timestamp):
	ret = []
	trem = ":32"
	
	fd = open("out/"+timestamp+"/timemark.txt")
	timeOptions = json.loads(fd.readlines()[0])
	fd.close()

	timeMarks = [formatForTime(x) for x in timeOptions]


	print timeMarks
	for v in range(len(voices)):
		lyString = []
		for p in range(len(voices[v])):
			# if it is a rest or the same on both sides, we can skip the whole chunk
			if isDeleteable(voices,0,p) and isDeleteable(voices,1,p):
			 	continue
			# tie from prev note if continuation.
			if p > 0 and voices[v][p]!=0:
				if voices[v][p-1] != 0:
					lyString.append("~")
			if voices[v][p] == 0:
				trem = ""
			else:
				trem = ":32"
			timeFormat = timeMarks[2*p] #str(p)+":["+str(voices[0][p])+","+str(voices[1][p])+"]"
			if v == 0:
				timeFormat = ""
			lyString.append(lilyPitchFromString(voices[v][p])+"1"+trem+" "+'^"{}"'.format(timeFormat))
			
			timeFormat = timeMarks[(2*p)+1]
			if v == 0:
				timeFormat = ""

			needsSecond = True
			if voices[0][p] == 0 and voices[1][p] ==0:
				needsSecond = False
			if needsSecond:
				needBang = False
				printRest = False
				if p > 0 and p < len(voices[v])-1 and voices[v][p]!=0:
					if voices[v][p-1] == 0 and voices[v][p+1] == 0:
						pass
					elif voices[v][p-1] == 0:
						lyString.append("\\<")
						needBang = True
					elif voices[v][p+1] == 0:
						lyString.append("\\>")
						needBang = True
						printRest = True
				if printRest:
					lyString.append(lilyPitchFromString(0)+"1"  +'^"{}"'.format(timeFormat))
				else:
					if voices[v][p] != 0:
						lyString.append("~")
		
					lyString.append(lilyPitchFromString(voices[v][p])+"1"+trem +'^"{}"'.format(timeFormat))
				if needBang:
					lyString.append("\\!")
		ret.append(lyString)
	return ret


timestamp = "12345"
dedication = ""
infd = open("out/"+timestamp+"/notes.txt",'r')
res = json.loads(infd.readlines()[0])
lilyStrings = convertVoicesToLily(res,timestamp)
outputLilyStrings(lilyStrings,timestamp,dedication)




