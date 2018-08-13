import os
import time
import sys
import ciscoPrimeReplacer

ciscoPrimeReplacer.loadDictionaries()
bootMessage= """
-------------------------------------------------------------------
	      Project Packrat - Cisco Prime Prototype
                         Alpha Version 1.9
-------------------------------------------------------------------

Which service will be used today?

	1. Add new device
	2. Look up devices
	3. Archive current configurations
	4. Apply templates
	5. Create new templates
	6. View and edit templates
	7. View archived configurations
	8. SSH into device
	9. Exit

Service: """

message= """	1. Add new device
	2. Look up devices
	3. Archive current configurations
	4. Apply templates
	5. Create new templates
	6. View and edit templates
	7. View archived configurations
	8. SSH into device
	9. Exit

Service: """

if len(sys.argv)==1:
	os.system("clear")
	print bootMessage,
	while True:
		service=raw_input()
		if service=="1":
			ciscoPrimeReplacer.addDevice()
		elif service=="2":
			ciscoPrimeReplacer.lookupDevice()
		elif service=="3":
			ciscoPrimeReplacer.archiveConfg()
		elif service=="4":
			ciscoPrimeReplacer.applyTemplate()
		elif service=="5":
			ciscoPrimeReplacer.createNew()
		elif service=="6":
			ciscoPrimeReplacer.viewOrModifyOldRunner(False)
		elif service=="7":
			ciscoPrimeReplacer.viewConfigurations()
		elif service=="8":
			print "SSH to be added in Alpha Version 2.0\n"
			time.sleep(.5)
		elif service=="9":
			print "\nExiting...\n"
			break
		elif service.lower()=="help":
			print "Help command to be added in Alpha Version 2.0\n"
			time.sleep(.5)
		else:
			print "\nIncorrect input\n"
			time.sleep(.5)
		if service.lower()!="help":
			os.system("clear")
			print bootMessage,
		else:
			print message,
else:
	i=len(sys.argv)
	temp=sys.argv[1]
	if temp=="add":
		if i>=4:   ciscoPrimeReplacer.addDevice(device=sys.argv[2], ip=sys.argv[3])
		elif i==3: ciscoPrimeReplacer.addDevice(device=sys.argv[2])
		else:      ciscoPrimeReplacer.addDevice()
	elif temp=="search":
		if i>=3: ciscoPrimeReplacer.lookupDevice(hostnameOrIP=sys.argv[2])
		else:    ciscoPrimeReplacer.lookupDevice()
	elif temp=="archive":
		if i>=3: ciscoPrimeReplacer.archiveConfg(ip=sys.argv[2])
		else:    ciscoPrimeReplacer.archiveConfg()
	elif temp=="apply":
		ciscoPrimeReplacer.applyTemplate()
	elif temp=="new":
		if i>=5:   ciscoPrimeReplacer.createNew(device=sys.argv[2], templateName=sys.argv[3], txt=sys.argv[4])
		elif i==4: ciscoPrimeReplacer.createNew(device=sys.argv[2], templateName=sys.argv[3])
		elif i==3: ciscoPrimeReplacer.createNew(device=sys.argv[2])
		else:	   ciscoPrimeReplacer.createNew()
	elif temp=="view":
		ciscoPrimeReplacer.viewOrModifyOldRunner(False)
	elif temp=="ssh":
		print "SSH to be added in Alpha Version 2.0\n"
