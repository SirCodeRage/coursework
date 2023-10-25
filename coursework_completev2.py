import netmiko
import getpass
def ssh():
    from netmiko import ConnectHandler
    iosv_l2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.101',
    'username' : 'prne',
    'password' : ''
    }
    iosv_l2['password'] = getpass.getpass("Enter password:")
    net_connect = ConnectHandler(**iosv_l2)
    command = ["exit","show ip int brief",'enable','config t','hostname R1']
    config = net_connect.send_config_set(command)
    print(config)
    file = open("config_setup_ssh.txt", "w")
    file.write(config)
def telenet():

    from netmiko import ConnectHandler
    
    iosv_l2 = {
        'device_type' : 'cisco_ios_telnet',
        'ip' : '192.168.56.101',
        'username' : 'cisco',
        'password' : ''
    }
    iosv_l2['password'] = getpass.getpass("Enter password:")
    net_connect = ConnectHandler(**iosv_l2)
    
    command = ["exit","show ip int brief",'enable','config t','hostname R1']
    config = net_connect.send_config_set(command)
    print(config)
    file = open("config_setup_telnet.txt", "w")
    file.write(config)

option = input("which way would you like to access the router:\nPress 1 for ssh or press 2 for telnet:\n")
if option == "1":
    ssh()
elif option =="2":
    telenet()
else:
    print("please press 1 or 2")
