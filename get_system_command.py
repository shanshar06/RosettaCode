from subprocess import call
import os
import sys

#subprocess.check_output(arg, *, .... )
#returns output of command executed

output_text = call.check_output("ls", shell=True, universal_newlines=True)

def write(output_text):
	name = 'new.txt'

	try:
		file = open(name, 'r+')
		file.close()
		file = open(name, 'w+')
		file.write(output_text)
		file.close()

	except:	
		sys.exit(0)

write(output_text)
