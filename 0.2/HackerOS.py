import sys
import time
import random
import os
import keyboard
import logging


#A function that does nothing(basicly)
def nothing():
	fsjifjomfl = "aiwkhiekf"

def math(num1, op, num2):
	try:
		if op == "+":
			print(num1 + num2)

		elif op == "-":
			print(num1 - num2)

		elif op == "*":
			print(num1 * num2)

		elif op == "/":
			print(num1 / num2)

		elif op == "%":
			print(num1 % num2)
		elif op == "^":
			print(num1 ^ num2)

		else:
			print("Error")
	except:
		print("Error")

#Logging
try:
	if sys.argv[2] == '1':
		open("test.log", "w").write("")
		logging.basicConfig(level=logging.INFO, format='%(message)s')
		logger = logging.getLogger()
		logger.addHandler(logging.FileHandler('test.log', 'a'))
		print = logger.info
except:
	nothing()

#Normal HackerOS
def runOS():
	username=input("Username: ")
	password=input("Password: ")
	print("Logging in...")

	print("Configuring databases...")
	vars=[]
	for n in range(len(vars), 20):
		vars.append("")
	usernames = ["Jeff99","xX_Henry_Xx","Bob123","C00lK1d"]
	passwords = ["Password123","qwerty","123456"]
	time.sleep(random.randint(1,5)/10)
	print("Connecting to internet...")
	time.sleep(random.randint(1,5)/10)
	print("Downloading temporary hacker files...")
	time.sleep(random.randint(1,5)/10)
	print("Setting up secret stuff...")
	time.sleep(3)
	os.system('cls')
	print("HackerOS ver. 0.2 started")
	print("type \"help\" for commands")
	info = "No info yet"
	if True:
		while True:
			cmd=""
			cmd=input("HackerOS/"+username+"> ")
			if cmd == "help":
				print("\n\t\"hack\" start cool hacking stuff")
				print("\t\"hackerpad\" open up HackerPad™, makes a file in ./TextFiles/")
				print("\t\"hackerchat\" open up HackerChat™")
				print("\t\"cls\" or \"clear\" clear screen")
				print("\t\"quit\" exit HackerOS")
				print("\t\"run [file/program]\" execute/open a program/file")
				print("\t\"cmd [command]\" execute a command line command")
				print("\t\"setvar [1-20] [value]\" sets a variable to the value")
				print("\t\"getvar [1-20]\" returns the value of the variable at the index number")
				print("\t\"math [number 1] [operation (+,-,x,/,%)] [number 2]\" runs a math operation with 2 numbers")

				print()
			elif cmd == "hack":
				ip = input("IP: ")
				print("Staring hack...")
				time.sleep(random.randint(1,5)/2)
				print("Acessing "+ip)
				time.sleep(random.randint(1,5)/2)
				print("Getting login info...")
				time.sleep(random.randint(1,5)/2)
				print("Done!")
				print("Type \"info\" to get the info.")
				info = "Username: "+usernames[random.randint(0,3)]+"\nPassword: "+passwords[random.randint(0,2)]
			elif cmd == "hackerpad":
				file = input("File: ")
				time.sleep(1)
				os.system("start notepad TextFiles/"+file)
			elif cmd == "info":
				print(info)
			elif cmd == "hackerchat":
				print("Starting HackerChat™...")
				time.sleep(1)
				os.system("start ./SecretFiles/chat.html")
			elif cmd == "":
				print()
			elif cmd == "clear" or cmd == "cls":
				os.system("cls")
			elif cmd.split(" ",1)[0] == "run":
				command = cmd.split(" ",1)[1]
				try:
					os.system("start "+command)
				except:
					print("An error occurred")
			elif cmd.split(" ",1)[0] == "cmd":
				command = cmd.split(" ",1)[1]
				try:
					os.system(command)
				except:
					print("An error occurred")
			elif cmd.split(" ",2)[0] == "setvar":
				if int(cmd.split(" ",2)[1]) <= 20 and int(cmd.split(" ",2)[1]) > 0:
					try:
						vars.insert(int(cmd.split(" ",2)[1]), cmd.split(" ",2)[2])
					except:
						print("Error")
				else:
					print("Number Overflow Error")
			elif cmd.split(" ",1)[0] == "getvar":
				if int(cmd.split(" ",2)[1]) <= 20 and int(cmd.split(" ",2)[1]) > 0:
					try:
						print(vars[int(cmd.split(" ",1)[1])])
					except:
						print("Error")
				else:
					print("Number Overflow Error")
			elif cmd == "quit":
				sys.exit()
			elif cmd.split(" ")[0] == "math":
				try:
					num1=float(cmd.split(" ")[1])
				except:
					print("Error: first argument is not an float or, it wasn't received.")

				try:
					op = cmd.split(" ")[2]
				except:
					print("Error: second argument is not a math operation('+','-','x', '/', '^', or '%') or, it wasn't received.")

				try:
					num2=float(cmd.split(" ")[3])
				except:
					print("Error: third argument is not an float or, it wasn't received.")
				math(num1, op, num2)
			else:
			    print("Unknown command: "+cmd)
	else:
		input("Incorrect login info")
		sys.exit()


#The script portion of HackerOS

def runScript():
	vars=[]
	condition = False
	for n in range(len(vars), 20):
		vars.append("")
	script = open(sys.argv[1], "r").read().split("\n")
	for cmd in script:
		if list(cmd)[0] == "~":
			test = list(cmd)
			test.pop(0)
			cmd = ''.join(test)
			if condition == False:
				continue
		if cmd.split(" ", 1)[0] == "print":
			print(cmd.split(" ", 1)[-1])
		elif cmd.split(" ", 1)[0] == "pause":
			input()
		elif cmd.split(" ", 1)[0] == "askvar":
			vars[int(cmd.split(" ", 1)[1])] = input()
		elif cmd.split(" ", 1)[0] == "printvar":
			print(vars[int(cmd.split(" ", 1)[1])])
		elif cmd.split(" ")[0] == "math":
			try:
				num1=float(cmd.split(" ")[1])
			except:
				print("Error: first argument is not an float or, it wasn't received.")

			try:
				op = cmd.split(" ")[2]
			except:
				print("Error: second argument is not a math operation('+','-','x', '/', or '%') or, it wasn't received.")

			try:
				num2=float(cmd.split(" ")[3])
			except:
				print("Error: third argument is not an float or, it wasn't received.")
			math(num1, op, num2)
		elif cmd == "clear" or cmd == "cls":
			os.system("cls")
		elif cmd.split(" " , 3)[0] == "if":
			if cmd.split(" " , 3)[2] == "==":
				if vars[int(cmd.split(" " , 3)[1])] == cmd.split(" " , 3)[3]:
					condition = True
				else:
					condition = False
			if cmd.split(" " , 3)[2] == "!=":
				if vars[int(cmd.split(" " , 3)[1])] != cmd.split(" " , 3)[3]:
					condition = True
				else:
					condition = False
		elif cmd.split(" ", 1)[0] == "cmd":
			os.system(cmd.split(" ", 1)[1])
		elif cmd.split(" ")[0] == "sleep":
			time.sleep(int(cmd.split(" ")[1]))
		elif cmd == "quit":
			sys.exit()
		elif cmd == "":
			nothing()
		else:
			print("Error: Unknown command: "+cmd.split(" ", 1)[0])
			input()
			break
try:
	sys.argv[1]
except:
	runOS()
if sys.argv[1]:
		runScript()