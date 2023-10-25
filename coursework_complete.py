import netmiko
import getpass
def ssh():
    from netmiko import ConnectHandler
    iosv_l2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.101',
    'username' : 'prne',
    'password' : 'cisco123!'
    }
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command("show ip int brief")#
    print(output)
def telenet():

    from netmiko import ConnectHandler
    iosv_l2 = {
        'device_type' : 'cisco_ios_telenet',
        'ip' : '192.168.56.101',
        'username' : 'cisco',
        'password' : 'cisco123!'
    }
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command("show ip int brief")#
    print(output)

option = input("which way would you like to access the router:\nPress 1 for telenet or press 2 for SSH:\n")
if option == 1:
    ssh()
elif option ==2:
    telenet()
else:
    print("please press 1 or 2")
