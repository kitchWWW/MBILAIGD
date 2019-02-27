import shutil
import random
import os
import json

timestamp = "12345"
notestype = "5_41"
timetype = "100_700"


os.mkdir("out/"+timestamp)

#find the appropreate time marks
fd = open("time/"+timetype+".txt")
marks = []
for l in fd.readlines():
	marks.append(json.loads(l))
fd.close()
marks= marks[0]
timeOptions = range(5,545) #five seconds of silence, then 9 min run time
opts = []
for i in range(len(marks)):
	opts.append(marks[i][1])
print opts
timeOptions = opts

outfd = open("out/"+timestamp+"/timemark.txt",'w')
outfd.write(json.dumps(timeOptions))
outfd.truncate()
outfd.close()



possible = os.listdir("notes/"+notestype+"/")
chosenNotes = random.choice(possible)
shutil.copyfile("notes/"+notestype+"/"+chosenNotes, "out/"+timestamp+"/notes.txt")



