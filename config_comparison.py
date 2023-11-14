#import the libraries that are used 
import netmiko 
import getpass
import difflib

def ssh(): # defines the function for ssh router 
    from netmiko import ConnectHandler
    iosv_l2 = { # define the parameter to connect to the router 
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.101', #ip address 
    'username' : 'cisco', # routers username 
    'password' : ''
    }
    iosv_l2['password'] = getpass.getpass("Enter password:") # hides the password when typed and don't store it in varible 
    
    net_connect = ConnectHandler(**iosv_l2)   
    command = ["exit","show ip int brief",'enable','config t','hostname R1']#  set of commands that are given to the router. it starts of in config t
    
    config = net_connect.send_config_set(command)
    print(config) # print the 
    file = open("config_setup_ssh.txt", "w")
    file.write(config)
    config_setup()
    return(net_connect)

def telenet():

    from netmiko import ConnectHandler
    
    iosv_l2 = {
        'device_type' : 'cisco_ios_telnet',
        'ip' : '192.168.56.101',
        'username' : 'cisco',
        'password' : '' #cisco123!
    }
    iosv_l2['password'] = getpass.getpass("Enter password:")
    net_connect = ConnectHandler(**iosv_l2)
    
    command = ["exit","show ip int brief",'enable','config t','hostname R1']
    config = net_connect.send_config_set(command)
    print(config)
    file = open("config_setup_telnet.txt", "w")
    file.write(config)
    config_setup()
    return (net_connect)
def config_setup(net_connect):
    from netmiko import ConnectHandler
    from difflib import unified_diff
    #command = input("please enter a command") # show archive config differences 
    running_config = net_connect.send_commannd("show running-config")
    file = open("config_running.txt", "w")
    file.write(running_config)
    start_config = net_connect.send_commannd("show startup-config")
    file = open("startup_running.txt", "w")
    file.write(start_config)
    if running_config == start_config:
        print("the running config is the same as the starting configuration")
    else:
        print("the file are different and here are the difference")
        diff = unified_diff(start_config.splitlines(), running_config.splitlines())
        print('\n'.join(diff))
    
    

option = input("which way would you like to access the router:\nPress 1 for ssh or press 2 for telnet:\n")
if option == "1":
    ssh()
    config_setup()
elif option =="2":
    telenet()
    config_setup()

else:
    print("please press 1 or 2")


