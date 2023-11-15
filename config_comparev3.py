import netmiko 
import getpass
from difflib import unified_diff

def ssh():
    from netmiko import ConnectHandler
    
    iosv_l2 = {
        'device_type' : 'cisco_ios',
        'ip' : '192.168.56.101',
        'username' : 'cisco',
        'password' : ''
    }
    iosv_l2['password'] = getpass.getpass("Enter password:")
    
    net_connect = ConnectHandler(**iosv_l2)   
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']
    
    config = net_connect.send_config_set(command)
    print(config)
    
    file = open("config_setup_ssh.txt", "w")
    file.write(config)
    
    return net_connect

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
    
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']
    config = net_connect.send_config_set(command)
    print(config)
    
    file = open("config_setup_telnet.txt", "w")
    file.write(config)
    
    return net_connect

def config_setup(net_connect):
    running_config = net_connect.send_command("show running-config")
    file = open("config_running.txt", "w")
    file.write(running_config)
    
    start_config = net_connect.send_command("show startup-config")
    file = open("config_startup.txt", "w")  # Change the file name
    file.write(start_config)
    
    if running_config == start_config:
        print("The running config is the same as the starting configuration")
    else:
        print("The files are different, and here are the differences:")
        diff = list(unified_diff(start_config.splitlines(), running_config.splitlines()))
        for line in diff:
            if line.startswith("+") or line.startswith("-"):
                print(line)

option = input("Which way would you like to access the router:\nPress 1 for SSH or press 2 for Telnet:\n")
if option == "1":
    net_connect = ssh()
    config_setup(net_connect)
elif option == "2":
    net_connect = telenet()
    config_setup(net_connect)
else:
    print("Please press 1 or 2")



