#script (python)
import clingo
import time as ts
import os


model_num = -1
timestamp = -1

def output(solution):
	global timestamp
	global model_num
	if timestamp == -1:
		timestamp = str(ts.time())
		os.mkdir('out/'+timestamp)
	model_num += 1
	print("hi")
	totalTime = 0;
	totalVoices = 0;
	atoms = solution.symbols(atoms=True)
	for a in atoms:
		if a.name == 'instruction':
			if a.arguments[1].number > totalVoices:
				totalVoices = a.arguments[1].number
			if a.arguments[2].number+1 > totalTime:
				totalTime = a.arguments[2].number+1
	res = [0]*totalVoices
	for i in range(totalVoices):
		res[i] = [0]*totalTime
	for a in atoms:
		if a.name == 'instruction':
			pitch = int(a.arguments[0].number)
			voice = a.arguments[1].number -1
			time = a.arguments[2].number
			res[voice][time] = pitch
	print "*********************"
	for i in range(len(res[0])):
		toprint = []
		for p in range(len(res)):
			toprint.append(str(res[p][i]))
		print "\t".join(toprint)

	print "*********************"
	lilyStrings = convertVoicesToLily(res)
	outputLilyStrings(lilyStrings,model_num)
	print("bye")
 
def main(prg):
    prg.ground([("base", [])])
    prg.solve()
    solution = prg.solve(on_model=output)

def lilyPitchFromString(p):
	if p == 0:
		return "r"
	p = p-10
	return ["f","a","c'","e'","g'"][p]

def outputLilyStrings(lilyStrings,model_num):
	print lilyStrings
	print timestamp
	orig = open("Score.ly",'r')
	fd = open('out/'+timestamp+'/out_'+str(model_num)+'.ly','w')
	partCount = 0
	for l in orig.readlines():
		if "%part" in l:
			l = " ".join(lilyStrings[1-partCount])+"\n"
			partCount+=1
		fd.write(l)
	fd.truncate()
	fd.close()
	os.chdir('out/'+timestamp)
	os.system("lilypond out_"+str(model_num)+" > /dev/null 2>&1  & ")
	os.chdir("../../")


def convertVoicesToLily(voices):
	ret = []
	for v in range(len(voices)):
		lyString = []
		for p in range(len(voices[v])):
			if p > 0:
				# if we have two rests in a row and change in the electronics, then pass
				if voices[0][p] == voices[0][p-1] and voices[1][p] == voices[1][p-1] and voices[0][p] == 0 and voices[1][p] == 0 :
					continue
			# tie from prev note if continuation.
			if p > 0 and voices[v][p]!=0:
				if voices[v][p-1] != 0:
					lyString.append("~")
			lyString.append(lilyPitchFromString(voices[v][p])+"1:32")
			needBang = False
			if p > 0 and p < len(voices[v])-1 and voices[v][p]!=0:
				if voices[v][p-1] == 0 and voices[v][p+1] == 0:
					pass
				elif voices[v][p-1] == 0:
					lyString.append("\\<")
					needBang = True
				elif voices[v][p+1] == 0:
					lyString.append("\\>")
					needBang = True
			if voices[v][p] != 0:
				lyString.append("~")
				lyString.append(lilyPitchFromString(voices[v][p])+"1:32")
				if needBang:
					lyString.append("\\!")
		ret.append(lyString)
	return ret

#end.