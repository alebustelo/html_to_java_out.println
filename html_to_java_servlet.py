#05/10/2017
#python 3
import os

def main():

	print('Enter the filename of the html file to process:')
	fileName = input()
	outputFile = open(fileName+'_java.txt', 'w')
	tempLine = ''
	firstLine = True

	with open(fileName) as f:
		lines = f.readlines()
		last = lines[-1]
		for line in lines[:-1]:
			tempLine = line.rstrip()
			tempLine.replace('"', r'\"')
			if firstLine:
				tempLine = 'out.println("' + tempLine + '"\n'
				firstLine = False
			else:
				tempLine = '\t+ "' + tempLine + '"\n'
			outputFile.write(tempLine)
		tempLine = '\t+ "' + last.rstrip() + '");'
		outputFile.write(tempLine)
		
main()