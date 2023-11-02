#import the libraries that are used 
import netmiko 
import getpass
def ssh(): # defines the function for ssh router 
    from netmiko import ConnectHandler
    iosv_l2 = { # define the parameter to connect to the router 
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.101', #ip address 
    'username' : 'cisco', # routers username 
    'password' : ''
    }
    iosv_l2['password'] = getpass.getpass("Enter password:") # hides the password when typed and don't store it in varible 
    
    net_connect = ConnectHandler(**iosv_l2)    command = ["exit","show ip int brief",'enable','config t','hostname R1']#  set of commands that are given to the router. it starts of in config t
    
    config = net_connect.send_config_set(command)
    print(config) # print the 
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
