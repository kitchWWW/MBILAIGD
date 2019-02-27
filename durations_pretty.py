#script (python)
import clingo
import os
import random
import json

model_num = -1

def output(solution):
	global model_num
	model_num += 1
	totalTime = 0;
	totalVoices = 0;
	atoms = solution.symbols(atoms=True)
	timeMarks = []
	for a in atoms:
		if a.name == 'timeMark':
			timeMarks.append([int(a.arguments[1].number), int(a.arguments[0].number)])
	print timeMarks
	outfd = open("timemarks.txt",'a+')
	outfd.write(json.dumps(timeMarks)+'\n')
	outfd.close()

 
def main(prg):
    prg.ground([("base", [])])
    prg.solve()
    solution = prg.solve(on_model=output)


#end.