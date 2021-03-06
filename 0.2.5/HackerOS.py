import sys
import time
import random
import os
import logging
import playsound


#A function that does nothing(basicly)
def nothing():
	fsjifjomfl = "aiwkhiekf"
def Error(message = ""):
	if message == "":
		print("Error")
	else:
		print("Error: "+message)
	playsound.playsound("./SecretFiles/ErrorSound.mp3")
state=""

def math(num1, op, num2):
	try:
		if op == "+":
			return str(num1 + num2)
		elif op == "-":
			return str(num1 - num2)
		elif op == "*":
			return str(num1 * num2)
		elif op == "/":
			return str(num1 / num2)
		elif op == "%":
			return str(num1 % num2)
		elif op == "^":
			return str(num1 ^ num2)
		else:
			Error()
	except:
		Error()

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
	vars={}
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
	print("HackerOS ver. 0.2.4 started!")
	playsound.playsound("./SecretFiles/BootSound.mp3")
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
				print("\t\"run [program name]\" execute a HaxScript file")
				print("\t\"cmd [command]\" execute a command line command")
				print("\t\"setvar [name] [value]\" sets a variable to the value")
				print("\t\"getvar [name]\" returns the value of the variable at the index number")
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
					state="Script"
					os.system("python HackerOS.py "+command+".hax")
				except:
					print("An error occurred")
				state="OS"
			elif cmd.split(" ",1)[0] == "cmd":
				command = cmd.split(" ",1)[1]
				try:
					os.system(command)
				except:
					print("An error occurred")
			elif cmd.split(" ",2)[0] == "setvar":
				vars[cmd.split(" ",2)[1]] = cmd.split(" ",2)[2]
			elif cmd.split(" ",1)[0] == "getvar":
				print(vars[cmd.split(" ",2)[1]])
			elif cmd == "quit":
				sys.exit()
			elif cmd.split(" ")[0] == "math":
				try:
					num1=float(cmd.split(" ")[1])
				except:
					try:
						try:
							num1=float(vars[cmd.split(" ")[1]])
						except:
							Error
					except:
						Error("var does not exist")

				try:
					op = cmd.split(" ")[2]
				except:
					Error("second argument is not a math operation('+','-','x', '/', '^', or '%') or, it wasn't received.")

				try:
					num2=float(cmd.split(" ")[3])
				except:
					try:
						try:
							num1=float(vars[cmd.split(" ")[3]])
						except:
							Error()
					except:
						Error("var does not exist")
				print(math(num1, op, num2))
			elif cmd.split(" ", 1)[0] == "print":
				print(cmd.split(" ", 1)[1])
			else:
			    Error("Unknown command: "+cmd)
	else:
		input("Incorrect login info")
		sys.exit()


#The script portion of HackerOS

def runScript():
	vars={}
	condition = False
	return_value = ""
	script = open(sys.argv[1], "r").read().split("\n")
	for cmd in script:
		args = cmd.split(",")
		if list(cmd)[0] == "~":
			test = list(cmd)
			test.pop(0)
			cmd = ''.join(test)
			args = cmd.split(",")
			if condition == False:
				continue
		if list(cmd)[0] == "!":
			test = list(cmd)
			test.pop(0)
			cmd = ''.join(test)
			args = cmd.split(",")
			if condition == True:
				continue
		if list(cmd)[0] == "#":
			test = list(cmd)
			test.pop(0)
			cmd = ''.join(test)
			args = cmd.split(",")
			args[1] = return_value
		if list(cmd)[0] == ".":
			continue
		if args[0] == "print":
			print(args[1])
			return_value = args[1]
		elif args[0] == "pause":
			input()
			return_value = ""
		elif args[0] == "askvar":
			vars[args[1]] = input()
			return_value = vars[args[1]]
		elif args[0] == "printvar":
			print(vars[args[1]])
		elif args[0] == "math":
			try:
				num1=float(vars[args[1]])
			except:
				try:
					try:
						num1=float(args[1])
					except:
						Error()
				except:
					Error("var does not exist")

			try:
				op = args[2]
			except:
				Error("second argument is not a math operation('+','-','x', '/', or '%') or, it wasn't received.")

			try:
				num2=float(vars[args[3]])
			except:
				try:
					try:
						num2=float(args[3])
					except:
						Error()
				except:
					Error("var does not exist")
			return_value = math(num1, op, num2)
		elif cmd == "clear" or cmd == "cls":
			os.system("cls")
			return_value = ""
		elif args[0] == "if":
			if args[2] == "==":
				try:
					condition = vars[args[1]] == vars[args[3]]
					continue
				except:
					nothing()
				try:
					condition = vars[args[1]] == args[3]
					continue
				except:
					nothing()
				try:
					condition = args[1] == args[3]
					continue
				except:
					nothing()
			return_value = condition
		elif args[0] == "cmd":
			os.system(args[1])
			return_value = ""
		elif args[0] == "sleep":
			time.sleep(int(args[1]))
			return_value = ""
		elif args[0] == "setvar":
			try:
				vars[args[2]]=vars[args[1]]
			except:
				nothing()
			try:
				vars[args[2]]=args[1]
			except:
				nothing()
			return_value = vars[args[1]]
		elif cmd == "quit":
			sys.exit()
		elif cmd == "":
			nothing()
		else:
			Error("Unknown command: "+args[0])
			input()
			break
try:
	sys.argv[1]
except:
	state="OS"
	runOS()
if sys.argv[1]:
	state="Script"
	runScript()