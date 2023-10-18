import paramiko
import time 
import getpass
host = "192.168.56.101" #the ip address of the route 
username = "prne"
password = "cisco123"

port = 8181
command = 'show ip interface brief \n'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host,username=username, password=password, port=port, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.readlines()
print(' '.join(map(str, output)))