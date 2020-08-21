print("Configuring data")

import sys
import os

try:
	file = open(sys.argv[1], "r")
except:
	print("No file specified")
	input()
	sys.exit()
if sys.argv[1].split(".")[-1] != "hax":
	print("File is not a HaxScript")
	input()
	sys.exit()
NewScript = ["# This is a compiled HaxScript", "import sys", "import os", "import time", ""]
lines = file.read().split("\n")
file.close()
vars = []

print("Compiling")
for cmd in lines:
	thing = False
	cmd = cmd.replace("\"", "\\\"")
	cmd = cmd.replace("condition", "condition2")
	cmd = cmd.replace("return_val", "return_val2")
	if list(cmd)[0] == '~':
		test=list(cmd)
		test.pop(0)
		cmd = "".join(test)
		NewScript.append("if condition == True:")
		thing = True
	if list(cmd)[0] == '!':
		test=list(cmd)
		test.pop(0)
		cmd = "".join(test)
		NewScript.append("if condition == False:")
		thing = True
	if list(cmd)[0] == '#':
		test=list(cmd)
		test.pop(0)
		cmd = "".join(test)
		stuff = cmd.split(",")
		stuff[1] = "return_val"
		vars.append("return_val")
		cmd = ",".join(stuff)
	args = cmd.split(",")
	print(args)
	if args[0] == 'print':
		print('print')
		var1 = False
		for var in vars:
			if args[1] == var:
				var1 = True
		if thing:
			if var1:
				NewScript.append("\tprint("+args[1]+")")
			else:
				NewScript.append("\tprint(\""+args[1]+"\")")
			continue
		if var1:
			NewScript.append("print("+args[1]+")")
		else:
			NewScript.append("print(\""+args[1]+"\")")
	elif args[0] == 'pause':
		print('pause')
		if thing:
			NewScript.append("\tinput()")
			continue
		NewScript.append("input()")
	elif args[0] == 'askvar':
		print('askvar')
		vars.append(args[1])
		if thing:
			NewScript.append("\t"+args[1]+" = input()")
			continue
		NewScript.append(args[1]+" = input()")
		NewScript.append("return_val = "+args[1])
	elif args[0] == 'printvar':
		print('printvar')
		if thing:
			NewScript.append("\tprint("+args[1]+")")
			continue
		NewScript.append("print("+args[1]+")")
	elif args[0] == 'math':
		if thing:
			NewScript.append("\tfloat("+args[1]+")"+args[2]+"float("+args[3]+"))")
			continue
		NewScript.append("float("+args[1]+")"+args[2]+"float("+args[3]+")")
		NewScript.append("return_val = str(float("+args[1]+")"+args[2]+"float("+args[3]+"))")
	elif args[0] == 'cls' or args[0] == 'clear':
		print('cls/clear')
		if thing:
			NewScript.append("\tos.system(\"cls\")")
			continue
		NewScript.append("os.system(\"cls\")")
	elif args[0] == 'cmd':
		print('cmd')
		if thing:
			NewScript.append("\tos.system(\""+args[1]+"\")")
			continue
		NewScript.append("os.system(\""+args[1]+"\")")
	elif args[0] == 'sleep':
		print('sleep')
		if thing:
			NewScript.append("\ttime.sleep("+args[1]+")")
			continue
		NewScript.append("time.sleep("+args[1]+")")
	elif args[0] == 'quit':
		print('quit')
		if thing:
			NewScript.append("\tsys.exit()")
			continue
		NewScript.append("sys.exit()")
	elif args[0] == 'setvar':
		print('setvar')
		vars.append(args[2])
		if thing:
			NewScript.append("\t"+args[2]+" = "+args[1])
		NewScript.append(args[2]+" = "+args[1])
	elif args[0] == 'if':
		print("There was an if!")
		var1 = False
		var2 = False
		for var in vars:
			if args[1] == var:
				var1 = True
			if args[3] == var:
				var2 = True
		NewScript.append("condition = False")
		if var1 and var2:
			NewScript.append("if "+args[1]+args[2]+args[3]+":")
		elif var1:
			NewScript.append("if "+args[1]+args[2]+"\""+args[3]+"\""+":")
		elif var2:
			NewScript.append("if "+"\""+args[1]+"\""+args[2]+args[3]+":")
		else:
			NewScript.append("if "+"\""+args[1]+"\""+args[2]+"\""+args[3]+"\""+":")
		NewScript.append("\tcondition = True")
	elif args[0] == '':
		print("Nothing")
		NewScript.append("")
	else:
		print("Error")
		input()
		sys.exit()
print("Done!")
f = input("New file name: ")+".py"
newFile = open(f, "w")
newFile.write("\n".join(NewScript))
newFile.close()
if input("Run file?\n(Y/n): ") == "n":
	print()
else:
	os.system("python "+f)
input()