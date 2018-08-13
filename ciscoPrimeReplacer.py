import os
import time
from time import strftime
import sys
sys.path.insert(0, 'sshTest')
import exportConfgNew
import fileinput
import getpass
import pushTemplateNew
import help
import threading

devices={}
ipAddresses={}
device_index={}
username=None
pswd=None
#Loads Dictionaries that are used to quickly reference the device directory
def loadDictionaries():
	#i is used as a local variable for device_index, which is important in multi-select functions
	i=1
	#checks to see if the device directory actually exists. If this moves need to change the path
	if os.path.isfile("sshTest/devices.txt"):
		#opens the device directory
		with open("sshTest/devices.txt", "r+") as f:
			while True:
				#reads a line that's "Hostname,IP"
				line=f.readline()
				#this checks to see if it is at the End of the File
				if not line: break
				#splits Hostname and IP into an array and adds them to each directory
				line=line.split(",")
				temp=line[1]
				line[1]=temp[:-1]
				devices[line[0]]=line[1]
				ipAddresses[line[1]]=line[0]
		#alphabetical order
		for device in devices:
			device_index[i]=device
			i=i+1
"""
ADD DEVICE MODULE
FUNCTION: MANUALLY ADD DEVICES TO THE DEVICE DIRECTORY
OPTIONAL ARGS: DEVICE, IP
"""

def addDevice(device=None, ip=None):
	#If hostname has not been specified by the command line it will prompt here
	if device==None:
		print "What is the device's hostname? ",
		device=raw_input()
	#While the user has not pressed enter. If the user presses enter it returns to the initial screen
	while device!="":
		devicel=device.lower() #lowercases device to prevent user error. If none of the cases match it will accept that it's the hostname
		#help commands below
		if devicel=="help":
			print help.getAddDeviceMain()+help.getAddDeviceDevice()+help.getCmdList()+help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
		elif devicel=="help ":
			print help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
		elif devicel=="help en" or devicel=="help ent" or devicel=="help ente" or devicel=="help enter":
			print help.getEnter1()
		elif devicel=="help e":
			print help.getEnter1()+help.getExit()
		elif devicel=="help ex" or devicel=="help exi" or devicel=="help exit":
			print help.getExit()
		elif devicel=="help q" or devicel=="help qu" or devicel=="help qui" or devicel=="help quit":
			print help.getQuit()
		elif devicel=="help c" or devicel=="help cl" or devicel=="help cle" or devicel=="help clea" or devicel=="help clear":
			print help.getClear()
		#System commands
		elif devicel=="clear":
			os.system("clear")
		elif devicel=="exit":
			return
		elif devicel=="quit":
			sys.exit()
		#checks to see if the device already exists in the device directories. If it does, prompt for another hostname
		elif device in devices:
			print "Hostname exists and has IP Address "+devices[device]
		else:
			#If IP has not been specified by the command line it will prompt here
			if ip==None:
				print "What is the device's IP Address? ",
				ip = raw_input()
			#while the user has not pressed enter. If the user presses enter it will prompt for device again
			while ip!="":
				ipl=ip.lower()
				#Help commands for addDevice IP below
				if ipl=="help":
					print help.getAddDeviceMain()+help.getAddDeviceIP()+help.getCmdList()+help.getClear()+help.getAddDeviceEnter2()+help.getAddDeviceDeviceName()+help.getExit()+help.getQuit()
				elif ipl=="help ":
					print help.getClear()+help.getAddDeviceEnter2()+help.getAddDeviceDeviceName()+help.getExit()+help.getQuit()
				elif ipl=="help c" or ipl=="help cl" or ipl=="help cle" or ipl=="help clea" or ipl=="help clear":
					print help.getClear()
				elif ipl=="help e": print help.getAddDeviceEnter2()+help.getExit()
				elif ipl=="help en" or ipl=="help ent" or ipl=="help ente" or ipl=="help enter": print help.getAddDeviceEnter2()
				elif ipl=="help ex" or ipl=="help exi" or ipl=="help exit": print help.getExit()
				elif ipl=="help d" or ipl=="help de" or ipl=="help dev" or ipl=="help devi" or ipl=="help devic" or ipl=="help device":
					print help.getAddDeviceDeviceName()
				elif ipl=="help q" or ipl=="help qu" or ipl=="help qui" or ipl=="help quit": print help.getQuit()
				elif ipl=="clear": os.system("clear")
				elif ipl=="device": print device
				elif ipl=="exit": return
				elif ipl=="quit": sys.exit()
				elif ip in ipAddresses: print "That IP Address already exists and is assigned to "+ipAddresses[ip] #checks if IP is already in device directory. If it is prompt again
				else:
					f=open("sshTest/devices.txt", "a+") #opens device directory in append mode. Path needs to be changed here if the location changes
					deviceInput = device+","+ip+"\n"    #adds the device by typing "Hostname,IP" and then a new line
					f.write(deviceInput)		    #writes the device to the file
					f.close()			    #closes the file
					devices[device]=ip		    #adds the device to the local dictionaries
				    
"""
LOOKUP DEVICE MODULE
FUNCTION: SEARCH FOR DEVICE IN DEVICE DIRECTORY
ARGUMENTS: hostnameOrIP
"""
def lookupDevice(hostnameOrIP=None):
	#if hostnameOrIP was not specified through command line, it will prompt here
	if hostnameOrIP==None:
		print "What is the hostname or ip address? ",
		hostnameOrIP=raw_input()
	#while the user has not pressed enter
	while hostnameOrIP!="":
		devicel=hostnameOrIP.lower() #lowercase the input to protect against user error
		#lookupDevice help commands below
		if devicel=="help":
			print help.getLookupDeviceMain()+help.getLookupDeviceSearch()+help.getCmdList()+help.getClear()+help.getLookupDeviceDevice()+help.getEnter1()+help.getExit()+help.getLookupDeviceIP()+help.getQuit()
		elif devicel=="help ":
			print help.getClear()+help.getLookupDeviceDevice()+help.getEnter1()+help.getExit()+help.getLookupDeviceIP()+help.getQuit()
		elif devicel=="help d" or devicel=="help de" or devicel=="help dev" or devicel=="help devi" or devicel=="help devic" or devicel=="help device" or devicel=="help devices": print help.getLookupDeviceDevice()
		elif devicel=="help e": print help.getEnter1()+help.getExit()
		elif devicel=="help en" or devicel=="help ent" or devicel=="help ente" or devicel=="help enter": print help.getEnter1()
		elif devicel=="help ex" or devicel=="help exi" or devicel=="help exit": print help.getExit()
		elif devicel=="help i" or devicel=="help ip": print help.getLookupDeviceIP()
		elif devicel=="help q" or devicel=="help qu" or devicel=="help qui" or devicel=="help quit": print help.getQuit()
		elif devicel=="help c" or devicel=="help cl" or devicel=="help cle" or devicel=="help clea" or devicel=="help clear":
			print help.getClear()
		#system commands below
		elif devicel=="clear":
			os.system("clear")
		elif devicel=="exit":
			return
		elif devicel=="quit":
			sys.exit()
		#entering ip will show the entire list of ipAddresses in the device directory. Looking at making this a paging system
		elif devicel=="ip":
			for ip in ipAddresses:
				print ip
		#entering devices will show the entire list of devices in the device directory. Looking at making this a paging system
		elif devicel=="devices":
			for dev in devices:
				print dev
		#if the hostnameOrIP exists print it with it's matching hostname/IP
		elif hostnameOrIP in devices or hostnameOrIP in ipAddresses:
			if hostnameOrIP in devices:
				print hostnameOrIP+" has IP Address "+devices[hostnameOrIP]
			else:
				print hostnameOrIP+" assigned to "+ipAddresses[hostnameOrIP]
			print "Change hostname and/or IP?(y/n) ", #prompt for changing the information. TO BE ADDED LATER
			change=raw_input()
			if change.lower()=='y': #Only succeeds if user types y
				print "Change hostname and ip to be added in Alpha 2.0"
		else:
			print "IP Address or hostname is not in use" #print that it's not in use if it's not in the device directory
		print "What is the hostname or ip address? ",
		hostnameOrIP=raw_input()

"""
ARCHIVE CONFG MODULE
FUNCTION: ARCHIVE RUNNING AND START CONFIGS AT A SELECTED TIME OR BY DEMAND
ARGUMENTS: hostnameOrIP
"""
def archiveConfg(ip=None):
	#if IPs or hostnames have been specified through command line just run this set of commands
	if ip!=None:
		username=raw_input("Username: ")    #prompts for username
		pswd=getpass.getpass('Password: ')  #prompts for password (will not show password in plaintext on screen)
		selectString=ip                     #stores the IPs in a string
		device_list=selectString.split(",") #splits that string by commas to see if there are multiple IPs or hostnames
		for selection in device_list:	    #cycles through
			if selection in ipAddresses:       #if the input is an IP address run this
				export=exportConfgNew.exportConfg(selection, username=username, password=pswd, pushOrPull=True, device=ipAddresses[selection]) #creates an exportConfg object located in SSHTest/exportConfgNew.py
				export.connect()    #uses the exportConfg function to connect to the IP
				export.mkdir()      #uses the exportConfg function to make the necessary directories
				export.export(False, False)       #exports the running and start configs to the directories. False, False means it's not an export run post applying template and it's not a failed apply
			elif selection in devices:         #if the input is a hostname run this
				export=exportConfgNew.exportConfg(devices[selection],username=username, password=pswd, pushOrPull=True, device=selection) #creates an exportConfg object located in SSHTest/exportConfgNew.py
				export.connect()    #uses the exportConfg function to connect to the IP
				export.mkdir()      #uses the exportConfg function to make the necessary directories
				export.export(False, False)       #exports the running and start configs to the directories. False, False means it's not an export run post applying template and it's not a failed apply
			else:
				print selection+" does not exist in the device directory" #If the hostname or IP is not in the device directory print that it's not
		return #exit the module
	#selected is a dictionary that's used for multi-selecting devices
	selected={}
	#used to prompt users on how they want to archive devices
	modeMessage= """
	1. Type devices to archive
	2. Select devices to archive
	3. Schedule an archive

Choose a archive mode: """
	print modeMessage,
	mode=raw_input()
	#while the user hasn't pressed enter to exit
	while mode!="":
		model=mode.lower() #lowercase the input to prevent error
		#help commands for mode select below
		if model=="help":
			print help.getArchiveConfgMain()+help.getArchiveConfgMode()+help.getCmdList()+help.getArchiveConfgMode1()+help.getArchiveConfgMode2()+help.getArchiveConfgMode3()+help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
		elif model=="help 1": print help.getArchiveConfgMode1()
		elif model=="help 2": print help.getArchiveConfgMode2()
		elif model=="help 3": print help.getArchiveConfgMode3()
		elif model=="help ":
			print help.getArchiveConfgMode1()+help.getArchiveConfgMode2()+help.getArchiveConfgMode3()+help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
		elif model=="help c" or model=="help cl" or model=="help cle" or model=="help clea" or model=="help clear":
			print help.getClear()
		elif model=="help e": print help.getEnter1()+help.getExit()
		elif model=="help en" or model=="help ent" or model=="help ente" or model=="help enter": print help.getEnter1()
		elif model=="help ex" or model=="help exi" or model=="help exit": print help.getExit()
		elif model=="help q" or model=="help qu" or model=="help qui" or model=="help quit": print help.getQuit()
		#system commands below
		elif model=="clear": os.system("clear")
		elif model=="exit": return
		elif model=="quit": sys.exit()
		elif mode=="1": #user chooses manual entries
			print "Type the hostname of the device and press enter to add it or type end to archive: ", #prompt for device names
			selectString=""
			device=raw_input()
			devicel=device.lower()
			#while the user hasn't entered to go back to the mode select screen
			while device!="":
				devicel=device.lower()
				#help commands for mode1 listed below
				if devicel=="help":
					print help.getArchiveConfgMain()+help.getArchiveConfgMode1Main()+help.getCmdList()+help.getClear()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getQuit()
				elif devicel=="help e": print help.getArchiveConfgMode1End()+help.getArchiveConfgMode1Enter()+help.getExit()
				elif devicel=="help en": print help.getArchiveConfgMode1End()+help.getArchiveConfgMode1Enter()
				elif devicel=="help end": print help.getArchiveConfgMode1End()
				elif devicel=="help ent" or devicel=="help ente" or devicel=="help enter": print help.getArchiveConfgMode1Enter()
				elif devicel=="help ex" or devicel=="help exi" or devicel=="help exit": print help.getExit()
				elif devicel=="help q" or devicel=="help qu" or devicel=="help qui" or devicel=="help quit": print help.getQuit()
				elif devicel=="help c" or devicel=="help cl" or devicel=="help cle" or devicel=="help clea" or devicel=="help clear":
					print help.getClear()
				#system command
				elif devicel=="clear":
					os.system("clear")
				elif devicel=="end": #once the user types end, run the archive process
					selectString=selectString[:-1] #takes out the last comma in the string
					device_list=selectString.split(",") #splits the devices into an array
					username=raw_input("Username: ") #prompts for username
					pswd=getpass.getpass('Password: ') #prompts for secure password
					for dev in device_list: #cycles through the array of input devices
						if dev in devices: #if the hostname is in the device directory
							export=exportConfgNew.exportConfg(devices[dev], username=username, password=pswd, pushOrPull=True, device=dev) #creates a new exportConfg object. Code located in sshTest/exportConfgNew.py
							export.connect() #uses the exportConfgNew function to connect to the device
							export.mkdir()   #makes the necessary directories
							export.export(False, False) #export the configs. False, False means not run after applying a template and it's not run after failing an apply
						else:
							print dev+" is not in the directory" #print that the device is not in the directory if it's not
					break
				#other system commands
				elif devicel=="exit":
					return
				elif devicel=="quit":
					sys.exit()
				else:
					selectString+=device+"," #add the device to the selected device string
				print selectString #show what devices the user has added
				device=raw_input("Type the hostname of the device and press enter to add it or type end to archive: ")
		elif mode=="2": #user chooses selection by list
			number= input("How many devices per page? ") #this will control how many devices are shown on each page
			selectString=""
			current=0
			selectionl=""
			#will cycle through until it has gone through every device or the user types end
			for i in range(1, len(devices)+number, number):
				for y in range(number): #prints the devices
					current=i+y
					print "%d. %s" % (i+y,device_index[current])
					if (y+i)==len(devices):
						break
				selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
				selectionl=selection.lower()
				#until the user types next or end
				while selectionl!="next":
					#help functions for archive Mode 2 below
					if selectionl=="help":
						print help.getArchiveConfgMain()+help.getArchiveConfgMode2Main()+help.getCmdList()+help.getClear()+help.getArchiveConfgMode2End()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getArchiveConfgMode2Num()+help.getQuit()
					elif selectionl=="help ":print help.getClear()+help.getArchiveConfgMode2End()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getArchiveConfgMode2Num()+help.getQuit()
					elif selectionl=="help c" or selectionl=="help cl" or selectionl=="help cle" or selectionl=="help clea" or selectionl=="help clear":
						print help.getClear()
					elif selectionl=="help e": print help.getArchiveConfgMode2End()+help.getArchiveConfgMode1Enter()+help.getExit()
					elif selectionl=="help en": print help.getArchiveConfgMode2End()+help.getArchiveConfgMode1Enter()
					elif selectionl=="help end":print help.getArchiveConfgMode2End()
					elif selectionl=="help ent" or selectionl=="help ente" or selectionl=="help enter": print help.getArchiveConfgMode1Enter()
					elif selectionl=="help ex" or selectionl=="help exi" or selectionl=="help exit": print help.getExit()
					elif selectionl=="help n": print help.getArchiveConfgMode2Next()+help.getArchiveConfgMode2Num() 
					elif selectionl=="help ne" or selectionl=="help nex" or selectionl=="help next": print help.getArchiveConfgMode2Next()
					elif selectionl=="help nu" or selectionl=="help num" or selectionl=="help numb" or selectionl=="help numbe" or selectionl=="help number": print help.getArchiveConfgMode2Num()
					elif selectionl=="help q" or selectionl=="help qu" or selectionl=="help qui" or selectionl=="help quit": print help.getQuit()
					#system commands below
					elif selectionl=="clear":
						os.system("clear")
						for y in range(number):
							current=i+y
							print "%d. %s" % (i+y, device_index[current])
							if (y+i)==len(devices):
								break
					elif selectionl=="exit":
						return
					#break if user types end
					elif selectionl=="end":
						break
					#system command
					elif selectionl=="quit":
						sys.exit()
					#return to the mode select prompt if user presses enter
					elif selectionl=="":
						break
					try: #trys to see if the input is an int
						if int(selection) in range(len(devices)+1): #if the selected int is in the range of devices add it to the selected string and print that it has been added
							selectString=selectString+device_index[int(selection)]+","
							print device_index[int(selection)]+" added"
						else:
							print "Incorrect Input" #print that the input is incorrect if it's not
					except ValueError: #if selection is not an int and isn't a system or help command,  print "Invalid input"
						print "Invalid input"
					#prompts at the end
					selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
					selectionl=selection.lower()
				if current==len(devices): break
				elif selectionl=="end" or selectionl=="": #break entirely if the user inputted either of these
					break
				os.system("clear") #clears the screen
				print "Selected: "+selectString
			if selectionl!="": #if it's not an enter proceed
				selectString=selectString[:-1] #gets rid of the last comma so it doesn't have errors
				selections=selectString.split(",") #splits the devices by commas
				username=raw_input("Username: ") #prompts for username
				pswd=getpass.getpass('Password: ') #prompts for password
				for selection in selections:     #for each inputted hostname
					if selection in devices: #if the hostname is in the device directory export the confgs
						export=exportConfgNew.exportConfg(devices[selection], username=username, password=pswd, pushOrPull=True, device=selection) #creates a new exportConfg object, located in sshTest/exportConfgNew.py
						export.connect() #connects to the device
						export.mkdir()   #makes the directories
						export.export(False, False)  #exports the configs
					else:
						print selection+" is not in the device directory" #print that it isn't in the device directory if it's not
		elif mode=="3": #if mode 3 is selected moved to the scheduling function
			scheduling()
			return
		else: #print that the input doesn't have a command mapped to it and prompt again
			print "Invalid input"
		print modeMessage,
		mode=raw_input()

"""
SCHEDULING MODULE
FUNCTION: HANDLES ALL SCHEDULING WORK
ARGS: TEMPLATES
"""

def scheduling(templates=None):
	#these booleans are used to allow for potential changes laater
	confirm=False
	dayConfirm=False
	monthConfirm=False
	hourConfirm=False
	minuteConfirm=False
	#dictionaries are used for rapid lookup later
	weekdays={
		0: "every Sunday",
		1: "every Monday",
		2: "every Tuesday",
		3: "every Wednesday",
		4: "every Thursday",
		5: "every Friday",
		6: "every Saturday"
	}
	months={
		1: "January",
		2: "February",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10: "October",
		11: "November",
		12: "December"
	}
	#-String is used for storing -Temp is used for presenting information
	dayTemp=""
	dayString=""
	monthTemp=""
	monthString=""
	hourTemp=""
	hourString=""
	minuteTemp=""
	minuteString=""
	temp="Current time settings: "
	#prompts to ask for type of scheduling. Days of the month will ask for 1-31, day of the week is every sunday, monday, etc.
	dayType=input("\n\t\t1. Day of the month\n\t\t2. Day of the week\n\nSchedule by(type number): ")
	#later the user will be asked to confirm that the time settings are correct. For now, it's set to false
	while not confirm:
		#if the user input day of the week
		if dayType==2:
			#after adding a day dayConfirm will be set to true
			while not dayConfirm:
				dayTemp=""
				dayString=""
				#prompts for the weekday
				weekday=raw_input("What day of the week('1'=Sunday, '7'=Saturday, 'all'=every weekday)? ")
				while weekday!="": #while it's not just an enter
					weekdayl=weekday.lower() #lowercase to prevent user error
					#help commands below
					if weekdayl=="help":
						print help.getSelectionWeekdayMain()+help.getCmdList()+help.getSelectionWeekdayAll()+help.getClear()+help.getExit()+help.getSelectionWeekdayNum()+help.getQuit()
					elif weekdayl=="help ":print help.getSelectionWeekdayAll()+help.getClear()+help.getExit()+help.getSelectionWeekdayNum()+help.getQuit()
					elif weekdayl=="help a" or weekdayl=="help al" or weekdayl=="help all": print help.getSelectionWeekdayAll()
					elif weekdayl=="help c" or weekdayl=="help cl" or weekdayl=="help cle" or weekdayl=="help clea" or weekdayl=="help clear":
						print help.getClear()
					elif weekdayl=="help e" or weekdayl=="help ex" or weekdayl=="help exi" or weekdayl=="help exit":
						print help.getExit()
					elif weekdayl=="help n" or weekdayl=="help nu" or weekdayl=="help num" or weekdayl=="help numb" or weekdayl=="help numbe" or weekdayl=="help number":
						print help.getSelectionWeekdayNum()
					elif weekdayl=="help q" or weekdayl=="help qu" or weekdayl=="help qui" or weekdayl=="help quit":
						print help.getQuit()
					#selects every day of the week and exits out of the day loop
					elif weekdayl=="all":
						dayString="*"
						dayConfirm=True
						dayTemp="every weekday of "
						break
					#system commands
					elif weekdayl=="clear":
						os.system("clear")
					elif weekdayl=="exit":
						return
					elif weekdayl=="quit":
						sys.exit()
					try: #try to see if it is an int
						if int(weekday)<1 or int(weekday)>7: #if it's not a valid input, then print that it's not
							print "Invalid input"
						else:
							weekday=int(weekday)-1 #weekdays in crontab are stored 0-6, but to make it less confusing 1-7 is used and subtract 1 for later
							if dayString.count(str(weekday))>0: #makes sure the day hasn't been added
								print "Day has already been added"
							else:
								dayTemp+=weekdays[int(weekday)] #matches to the dictionary and adds to string
								dayString+=str(weekday) #add to the string
								print dayTemp #prints it
								add=raw_input("Add another weekday(y/n)? ") #prompt for additional input
								if add=="n":
									dayConfirm=True
									dayTemp+=" of "
									break
								else:
									dayConfirm=True
									dayString+="," #these are used to format the string to the type needed for crontab
									dayTemp+=", "
							weekday=raw_input("What day of the week(1=Sunday, 7=Saturday, 'all'=every weekday)? ")
							if weekday=="":
								dayTemp=dayTemp[:-2]
								dayString=dayString[:-1]
								dayTemp+=" of "
					except ValueError: #if valueError then print this
						print "Invalid Input"
						weekday=raw_input("What day of the week(1=Sunday, 7=Saturday, 'all'=every weekday)? ")
						if weekday=="" and dayConfirm==True:
							dayTemp=dayTemp[:-2]
							dayString=dayString[:-1]
							dayTemp+=" of "
		#same thing for days just with months. Same functions
		while not monthConfirm:
			monthString=""
			monthTemp=""
			month=raw_input("What month(1=January, 12=December, 'all'=Every month)? ")
			while month!="":
				monthl=month.lower()
				if monthl=="help":
					print help.getSelectionMonthMain()+help.getCmdList()+help.getSelectionMonthAll()+help.getClear()+help.getExit()+help.getSelectionMonthNum()+help.getQuit()
				elif monthl=="help ":
					print help.getSelectionMonthAll()+help.getClear()+help.getExit()+help.getSelectionMonthNum()+help.getQuit()
				elif monthl=="help e" or monthl=="help ex" or monthl=="help exi" or monthl=="help exit":
					print help.getExit()
				elif monthl=="help a" or monthl=="help al" or monthl=="help all":
					print help.getSelectionMonthAll()
				elif monthl=="help c" or monthl=="help cl" or monthl=="help cle" or monthl=="help clea" or monthl=="help clear":
					print help.getClear()
				elif monthl=="help q" or monthl=="help qu" or monthl=="help qui" or monthl=="help quit":
					print help.getQuit()
				elif monthl=="help n" or monthl=="help nu" or monthl=="help num" or monthl=="help numb" or monthl=="help numbe" or monthl=="help number":
					print help.getSelectionMonthNum()
				elif monthl=="exit":
					return
				elif monthl=="quit":
					sys.exit()
				elif monthl=="clear":
					os.system("clear")
				elif monthl=='all':
					monthString="*"
					monthConfirm=True
					monthTemp="every Month at "
					break
				try:
					if int(month)<1 or int(month)>12:
						print "invalid input"
					else:
						if monthString.count(str(month))>0:
							print "Month has already been added"
						else:
							monthString+=str(month)
							monthTemp+=months[int(month)]
							print monthTemp
							add=raw_input("Add another month(y/n)? ")
							if add=="n":
								monthConfirm=True
								monthTemp+=" at "
								break
							else:
								monthConfirm=True
								monthString+=","
								monthTemp+=", "
						month=raw_input("What month(1=January, 12=December, 'all'=Every month)? ")
						if month=="":
							monthString=monthString[:-1]
							monthTemp=monthTemp[:-2]
							monthTemp+=" at "
				except ValueError:
					print "Invalid input"
					month=raw_input("What month(1=January, 12=December, 'all'=Every month)? ")
					if month=="" and monthConfirm==True:
						monthString=monthString[:-1]
						monthTemp=monthTemp[:-2]
						monthTemp+=" at "
		#same thing
		if dayType==1:
			while not dayConfirm:
				dayString=""
				dayTemp=""
				dayMonth=raw_input("What day of the month('all'=every day)? ")
				while dayMonth!="":
					dayMonthl=dayMonth.lower()
					if dayMonthl=="help":
						print help.getSelectionDayMain()+help.getCmdList()+help.getSelectionDayAll()+help.getClear()+help.getExit()+help.getSelectionDayNum()+help.getQuit()
					elif dayMonthl=="help ":
						print help.getSelectionDayAll()+help.getClear()+help.getExit()+help.getSelectionDayNum()+help.getQuit()
					elif dayMonthl=="help a" or dayMonthl=="help al" or dayMonthl=="help all":
						print help.getSelectionDayAll()
					elif dayMonthl=="help c" or dayMonthl=="help cl" or dayMonthl=="help cle" or dayMonthl=="help clea" or dayMonthl=="help clear":
						print help.getClear()
					elif dayMonthl=="help e" or dayMonthl=="help ex" or dayMonthl=="help exi" or dayMonthl=="help exit":
						print help.getExit()
					elif dayMonthl=="help n" or dayMonthl=="help nu" or dayMonthl=="help num" or dayMonthl=="help numb" or dayMonthl=="help numbe" or dayMonthl=="help number":
						print help.getSelectionDayNum()
					elif dayMonthl=="help q" or dayMonthl=="help qu" or dayMonthl=="help qui" or dayMonthl=="help quit":
						print help.getQuit()
					elif dayMonthl=="clear":
						os.system("clear")
					elif dayMonthl=="exit":
						return
					elif dayMonthl=="quit":
						sys.exit()
					elif dayMonthl=="all":
						dayString="*"
						dayConfirm=True
						dayTemp="every day of "
						break
					try:
						if int(dayMonth)<1 or int(dayMonth)>31:
							print "invalid input"
						else:
							if dayString.count(dayMonth)>0:
								print "Day has already been added"
							else:
								dayString+=dayMonth
								if int(dayMonth)==1 or int(dayMonth)==21 or int(dayMonth)==31:
									dayTemp+=str(dayMonth)+"st"
								elif int(dayMonth)==2 or int(dayMonth)==22:
									dayTemp+=str(dayMonth)+"nd"
								elif int(dayMonth)==3 or int(dayMonth)==23:
									dayTemp+=str(dayMonth)+"rd"
								else:
									dayTemp+=str(dayMonth)+"th"
								print dayTemp
								add=raw_input("Add another day(y/n)? ")
								if add=="n":
									dayConfirm=True
									dayTemp+=" of "
									break
								else:
									dayConfirm=True
									dayString+=","
									dayTemp+=", "
							dayMonth=raw_input("What day of the month('all'=every day)? ")
							if dayMonth=="":
								dayString=dayString[:-1]
								dayTemp=dayTemp[:-2]
								dayTemp+=" of "
					except ValueError:
						print "Invalid input"
						dayMonth=raw_input("What day of the month('all'=every day)? ")
						if dayMonth=="" and dayConfirm==True:
							dayString=dayString[:-1]
							dayTemp=dayTemp[:-2]
							dayTemp+=" of "
		#same thing
		while not hourConfirm:
			hourTemp=""
			hourString=""
			currentTime=strftime("%H%M,")
			hour=raw_input("What hour(UTC Current Time:"+currentTime+" 0-23, 'all'=every hour)? ")
			while hour!="":
				hourl=hour.lower()
				if hourl=="help":
					print help.getSelectionHourMain()+help.getCmdList()+help.getSelectionHourAll()+help.getClear()+help.getExit()+help.getSelectionHourNum()+help.getQuit()
				elif hourl=="help ":
					print help.getSelectionHourAll()+help.getClear()+help.getExit()+help.getSelectionHourNum()+help.getQuit()
				elif hourl=="help a" or hourl=="help al" or hourl=="help all":
					print help.getSelectionHourAll()
				elif hourl=="help c" or hourl=="help cl" or hourl=="help cle" or hourl=="help clea" or hourl=="help clear":
					print help.getClear()
				elif hourl=="help e" or hourl=="help ex" or hourl=="help exi" or hourl=="help exit":
					print help.getExit()
				elif hourl=="help n" or hourl=="help nu" or hourl=="help num" or hourl=="help numb" or hourl=="help numbe" or hourl=="help number":
					print help.getSelectionHourNum()
				elif hourl=="help q" or hourl=="help qu" or hourl=="help qui" or hourl=="help quit":
					print help.getQuit()
				elif hourl=="clear":
					os.system("clear")
				elif hourl=="exit":
					return
				elif hourl=="quit":
					sys.exit()
				elif hourl=='all':
					hourString="*"
					hourConfirm=True
					hourTemp="every hour"
					break
				try:
					if int(hour)<0 or int(hour)>23:
						print "invalid input"
					else:
						if hourString.count(hour)>0:
							print "Hour has already been added"
						else:
							hourString+=str(hour)
							hourTemp+=str(hour)
							print hourTemp
							add=raw_input("Add another hour(y/n)? ")
							if add=="n":
								hourConfirm=True
								hourTemp+=" hours"
								break
							else:
								hourConfirm=True
								hourString+=","
								hourTemp+=", "
						hour=raw_input("What hour(UTC Current Time: "+currentTime+" 0-23, 'all'=every hour)? ")
						if hour=="":
							hourString=hourString[:-1]
							hourTemp=hourTemp[:-2]
							hourTemp+=" hour"
				except ValueError:
					print "Invalid input"
					hour=raw_input("What hour(UTC Current Time: "+currentTime+" 0-23, 'all'=every hour)? ")
					if hour=="" and hourConfirm==True:
						hourString=hourString[:-1]
						hourTemp=hourTemp[:-2]
						hourTemp+=" hour"
		#same thing
		while not minuteConfirm:
			minuteTemp=""
			minuteString=""
			minute=raw_input("What minute(0-59, 'all'=every minute)? ")
			while minute!="":
				minutel=minute.lower()
				if minutel=="help":
					print help.getSelectionMinuteMain()+help.getCmdList()+help.getSelectionMinuteAll()+help.getClear()+help.getExit()+help.getSelectionMinuteNum()+help.getQuit()
				elif minutel=="help ":
					print help.getSelectionMinuteAll()+help.getClear()+help.getExit()+help.getSelectionMinuteNum()+help.getQuit()
				elif minutel=="help a" or minutel=="help al" or minutel=="help all":
					print help.getSelectionMinuteAll()
				elif minutel=="help c" or minutel=="help cl" or minutel=="help cle" or minutel=="help clea" or minutel=="help clear":
					print help.getClear()
				elif minutel=="help e" or minutel=="help ex" or minutel=="help exi" or minutel=="help exit":
					print help.getExit()
				elif minutel=="help n" or minutel=="help nu" or minutel=="help num" or minutel=="help numb" or minutel=="help numbe" or minutel=="help number":
					print help.getSelectionMinuteNum()
				elif minutel=="help q" or minutel=="help qu" or minutel=="help qui" or minutel=="help quit":
					print help.getQuit()
				elif minutel=="clear":
					os.system("clear")
				elif minutel=="exit":
					return
				elif minutel=="quit":
					sys.exit()
				elif minutel=='all':
					minuteString=="*"
					minuteConfirm=True
					minuteTemp="every minute of "
					break
				try:
					if int(minute)<0 or int(minute)>59:
						print "invalid input"
					else:
						if minuteString.count(minute)>0:
							print "Minute has already been added"
						else:
							minuteString+=str(minute)
							minuteTemp+=str(minute)
							print minuteTemp
							add=raw_input("Add another minute(y/n)? ")
							if add=="n":
								minuteConfirm=True
								minuteTemp+=" minutes of "
								break
							else:
								minuteConfirm=True
								minuteString+=","
								minuteTemp+=", "
						minute=raw_input("What minute(0-59, 'all'=every minute)? ")
						if minute=="":
							minuteString=minuteString[:-1]
							minuteTemp=minuteTemp[:-2]
							minuteTemp+=" minutes of "
				except ValueError:
					print "Invalid input"
					minute=raw_input("What minute(0-59, 'all'=every minute)? ")
					if minute=="" and minuteConfirm==True:
						minuteString=minuteString[:-1]
						minuteTemp=minuteTemp[:-2]
						minuteTemp+=" minutes of "
		newTemp=temp+dayTemp+monthTemp+minuteTemp+hourTemp
		print newTemp
		confirmString=raw_input("Is this correct(y/n)? ") #prompts to confirm that it is the correct time setting
		if confirmString.lower()=="y":
			confirm=True
		else:
			confirm=False
			change=raw_input("\n\t\t1. Days\n\t\t2. Months\n\t\t3. Hours\n\t\t4. Minutes\n\nWhich setting to change(enter to continue)? ") #asks what settings need to be changed
			while change!="":
				changel=change.lower()
				if changel=="help":
					print help.getSelectionChangeMain()+help.getCmdList()+help.getClear()+help.getExit()+help.getSelectionChangeNum()+help.getQuit()
				elif changel=="help ":
					print help.getClear()+help.getExit()+help.getSelectionChangeNum()+help.getQuit()
				elif changel=="help c" or changel=="help cl" or changel=="help cle" or changel=="help clea" or changel=="help clear":
					print help.getClear()
				elif changel=="help e" or changel=="help ex" or changel=="help exi" or changel=="help exit":
					print help.getExit()
				elif changel=="help n" or changel=="help nu" or changel=="help num" or changel=="help numb" or changel=="help numbe" or changel=="help number":
					print help.getSelectionChangeNum()
				elif changel=="help q" or changel=="help qu" or changel=="help qui" or changel=="help quit":
					print help.getQuit()
				try: #sets the boolean to false for every setting that needs to be changed
					if int(change)==1:
						dayConfirm=False
					elif int(change)==2:
						monthConfirm=False
					elif int(change)==3:
						hourConfirm=False
					elif int(change)==4:
						minuteConfirm=False
					else:
						print "Invalid input"
					change=raw_input("\n\t\t1. Days\n\t\t2. Months\n\t\t3. Hours\n\t\t4. Minutes\n\nWhich setting to change(enter to continue)? ")
				except ValueError:
					print "Invalid input"
					change=raw_input("\n\t\t1. Days\n\t\t2. Months\n\t\t3. Hours\n\t\t4. Minutes\n\nWhcih setting to change(enter to continue)? ")
	selectionType=raw_input("\n\t\t1. Type device names\n\t\t2. Select devices\n\nChoose a mode of selecting devices: ") #prompts for the type of selection desired for selecting devices
	while selectionType!="":
		selectionTypel=selectionType.lower()
		if selectionTypel=="help":
			print help.getSelectionSelectionType()+help.getCmdList()+help.getClear()+help.getExit()+help.getQuit()
		elif selectionTypel=="help ":
			print help.getClear()+help.getExit()+help.getQuit()
		elif selectionTypel=="help c" or selectionTypel=="help cl" or selectionTypel=="help cle" or selectionTypel=="help clea" or selectionTypel=="help clear":
			print help.getClear()
		elif selectionTypel=="help e" or selectionTypel=="help ex" or selectionTypel=="help exi" or selectionTypel=="help exit":
			print help.getExit()
		elif selectionTypel=="help q" or selectionTypel=="help qu" or selectionTypel=="help qui" or selectionTypel=="help quit":
			print help.getQuit()
		elif selectionTypel=="clear":
			os.system("clear")
		elif selectionTypel=="exit":
			return
		elif selectionTypel=="quit":
			sys.exit()
		#same thing with manual selection with archiving and templating
		elif selectionType=="1":
			device=raw_input("Type the name of the device: ")
			selectString=""
			while device!="":
				devicel=device.lower()
				if devicel=="help":
					print help.getSelectionSelectionType1()+help.getCmdList()+help.getClear()+help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getQuit()
				elif devicel=="help ":
					print help.getClear()+help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getQuit()
				elif devicel=="help c" or devicel=="help cl" or devicel=="help cle" or devicel=="help clea" or devicel=="help clear":
					print help.getClear()
				elif devicel=="help e":
					print help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()+help.getExit()
				elif devicel=="help en":
					print help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()
				elif devicel=="help end":
					print help.getSelectionSelectionTypeEnd()
				elif devicel=="help ent" or devicel=="help ente" or devicel=="help enter":
					print help.getArchive
				elif devicel=="help ex" or devicel=="help exi" or devicel=="help exit":
					print help.getExit()
				elif devicel=="help q" or devicel=="help qu" or devicel=="help qui" or devicel=="help quit":
					print help.getQuit()
				elif devicel=="clear": os.system("clear")
				elif devicel=="exit": return
				elif devicel=="quit": sys.exit()
				elif devicel=="end":
					selectString=selectString[:-1]
					device_list=selectString.split(",")
					username=raw_input("Username: ")
					pswd=getpass.getpass('Password: ')
					for dev in device_list:
						if dev in devices:
							#here it creates a new file with the existing cron jobs
							os.system("crontab -l > mycron")
							#creates new string that will be used to state the cron job
							job="echo \""
							#puts minutes, hours, days, and months in string
							job+=minuteString+" "
							job+=hourString+" "
							if dayType==1:
								job+=dayString+" "
							else:
								job+="* "
							job+=monthString+" "
							if dayType==2:
								job+=dayString+" "
							else:
								job+="* "
							#what command will be run at the selected time
							if templates!=None: #if template was given (meaning it's an apply), run this command
								job+="python sshTest/pushTemplateNew.py "+username+" "+pswd+" "+devices[dev]+" "+dev+" "+templates[1]+" "+templates[0]+"\""
							else: #if not, run this
								job+="python sshTest/exportConfgNew.py "+username+" "+pswd+" "+devices[dev]+" "+dev+"\""
							#adds it to the string. It'll echo into the file, adding the job
							job+=" >> mycron"
							#run it on the system
							os.system(job)
							#replace the user crontab with the file
							os.system("crontab mycron")
							#remove the file
							os.system("rm mycron")
                                                        os.system("crontab -l > Schedule")
						else:
							print dev+" is not in the directory"
					break
				else:
					selectString+=device+","
				device=raw_input("Type the name of the device: ")
		#same thing with other list selections
		elif selectionType=="2":
			number=input("How many devices per page? ")
			selectString=""
			current=0
			selectionl=""
			for i in range(1, len(devices)+number, number):
				for y in range(number):
					current=i+y
					print "%d. %s" % (i+y, device_index[current])
					if (y+i)==len(devices):
						break
				selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
				selectionl=selection.lower()
				while selectionl!="":
					if selectionl=="help":
						print help.getSelectionSelectionType2()+help.getCmdList()+help.getClear()+help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getArchiveConfgMode2Next()+help.getQuit()
					elif selectionl=="help ":
						print help.getClear()+help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getArchiveConfgMode2Next()+help.getQuit()
					elif selectionl=="help c" or selectionl=="help cl" or selectionl=="help cle" or selectionl=="help clea" or selectionl=="help clear":
						print help.getClear()
					elif selectionl=="help e":
						print help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()+help.getExit()
					elif selectionl=="help en":
						print help.getSelectionSelectionTypeEnd()+help.getArchiveConfgMode1Enter()
					elif selectionl=="help end":
						print help.getSelectionSelectionTypeEnd()
					elif selectionl=="help ent" or selectionl=="help ente" or selectionl=="help enter":
						print help.getArchiveConfgMode1Enter()
					elif selectionl=="help ex" or selectionl=="help exi" or selectionl=="help exit":
						print help.getExit()
					elif selectionl=="help n" or selectionl=="help ne" or selectionl=="help nex" or selectionl=="help next":
						print help.getArchiveConfgMode2Next()
					elif selectionl=="help q" or selectionl=="help qu" or selectionl=="help qui" or selectionl=="help quit":
						print help.getQuit()
					elif selectionl=="clear":
						os.system("clear")
						for y in range(number):
							current=i+y
							print "%d. %s" % (i+y, device_index[current])
							if (y+i)==len(devices): break
					elif selectionl=="end" or selectionl=="next":
						break
					elif selectionl=="exit":
						return
					elif selectionl=="quit":
						sys.exit()
					try:
						if int(selection) in range(len(devices)+1):
							selectString=selectString+device_index[int(selection)]+","
							print device_index[int(selection)]+" added"
						else:
							print "Incorrect input"
						selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
						selectionl=selection.lower()
					except ValueError:
						print "Invalid input"
						selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
						selectionl=selection.lower()
				if current==len(devices): break
				elif selectionl=="end" or selectionl=="":
					break
				os.system("clear")
				print "Selected: "+selectString
			if selectionl!="":
				selectString=selectString[:-1]
				selections=selectString.split(",")
				username=raw_input("Username: ")
				pswd=getpass.getpass('Password: ')
				for selection in selections:
					if selection in devices:
						#same thing as above
						os.system("crontab -l > mycron")
						job="echo \""
						job+=minuteString+" "
						job+=hourString+" "
						if dayType==1:
							job+=dayString+" "
						else:
							job+="* "
						job+=monthString+" "
						if dayType==2:
							job+=dayString+" "
						else:
							job+="* "
						if templates!=None:
							job+="python sshTest/pushTemplateNew.py "+username+" "+pswd+" "+devices[selection]+" "+selection+" "+templates[1]+" "+templates[0]+"\""
						else:
							job+="python sshTest/exportConfgNew.py "+username+" "+pswd+" "+devices[selection]+" "+selection+"\""
						job+=" >> mycron"
						os.system(job)
						os.system("crontab mycron")
						os.system("rm mycron")
					else:
						print selection+" is not in the directory"
				break
		else:
			print "Invalid input"
			selectionType=raw_input("\n\t\t1. Type device names\n\t\t2. Select devices\n\nChoose a mode of selection devices: ")



def applyTemplate():
	selected={}
	modeMessage="""
	1. Type device to apply
	2. Select devices to apply
	3. Schedule template apply

Choose a mode for applying the template: """
	templates=viewOrModifyOldRunner(True) #gets a template from another function/module, getting the path to the template parent file and the path to the template
	if templates!=False:
		print modeMessage,
		mode=raw_input()
		while mode!="":
			model=mode.lower()
			if model=="help":
				print help.getApplyTemplateMode()+help.getCmdList()+help.getApplyTemplateMode1()+help.getApplyTemplateMode2()+help.getApplyTemplateMode3()+help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
			elif model=="help ":
				print help.getApplyTemplateMode1()+help.getApplyTemplateMode2()+help.getApplyTemplatMode3()+help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
			elif model=="help 1": print help.getApplyTemplateMode1()
			elif model=="help 2": print help.getApplyTemplateMode2()
			elif model=="help 3": print help.getApplyTemplateMode3()
			elif model=="help c" or model=="help cl" or model=="help cle" or model=="help clea" or model=="help clear":
				print help.getClear()
			elif model=="help e":
				print help.getEnter1()+help.getExit()
			elif model=="help en" or model=="help ent" or model=="help ente" or model=="help enter":
				print help.getEnter1()
			elif model=="help ex" or model=="help exi" or model=="help exit":
				print help.getExit()
			elif model=="help q" or model=="help qu" or model=="help qui" or model=="help quit":
				print help.getQuit()
			elif model=="clear":
				os.system("clear")
			elif model=="exit":
				return
			elif model=="quit":
				sys.exit()
			#same thing as archive just a different end result
			elif mode=="1":
				selectString=""
				device=raw_input("Type the name of the device: ")
				while device!="":
					devicel=device.lower()
					if devicel=="help":
						print help.getApplyTemplateMode1Main()+help.getCmdList()+help.getClear()+help.getApplyTemplateMode1End()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getQuit()
					elif devicel=="help ":
						print help.getClear()+help.getApplyTemplateMode1End()+help.getArchiveConfgMode1Enter()+help.getExit()+help.getQuit()
					elif devicel=="help c" or devicel=="help cl" or devicel=="help cle" or devicel=="help clea" or devicel=="help clear":
						print help.getClear()
					elif devicel=="help e":
						print help.getApplyTemplateMode1End()+help.getArchiveConfgMode1Enter()+help.getExit()
					elif devicel=="help en":
						print help.getApplyTemplateMode1End()+help.getArchiveConfgMode1Enter()
					elif devicel=="help end":
						print help.getApplyTemplateMode1End()
					elif devicel=="help ent" or devicel=="help ente" or devicel=="help enter":
						print help.getArchiveConfgMode1Enter()
					elif devicel=="help ex" or devicel=="help exi" or devicel=="help exit":
						print help.getExit()
					elif devicel=="help q" or devicel=="help qu" or devicel=="help qui" or devicel=="help quit":
						print help.getQuit()
					elif devicel=="clear":
						os.system("clear")
					elif devicel=="exit":
						return
					elif devicel=="quit":
						sys.exit()
					elif devicel=="end":
						selectString=selectString[:-1]
						device_list=selectString.split(",")
						username=raw_input("Username: ")
						pswd=getpass.getpass('Password: ')
						for dev in device_list:
							if dev in devices:
								#exports first and then applys. sshTest/pushTemplateNew.py
								export=exportConfgNew.exportConfg(devices[dev], username=username, password=pswd, pushOrPull=False, device=dev)
								export.connect()
								export.mkdir()
								export.export(False, False)
								apply=pushTemplateNew.pushTemplate(devices[dev], username=username, password=pswd, device=dev, fileLocation=templates[1], path=templates[0])
								apply.connect()
								apply.apply()
							else:
								print dev+" is not in the device directory"
						break
					else:
						selectString=device+","
					print selectString
					device=raw_input("Type the name of the device: ")
			#same thing as archiving again
			elif mode=="2":
				number= input("How many devices per page? ")
				selectString=""
				current=0
				selectionl=""
				for i in range(1, (len(devices)+number), number):
					for y in range(number):
						current=i+y
						print "%d. %s" % (i+y,device_index[current])
						if (y+i)==len(devices): break
					selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
					selectionl=selection.lower()
					while selectionl!="next":
						if selectionl=="help":
							print help.getApplyTemplateMode2Main()+help.getCmdList()+help.getClear()+help.getApplyTemplateMode2End()+help.getExit()+help.getArchiveConfgMode2Next()+help.getArchiveConfgMode2Num()+help.getQuit()
						elif selectionl=="help ":
							print help.getClear()+help.getApplyTemplateMode2End()+help.getExit()+help.getArchiveConfgMode2Next()+help.getArchiveConfgMode2Num()+help.getQuit()
						elif selectionl=="help c" or selectionl=="help cl" or selectionl=="help cle" or selectionl=="help clea" or selectionl=="help clear":
							print help.getClear()
						elif selectionl=="help e":
							print help.getApplyTemplateMode2End()+help.getExit()
						elif selectionl=="help en" or selectionl=="help end":
							print help.getApplyTemplateMode2End()
						elif selectionl=="help ex" or selectionl=="help exi" or selectionl=="help exit":
							print help.getExit()
						elif selectionl=="help n":
							print help.getArchiveConfgMode2Next()+help.getArchiveConfgMode2Num()
						elif selectionl=="help ne" or selectionl=="help nex" or selectionl=="help next":
							print help.getArchiveConfgMode2Next()
						elif selectionl=="help nu" or selectionl=="help num" or selectionl=="help numb" or selectionl=="help numbe" or selectionl=="help number":
							print help.getArchiveConfgMode2Num()
						elif selectionl=="help q" or selectionl=="help qu" or selectionl=="help qui" or selectionl=="help quit":
							print help.getQuit()
						elif selectionl=="clear":
							os.system("clear")
							for y in range(number):
								current=i+y
								print "%d. %s" % (i+y, device_index[current])
								if (i+y)==len(devices): break
							print "Selected: "+selectString
						elif selectionl=="exit":
							return
						elif selectionl=="end":
							break
						elif selectionl=="quit":
							sys.exit()
						elif selectionl=="":
							break
						try:
							if int(selection) in range(len(devices)+1):
								selectString=selectString+device_index[int(selection)]+","
								print device_index[int(selection)]+" added"
							else:
								print "Incorrect input"
						except ValueError:
							print "Invalid input"
						selection=raw_input("Type the number corresponding to the device to add it or type next to continue: ")
						selectionl=selection.lower()
					if current==len(devices):
						break
					elif selectionl=="end" or selectionl=="":
						break
					os.system("clear")
					print "Selected: "+selectString
				if selectionl!="":
					selectString=selectString[:-1]
					selections=selectString.split(",")
					username=raw_input("Username: ")
					pswd=getpass.getpass('Password: ')
					for selection in selections:
						if selection in devices:
							export=exportConfgNew.exportConfg(devices[selection], username=username, password=pswd, pushOrPull=False, device=selection)
							export.connect()
							export.mkdir()
							export.export(False, False)
							apply=pushTemplateNew.pushTemplate(devices[selection], username=username, password=pswd, device=selection, fileLocation=templates[1], path=templates[0])
							apply.connect()
							apply.apply()
						else:
							print selection+" is not in the device directory"
			elif mode=="3":
				scheduling(templates)
				return
			else:
				print "Invalid Input"
			print modeMessage,
			mode=raw_input()

def createNew(device=None, templateName=None, txt=None):
        txtPrompt= """
        1. Vim
        2. Nano

Which text editor (type number): """
	if device==None:
		print "What device is this template being created for? ",
		device=raw_input()
	while device!="":
		devicel=device.lower()
		if devicel=="help":
			print help.getCreateNewMain()+help.getCmdList()+help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
		elif devicel=="help ":
			print help.getClear()+help.getEnter1()+help.getExit()+help.getQuit()
		elif devicel=="help c" or devicel=="help cl" or devicel=="help cle" or devicel=="help clea" or devicel=="help clear":
			print help.getClear()
		elif devicel=="help e":
			print help.getEnter1()+help.getExit()
		elif devicel=="help en" or devicel=="help ent" or devicel=="help ente" or devicel=="help enter":
			print help.getEnter1()
		elif devicel=="help ex" or devicel=="help exi" or devicel=="help exit":
			print help.getExit()
		elif devicel=="help q" or devicel=="help qu" or devicel=="help qui" or devicel=="help quit":
			print help.getQuit()
		elif devicel=="exit":
			return
		elif devicel=="clear":
			os.system("clear")
		elif devicel=="quit":
			sys.exit()
		else:
			confirm=raw_input(device+": Is this the correct device(y/n)? ")
			if confirm.lower!="y":
				if not os.path.exists("/home/cheti/tftp/templates/devices/"+device):
					os.mkdir("/home/cheti/tftp/templates/devices/"+device)
					os.chmod("/home/cheti/tftp/templates/devices/"+device, 0777)
				if templateName==None:
					print "What is the template name? ",
					templateName=raw_input()
				while templateName!="":
					templateNamel=templateName.lower()
					if templateNamel=="help":
						print help.getCreateNewName()+help.getCmdList()+help.getClear()+help.getCreateNewEnter()+help.getExit()+help.getQuit()
					elif templateNamel=="help ":
						print help.getClear()+help.getCreateNewEnter()+help.getExit()+help.getQuit()
					elif templateNamel=="help c" or templateNamel=="help cl" or templateNamel=="help cle" or templateNamel=="help clea" or templateNamel=="help clear":
						print help.getClear()
					elif templateNamel=="help e":
						print help.getCreateNewEnter()+help.getExit()
					elif templateNamel=="help en" or templateNamel=="help ent" or templateNamel=="help ente" or templateNamel=="help enter":
						print help.getCreateNewEnter()
					elif templateNamel=="help ex" or templateNamel=="help exi" or templateNamel=="help exit":
						print help.getExit()
					elif templateNamel=="help q" or templateNamel=="help qu" or templateNamel=="help qui" or templateNamel=="help quit":
						print help.getQuit()
					else:
						if txt==None:
							txt=raw_input(txtPrompt)
						while txt!="1" and txt!="2" and txt.lower()!="vim" and txt.lower()!="nano":
							txtl=txt.lower()
							if txtl=="help":
								print help.getTxt()+help.getCmdList()+help.getClear()+help.getExit()+help.getQuit()
							elif txtl=="help ":
								print help.getClear()+help.getExit()+help.getQuit()
							elif txtl=="help c" or txtl=="help cl" or txtl=="help cle" or txtl=="help clea" or txtl=="help clear":
								print help.getClear()
							elif txtl=="help e" or txt1=="help ex" or txtl=="help exi" or txtl=="help exit":
								print help.getExit()
							elif txtl=="help q" or txtk=="help qu" or txtl=="help qui" or txtl=="help quit":
								print help.getQuit()
							else:
								print "Invalid input"
							txt=raw_input(txtPrompt)
						if txt=="1":
							txt="vim"
						elif txt=="2":
							txt="nano"
						os.system(txt+" "+templateName+".template")
						os.rename(templateName+".template", "tftp/templates/devices/"+
							device+"/"+templateName+".template")
						break
					print "What is the template name? ",
					templateName=raw_input()
				if templateName!="": break
		print "What device is this template being created for? ",
		device=raw_input()

def viewOrModifyOldRunner(choosing):
	devices=os.listdir("tftp/templates/devices")
	print "\nDevices"
	print "-------"
	for device in devices:
		print device
	print ""
	print "Which device? ",
	inputDevice=raw_input()
	while inputDevice!="":
		inputDevicel=inputDevice.lower()
		if inputDevicel=="help":
			print help.getViewOrModifyOldRunnerMain()+help.getCmdList()+help.getClear()+help.getEnter1()+help.getExit()+help.getViewOrModifyOldRunnerName()+help.getQuit()
		elif inputDevicel=="help ":
			print help.getClear()+help.getEnter1()+help.getExit()+help.getViewOrModifyOldRunnerName()+help.getQuit()
		elif inputDevicel=="help c" or inputDevicel=="help cl" or inputDevicel=="help cle" or inputDevicel=="help clea" or inputDevicel=="help clear":
			print help.getClear()
		elif inputDevicel=="help e":
			print help.getEnter1()+help.getExit()
		elif inputDevicel=="help en" or inputDevicel=="help ent" or inputDevicel=="help ente" or inputDevicel=="help enter":
			print help.getEnter1()
		elif inputDevicel=="help ex" or inputDevicel=="help exi" or inputDevicel=="help exit":
			print help.getExit()
		elif inputDevicel=="help n" or inputDevicel=="help na" or inputDevicel=="help nam" or inputDevicel=="help name":
			print help.getViewOrModifyOldRunnerName()
		elif inputDevicel=="help q" or inputDevicel=="help qu" or inputDevicel=="help qui" or inputDevicel=="help quit":
			print help.getQuit()
		elif inputDevicel=="clear":
			os.system("clear")
		elif inputDevicel=="exit":
			return False
		elif inputDevicel=="quit":
			sys.exit()
		elif not os.path.exists("tftp/templates/devices/"+inputDevice):
			print "Incorrect device"
		else:
			if choosing==True:
				paths=viewOrModifyOld(inputDevice, choosing)
				if paths!=None:
					return paths
				elif paths==False:
					return False
			else:
				viewOrModifyOld(inputDevice, choosing)
		print "\nDevices"
		print   "-------"
		for dev in devices:
			print dev
		print "\nWhich device? ",
		inputDevice=raw_input()
	return False

def viewOrModifyOld(device, choosing):
	templates=os.listdir("tftp/templates/devices/"+device)
	print "\nTemplates"
	print "---------"
	for template in templates:
		print template
	print ""
	print "Which template? ",
	inputTemplate=raw_input()
	while inputTemplate!="":
		inputTemplatel=inputTemplate.lower()
		if inputTemplatel=="help":
			print help.getViewOrModifyOldMain()+help.getCmdList()+help.getClear()+help.getViewOrModifyOldEnter()+help.getExit()+help.getViewOrModifyOldName()+help.getQuit()
		elif inputTemplatel=="help ":
			print help.getClear()+help.getViewOrModifyOldEnter()+help.getExit()+help.getViewOrModifyOldName()+help.getQuit()
		elif inputTemplatel=="help c" or inputTemplatel=="help cl" or inputTemplatel=="help cle" or inputTemplatel=="help clea" or inputTemplatel=="help clear":
			print help.getClear()
		elif inputTemplatel=="help e":
			print help.getViewOrModifyOldEnter()+help.getExit()
		elif inputTemplatel=="help en" or inputTemplatel=="help ent" or inputTemplatel=="help ente" or inputTemplatel=="help enter":
			print help.getViewOrModifyOldEnter()
		elif inputTemplatel=="help ex" or inputTemplatel=="help exi" or inputTemplatel=="help exit":
			print help.getExit()
		elif inputTemplatel=="help n" or inputTemplatel=="help na" or inputTemplatel=="help nam" or inputTemplatel=="help name":
			print help.getViewOrModifyOldName()
		elif inputTemplatel=="help q" or inputTemplatel=="help qu" or inputTemplatel=="help qui" or inputTemplatel=="help quit":
			print help.getQuit()
		elif inputTemplatel=="clear":
			os.system("clear")
		elif inputTemplatel=="exit":
			return False
		elif inputTemplatel=="quit":
			sys.exit()
		elif not os.path.exists("tftp/templates/devices/"+device+"/"+inputTemplate):
			print "That template does not exist"
		elif choosing==True:
			paths=["tftp/templates/devices/"+device+"/","tftp/templates/devices/"+device+"/"+inputTemplate]
			return paths
		else:
                        print "\n\t\t1. Vim\n\t\t2. Nano\n\nWhich text editor (type number): ",
                        txt=raw_input()
                        while txt!="1" and txt!="2":
				txtl=txt.lower()
				if txtl=="help":
					print help.getTxt()+help.getCmdList()+help.getClear()+help.getExit()+help.getQuit()
				elif txtl=="help ":
					print help.getClear()+help.getExit()+help.getQuit()
				elif txtl=="help c" or txtl=="help cl" or txtl=="help cle" or txtl=="help clea" or txtl=="help clear":
					print help.getClear()
				elif txtl=="help e" or txtl=="help ex" or txtl=="help exi" or txtl=="help exit":
					print help.getExit()
				elif txtl=="help q" or txtl=="help qu" or txtl=="help qui" or txtl=="help quit":
					print help.getQuit()
				elif txtl=="clear":
					os.system("clear")
				elif txtl=="exit":
					return False
				elif txtl=="quit":
					sys.exit()
                        	print "Invalid input"
                        	txt=raw_input("\n\t\t1. Vim\n\t\t2. Nano\n\nWhich text editor (type number): ")
                        if txt=="1":
                        	txt="vim"
                        else:
				txt="nano"
			os.system(txt+" tftp/templates/devices/"+device+"/"+inputTemplate)
		print "\nTemplates"
		print   "---------"
		for temp in templates:
			print temp
		print "\nWhich template? ",
		inputTemplate=raw_input()
	return None

def viewConfigurations():
	dates=os.listdir("tftp/archive")
	print "\nDates"
	print "-----"
	for dat in dates:
		print dat
	date=raw_input("\nWhich date? ")
	while date!="":
		datel=date.lower()
		if datel=="help":
			print "help function to be added in Alpha 2.0"
		elif datel=="clear":
			os.system("clear")
		elif datel=="exit":
			return
		elif datel=="quit":
			sys.exit()
		elif not os.path.exists("tftp/archive/"+date):
			print "That date has no archives attached to it"
		else:
			hostnames=os.listdir("tftp/archive/"+date+"/")
			print "\nHostnames"
			print "---------"
			for device in hostnames:
				print device
			dev=raw_input("\nWhich hostname? ")
			while dev!="":
				devl=dev.lower()
				if devl=="help":
					pass
				elif not os.path.exists("tftp/archive/"+date+"/"+dev):
					print "That hostname doesn't exist"
				else:
					configs=os.listdir("tftp/archive/"+date+"/"+dev+"/")
					print "\nConfigurations"
					print "--------------"
					for file in configs:
						if os.path.isfile(os.path.join("tftp/archive/"+date+"/"+dev+"/", file)):
							print file
					config=raw_input("\nWhich configuration? ")
					while config!="":
						configl=config.lower()
						if configl=="help":
							pass
						elif not os.path.exists("tftp/archive/"+date+"/"+dev+"/"+config):
							print "That configuration does not exist"
						else:
							print "\n\t\t1. Vim\n\t\t2. Nano\n\nWhich text editor (type number): "
							txt=raw_input()
							while txt!="1" and txt!="2":
								txtl=txt.lower()
								if txtl=="help":
									pass
								print "Invalid input"
								txt=raw_input("\n\t\t1. Vim\n\t\t2. Nano\n\nWhich text editor (type number): ")
							if txt=="1": txt="vim"
							else: txt="nano"
							os.system(txt+" tftp/archive/"+date+"/"+dev+"/"+config)
						print "\nConfigurations"
						print "--------------"
						for file in configs:
							if os.path.isfile(os.path.join("tftp/archive/"+date+"/"+dev+"/", file)):
								print file
						config=raw_input("\nWhich configuration? ")
				print "\nHostnames"
				print "---------"
				for device in hostnames:
					print device
				dev=raw_input("\nWhich hostname? ")
		print "\nDates"
		print "-----"
		for dat in dates:
			print dat
		date=raw_input("\nWhich date? ")
