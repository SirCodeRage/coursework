import netmiko
import getpass
from netmiko import ConnectHandler
password = getpass.getpass(prompt = "enter password") 
iosv_l2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.101',
    'username' : 'prne',
    'password' : password,
}
net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command("show ip int brief")#
command= 
print(output)
