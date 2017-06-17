#!/usr/bin/env python2.7

import os,sys

def processFile(szFile): 
	#here we split the name of the file say importPlanner.csv into lstFile[0] = importPlanner lstFile[1] = csv
	#we can then append the file name importPlannerClean

	#open the file
	fo = open(szFile,"r")
	lstInput = []

	#iterates and reads the text file

	for oLine in fo:
		try:
			lstLine = oLine.replace("\n","").split("\t")

		except Exception as e:
			print e
			pass

		lstInput.append(lstLine)

	fo.close()

	fw = open("data.csv","w") 

	for oLine in lstInput:
		szWriteLine = ",".join(oLine)
		fw.write(szWriteLine+"\n")

	fw.close()


processFile("data.txt")