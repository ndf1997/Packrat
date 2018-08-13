import paramiko
import time
from time import strftime
import os
import sys

class exportConfg(object):
	OutMAX=65535
	path=" "
	def __init__(self, ip, username, password, pushOrPull, device):
		self.ip=ip
		self.username=username
		self.password=password
		self.pushOrPull=pushOrPull
		self.currentTime=strftime("%H%M.")
		self.date=strftime("%m%d%Y")
		self.device=device
		self.ssh=paramiko.SSHClient()
		self.remote=None
	def connect(self):
		response = os.system("ping -c 1 " + self.ip)
		if response==0:
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(self.ip, username=self.username, password=self.password, look_for_keys=False, allow_agent=False)
			self.remote=self.ssh.invoke_shell()
			time.sleep(3)
			output=self.remote.recv(65535)
			self.remote.send("\n")
			time.sleep(1)
			self.device=self.remote.recv(2000)
			if self.device.count('>')==1:
				self.device=self.device.split('>')[0]
			elif self.device.count('#')==1:
				self.device=self.device.split('#')[0]
			self.device=self.device[2:]
		else:
			print "Ping unsuccessful"
	def mkdir(self):
		if self.pushOrPull==True:
			path="/home/cheti/tftp/archive/"
			if not os.path.exists(path+self.date):
				os.mkdir(path+self.date)
				os.chmod(path+self.date,0777)
			if not os.path.exists(path+self.date+"/"+self.device):
				os.mkdir(path+self.date+"/"+self.device)
				os.chmod(path+self.date+"/"+self.device,0777)
			path = "/home/cheti/tftp/archive/"+self.date+"/"+self.device
		else:
			path="/home/cheti/tftp/templates/"
			if not os.path.exists(path+self.date):
				os.mkdir(path+self.date)
				os.chmod(path+self.date,0777)
			if not os.path.exists(path+self.date+"/"+self.device):
				os.mkdir(path+self.date+"/"+self.device)
				os.chmod(path+self.date+"/"+self.device, 0777)
			if not os.path.exists(path+self.date+"/"+self.device+"/"+"Backups"):
				os.mkdir(path+self.date+"/"+self.device+"/Backups")
				os.chmod(path+self.date+"/"+self.device+"/Backups", 0777)
				os.mkdir(path+self.date+"/"+self.device+"/PostrunConfigs")
				os.chmod(path+self.date+"/"+self.device+"/PostrunConfigs",0777)
				os.mkdir(path+self.date+"/"+self.device+"/ErroredConfigs")
				os.chmod(path+self.date+"/"+self.device+"/ErroredConfigs",0777)
			path="/home/cheti/tftp/templates/"+self.date+"/"+self.device
	def export(self, post, failed):
		runName = self.currentTime+self.device+"-running-confg"
		startName= self.currentTime+self.device+"-startup-confg"
		otherPath=" "
		if self.pushOrPull==True:
			path="archive/"+self.date+"/"+self.device+"/"
			otherPath="tftp/archive/"+self.date+"/"+self.device+"/"
		else:
			if post==True:
				path="templates/"+self.date+"/"+self.device+"/PostrunConfigs/"
				otherPath="tftp/templates/"+self.date+"/"+self.device+"/PostrunConfigs/"
			else:
				if failed==True:
					path="templates/"+self.date+"/"+self.device+"/ErroredConfigs/"
					otherPath="tftp/templates/"+self.date+"/"+self.device+"/ErroredConfigs/"
				else:
					path="templates/"+self.date+"/"+self.device+"/Backups/"
					otherPath="tftp/templates/"+self.date+"/"+self.device+"/Backups/"
		self.remote.send("copy running-config tftp://192.168.78.100/"+path+runName+"\n")
		time.sleep(1)
		output=self.remote.recv(5000)
		self.remote.send("\n")
		time.sleep(1)
		output=self.remote.recv(5000)
		self.remote.send("\n")
		time.sleep(2)
		output=self.remote.recv(5000)
		self.remote.send("copy startup-config tftp://192.168.78.100/"+path+startName+"\n")
		time.sleep(1)
		output=self.remote.recv(5000)
		self.remote.send("\n")
		time.sleep(1)
		output=self.remote.recv(5000)
		self.remote.send("\n")
		time.sleep(2)
		output=self.remote.recv(5000)
		self.remote.send("exit\n")
		time.sleep(1)
		newName=self.currentTime+self.device
		os.system("diff "+otherPath+startName+" "+otherPath+runName+" > "+otherPath+"diff."+newName+".txt")
		end=""
		with open(otherPath+"diff."+newName+".txt","r+") as f:
			diff=""
			while True:
				line=f.readline()
				if not line:break
				diff+=line
			confgChange=diff.split("ciscoadm")
			rest="".join(confgChange[len(confgChange)-1:])
			certificate=rest[rest.index("certificate")-12:rest.index("quit")+4]
			removal="".join(rest.split(certificate))
			end="\n".join(removal.split("\n")[2:])
		os.system("rm "+otherPath+"diff."+newName+".txt")
		f=open(otherPath+"diff."+newName+".txt","w+")
		f.write(end)
		f.close()
if len(sys.argv)==5 and sys.argv[1]!="new" and sys.argv[1]!="add" and sys.argv[1]!="search" and sys.argv[1]!="apply" and sys.argv[1]!="view":
	print sys.argv
	export=exportConfg(ip=sys.argv[3],username=sys.argv[1],password=sys.argv[2],pushOrPull=True,device=sys.argv[4])
	export.connect()
	export.mkdir()
	export.export(False, False)
