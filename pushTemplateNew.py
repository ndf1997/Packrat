import paramiko
import time
from time import strftime
import os
import exportConfgNew
import sys

class pushTemplate:
	MAX=65535
	def __init__(self, ip, username, password, device, fileLocation,path):
		self.ip=ip
		self.username=username
		self.password=password
		self.ssh=paramiko.SSHClient()
		self.device=device
		self.remote=None
		self.fileLocation=fileLocation
		self.path=path
		self.currentTime=strftime("%H%M.")
		self.date=strftime("%m%d%Y")
	def connect(self):
		response = os.system("ping -c 1 " +self.ip)
		if response==0:
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(self.ip, username=self.username, password=self.password, look_for_keys=False, allow_agent=False)
			self.remote=self.ssh.invoke_shell()
			time.sleep(3)
			output=self.remote.recv(65535)
		else:
			print "Ping unsuccessful"
	def apply(self):
		i=0
		with open(self.fileLocation, "r") as f:
			while True:
				line=f.readline()
				if not line: break
				self.remote.send(line)
				i+=1
				if i==10:
					time.sleep(1)
					output=self.remote.recv(65536)
					if output.count('%')>=1:
						message=output.split('%')
						templateCode=message[0]
						temp=message[1]
						print temp
						error="%"+temp[:temp.index("\n")]
						templateCode=templateCode+error
						if not os.path.exists(self.path+"errors"):
							os.mkdir(self.path+"errors")
							os.chmod(self.path+"errors",0777)
						if not os.path.exists(self.path+"errors/"+self.date+"/"):
							os.mkdir(self.path+"errors/"+self.date)
							os.chmod(self.path+"errors/"+self.date,0777)
						text_file=open(self.path+"errors/"+self.date+"/"+self.currentTime+"error.txt", "w+")
						text_file.write(templateCode)
						text_file.close()
						self.remote.send("end\n")
						export=exportConfgNew.exportConfg(ip=self.ip, username=self.username, password=self.password, pushOrPull=False, device=self.device)
						export.connect()
						export.mkdir()
						export.export(post=False, failed=True)
						self.remote.send("configure replace nvram:startup-config force\n")
						time.sleep(5)
						self.remote.send("exit\n")
						return
					else:
						i=0
		export=exportConfgNew.exportConfg(ip=self.ip, username=self.username, password=self.password, pushOrPull=False, device=self.device)
		export.connect()
		export.mkdir()
		export.export(post=True, failed=False)
		self.remote.send("exit\n")
if len(sys.argv)==7 and sys.argv[1]!="add" and sys.argv[1]!="search" and sys.argv[1]!="archive" and sys.argv[1]!="new" and sys.argv[1]!="view":
	export=exportConfgNew.exportConfg(ip=sys.argv[3], username=sys.argv[1], password=sys.argv[2], pushOrPull=False, device=sys.argv[4])
	export.connect()
	export.mkdir()
	export.export(False, False)
	apply=pushTemplate(ip=sys.argv[3], username=sys.argv[1], password=sys.argv[2], device=sys.argv[4], fileLocation=sys.argv[5], path=sys.argv[6])
	apply.connect()
	apply.apply()
