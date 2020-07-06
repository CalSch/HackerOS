

import sys
import time
import random
import os
import keyboard

usernames = ["Jeff99","xX_Henry_Xx","Bob123","C00lK1d"]
passwords = ["Password123","qwerty","123456"]
vars=[]
for n in range(len(vars), 20):
    vars.append("")



username=input("Username: ")
password=input("Password: ")
print("Logging in...")

print("Configuring databases...")
time.sleep(random.randint(1,5)/10)
print("Connecting to internet...")
time.sleep(random.randint(1,5)/10)
print("Downloading temporary hacker files...")
time.sleep(random.randint(1,5)/10)
print("Setting up secret stuff...")
time.sleep(3)
os.system('cls')
print("HackerOS ver. 0.1.9 started")
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
	    	prefs = open("./SecretFiles/prefs.dat", "w+")
	    	prefs.write(color)
	    	sys.exit()

	    else:
	        print("Unknown command: "+cmd)
else:
	input("Incorrect login info")
	sys.exit()