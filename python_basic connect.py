import netmiko
import getpass
from netmiko import ConnectHandler
iosv_l2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.101',
    'username' : 'prne',
    'password' : 'cisco123'
}
net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command("show ip int brief")#
print(output)
