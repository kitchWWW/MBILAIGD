#script (python)
import clingo
import os
import random
import json

model_num = -1
timestamp = "12345"

def output(solution):
	global timestamp
	global model_num
	if model_num == -1:
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
	outfd = open("out/"+timestamp+"/notes_"+str(model_num)+".txt",'w')
	outfd.write(json.dumps(res))
	outfd.close()
	# lilyStrings = convertVoicesToLily(res)
	# outputLilyStrings(lilyStrings,model_num)
	# print("bye")
 
def main(prg):
    prg.ground([("base", [])])
    prg.solve()
    solution = prg.solve(on_model=output)

#end.