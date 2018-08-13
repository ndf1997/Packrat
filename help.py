addDeviceMain="""
This is the module to add a new Cisco device to the device directory in Project Packrat.
By adding a device, Project Packrat is able to acquire the information on that device.
"""
addDeviceDevice="""
Currently, the module is asking for the device's hostname.

After typing the device's hostname, Project Packrat will check the device directory to ensure that
the hostname is not already in use. If it is in us, Project Packrat will respond by showing the IP
assigned to that hostname.

After putting in a valid hostname, Project Packrat will then ask for the IP Address to be assigned to
that device, and then it will add the device to the device directory.
"""

cmdList="""
Command List
-------------------------------------------------
"""
enter1="*enter* - returns the program to the start screen\n"
exit="exit - returns the program to the main screen\n"
quit="quit - exits the program entirely\n"
addDeviceIP="""
Currently, the module is asking for the IP address assigned to the new device.

The module has checked to see if the new device's hostname already exists, and finding that it does not
now needs the IP address assigned to that device.

After typing the device's IP address, Project Packrat will check the device directory to ensure that the
IP Address is not already in use. If it is in use, Project Packrat will respond by showing the hostname
that has the IP address assigned to it
"""
addDeviceEnter2="*enter* - returns the program to the naming screen\n"
addDeviceDeviceName="device - shows the hostname of the added device\n"
lookupDeviceMain="""
This is a module used to look up device names and, if desired, rename them.
Project Packrat searches the device directory for the hostname or IP Address and returns it
"""
lookupDeviceSearch="""
Currently, the module is asking for a hostname or IP Address to search for.
If it finds that it exists it will return. If it does not exist it will return that it is not in use
"""
lookupDeviceIP="ip - returns the entire list of IP addresses in the device directory\n"
lookupDeviceDevice="devices - returns the entire list of device hostnames in the device directory\n"
archiveConfgMain="""\nThis module is used to control the archiving of device running and startup configs.\n"""
archiveConfgMode="""
This screen is used to select the way archives are created. Typing devices requires manual input of device hostnames,
selecting devices allows for the selection of hostnames from a list that is presented by a user defined speed,
and scheduling is used to set archives at a certain or repeating time.
"""
applyTemplateMode="""
This screen is used to select the way templates are applied. Typing devices requires manual input of device
hostnames, selecting devices allows for the selection of hostnames from a list that is presented by a user defined
speed, and scheduling is used to set applys at a certain or repeating time.
"""
archiveConfgMode1="1 - Force an archive by manually adding devices\n"
archiveConfgMode2="2 - Force an archive by selecting devices from a numbered list\n"
archiveConfgMode3="3 - Schedule an archive at another time\n"
applyTemplateMode1="1 - Force an apply by manually adding devices\n"
applyTemplateMode2="2 - Force an apply by selecting devices from a numbered list\n"
applyTemplateMode3="3 - Schedule an apply at another time\n"
archiveConfgMode1Main="""
Currently, the module is asking for the hostname of the device that will be archived.
Hostnames can be entered in a comma separated list or one at a time. 

After entering the hostnames desired, type end to continue. The program will prompt for a username and
secure password. It will then login to each device and run a predetermined set of commands and export the configs
to the local tftp server. It will also create a file containing the difference of the running config and the
startup config and alert if there is a difference. This program is located in sshTest/exportConfgNew.py
"""
applyTemplateMode1Main="""
Currently, the module is asking for the hostname of the device that will have the selected template applied.
Hostnames can be entered in a comma separated list or one at a time.

After entering the desired hostnames, type end to continue. The program will prompt for a username and secure
password. It will then login to each device and run a prewritten set of commands and first export the configs
to the local tftp server, doing the basic archiving. It will then run through another prewritten set of 
commands, and if it fails at any point it will rollback the changes made.
"""
archiveConfgMode1End="end - starts the archive for the typed devices\n"
applyTemplateMode1End="end - starts the apply for the typed devices\n"
archiveConfgMode1Enter="*enter* - returns the program to the mode selection screen\n"
archiveConfgMode2Main="""
Currently, the module is presenting a list of the devices in the device directory.
By typing in the number corresponding to the listed device, the device will be added to the archive.

After going through all pages or typing end, the program will prompt for a username and secure password.
This is used to login and archive the current and running configs. Each device is then entered using a
predetermined set of commands and the configs are exported to the local TFTP server. It will also create
a file containing the difference of the running config and the startup config and alert if there is a difference.
This program is located in sshTest/exportConfgNew.py
"""
applyTemplateMode2Main="""
Currently, the module is presenting a list of devices in the device directory.
By typing in the number corresponding to the listed device, the device will have the template applied to it.

After going through all pages or typing end, the program will prompt for a username and secure password.
This is used to login and apply the templates. Each devices is entered using a preset list of commands and the
configs are archived and the templates are then applied. If it fails it archives the configs and rollsback the
changes.
"""
archiveConfgMode2Next="next - Moves to the next page on the list of devices\n"
archiveConfgMode2End="end - Stops showing devices and starts the archive\n"
applyTemplateMode2End="end - Stops showing devices and starts applying the template\n"
archiveConfgMode2Num="*number* - adds the device corresponding to that number on the list\n"
selectionWeekdayMain="""
Currently the module is asking to type the number corresponding to the day of the week the scheduled task
will run on. If the day has already been added it will reject the day.
"""
selectionWeekdayNum="*number* - adds the day corresponding to that number (1-7, 1 being Sunday and 7 being Saturday)\n"
selectionWeekdayAll="all - adds every weekday to the task\n"
selectionMonthMain="""
Currently the module is asking to type the number corresponding to the month the schedule task will run in. If
the month has already been added it will not add it.
"""
selectionMonthAll="all - adds every month to the task\n"
selectionMonthNum="*number* - adds the month corresponding to that number (1-12, 1 being January and 12 being December)\n"
selectionDayMain="""
Currently the module is asking to type the number corresponding to the day of the month the schedule will run on.
If the day has already been added the program will not add it again.
"""
selectionDayAll="all - adds every day to the task\n"
selectionDayNum="*number* - adds the day corresponding to that number (1-31)\n"
selectionHourMain="""
Currently the module is asking to type the hour that the scheduled task will start on. The time is set on UTC-0,
so EDT+4 and EST+5. If the hour has already been added it will not be added again.
"""
selectionHourAll="all - adds every hour to the task\n"
selectionHourNum="*number* - adds the hour corresponding to that number (0-23)\n"
selectionMinuteMain="""
Currently the module is asking to type the minute that the scheduled task will start on. So the scheduled task will
run on the minute of the hours selected previously. If the minute has already been added it will not be added again.
"""
selectionMinuteAll="all - adds every minute to the task\n"
selectionMinuteNum="*number* - adds the minute corresponding to that number (0-59)\n"
clear="clear - clears the terminal of all text"
selectionChangeMain="""
Currently the module is asking for what setting needs to be changed. Anything set to be changed will overwrite the 
current contents. Press to continue and change the specified settings.
"""
selectionChangeNum="*number* - adds the corresponding setting to the list of settings to be changed.\n"
selectionSelectionType="""
This screen is prompting for a way of selecting devices. Type device names allows for manually entering a comma
separated list of devices (device1,device2,...), and select devices will create a list that will cycle through the
list of devices.
"""
selectionSelectionType1="""
Currently, the module is asking for a list of devices. Entering each device individually or comma separated are both
possible. Type end when you are finished entering devices.

After entering devices, the program will prompt for a username and password so that the scheduled task has the
permissions required to run.
"""
selectionSelectionType2="""
Currently, the module is showing a list of devices that can be selected by typing the number corresponding to that
device. Typing next will go to the next page of devices, and typing end will finish selecting devices and add the 
scheduled task with those devices to the local crontab.

After entering the devices, the program will prompt for a username and password so that the scheduled task has the
permissions required to run.
"""
selectionSelectionTypeEnd="end - starts the program for the selected devices\n"
createNewMain="""
This module is used to create new templates to be used for applying to Cisco devices.

Currently, the module is asking for the device name (ex. 2960-CX). This is so that when it creates the new template,
it will be placed under that device.
"""
createNewName="""
Currently, the module is asking for a template name. This is so it knows what the file will be called.
The module will name the template "name".template
"""
createNewEnter="*enter* - returns the program to the device choice\n"
txt="""
Currently, the module is asking you to choose a text editor. Each have differences between them.
"""
viewOrModifyOldRunnerMain="""
This module is used to view and modify templates. 

Currently the module is prompting to choose a device that the template is listed under.
"""
viewOrModifyOldRunnerName="*name* - selects the named device\n"
viewOrModifyOldMain="""
Currently, the module is prompting to choose a template to view or modify.
"""
viewOrModifyOldName="*name* - selects the named template\n"
viewOrModifyOldEnter="*enter* - returns to the device selection page\n"

def getAddDeviceMain(): return addDeviceMain
def getAddDeviceDevice(): return addDeviceDevice
def getCmdList(): return cmdList
def getEnter1(): return enter1
def getExit(): return exit
def getQuit(): return quit
def getAddDeviceIP(): return addDeviceIP
def getAddDeviceEnter2(): return addDeviceEnter2
def getAddDeviceDeviceName(): return addDeviceDeviceName
def getLookupDeviceMain(): return lookupDeviceMain
def getLookupDeviceIP(): return lookupDeviceIP
def getLookupDeviceDevice(): return lookupDeviceDevice
def getLookupDeviceSearch(): return lookupDeviceSearch
def getArchiveConfgMain(): return archiveConfgMain
def getArchiveConfgMode(): return archiveConfgMode
def getArchiveConfgMode1(): return archiveConfgMode1
def getArchiveConfgMode2(): return archiveConfgMode2
def getArchiveConfgMode3(): return archiveConfgMode3
def getArchiveConfgMode1Main(): return archiveConfgMode1Main
def getArchiveConfgMode1Enter(): return archiveConfgMode1Enter
def getArchiveConfgMode2Main(): return archiveConfgMode2Main
def getArchiveConfgMode2Next(): return archiveConfgMode2Next
def getArchiveConfgMode2End(): return archiveConfgMode2End
def getArchiveConfgMode2Num(): return archiveConfgMode2Num
def getClear(): return clear
def getSelectionWeekdayMain(): return selectionWeekdayMain
def getSelectionWeekdayAll(): return selectionWeekdayAll
def getSelectionWeekdayNum(): return selectionWeekdayNum
def getSelectionMonthMain(): return selectionMonthMain
def getSelectionMonthAll(): return selectionMonthAll
def getSelectionMonthNum(): return selectionMonthNum
def getSelectionDayMain(): return selectionDayMain
def getSelectionDayAll(): return selectionDayAll
def getSelectionDayNum(): return selectionDayNum
def getSelectionHourMain(): return selectionHourMain
def getSelectionHourAll(): return selectionHourAll
def getSelectionHourNum(): return selectionHourNum
def getSelectionMinuteMain(): return selectionMinuteMain
def getSelectionMinuteAll(): return selectionMinuteAll
def getSelectionMinuteNum(): return selectionMinuteNum
def getSelectionChangeMain(): return selectionChangeMain
def getSelectionSelectionType(): return selectionSelectionType
def getSelectionSelectionType1(): return selectionSelectionType1
def getSelectionSelectionType2(): return selectionSelectionType2
def getSelectionChangeNum(): return selectionChangeNum
def getSelectionSelectionTypeEnd(): return selectionSelectionTypeEnd
def getApplyTemplateMode(): return applyTemplateMode
def getApplyTemplateMode1(): return applyTemplateMode1
def getApplyTemplateMode2(): return applyTemplateMode2
def getApplyTemplateMode3(): return applyTemplateMode3
def getApplyTemplateMode1Main(): return applyTemplateMode1Main
def getApplyTemplateMode1End(): return applyTemplateMode1End
def getCreateNewMain(): return createNewMain
def getCreateNewName(): return createNewName
def getCreateNewEnter(): return createNewEnter
def getTxt(): return txt
def getViewOrModifyOldRunnerMain(): return viewOrModifyOldRunnerMain
def getViewOrModifyOldRunnerName(): return viewOrModifyOldRunnerName
def getViewOrModifyOldMain(): return viewOrModifyOldMain
def getViewOrModifyOldName(): return viewOrModifyOldName
def getViewOrModifyOldEnter(): return viewOrModifyOldEnter
