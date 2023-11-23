#file "/home/devasc/Downloads/coursework_m2.5_complete (1).py", line 51, in config_setup
#    running_config = net_connect.send_command("show running-config")
#AttributeError: 'str' object has no attribute 'send_command'
#import the libraries that are used 
#import the libraries that are used 
import netmiko 
import getpass
import difflib
import os 
net_connect = ""
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
    config_setup(net_connect)
    return net_connect

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
    config_setup(net_connect)
    return net_connect
def config_setup(net_connect):
    from netmiko import ConnectHandler
    from difflib import unified_diff
    #
    running_config = net_connect.send_command("show running-config")
    file = open("config_running.txt", "w")
    file.write(running_config)
    start_config = net_connect.send_command("show startup-config")
    file = open("startup_config_running.txt", "w")
    file.write(start_config)
    if running_config == start_config:
        print("the running config is the same as the starting configuration")
    else:
        print("the file are different and here are the difference")
        print("The files are different, and here are the differences:")
        diff = list(unified_diff(start_config.splitlines(), running_config.splitlines()))
        for line in diff:
            if line.startswith("+") or line.startswith("-"):
                print(line)
    
def compare_config(net_connect):
    from difflib import unified_diff
    directory = os.path.dirname(os.path.abspath(__file__)) # using the OS libary it is searching for files in the same directory as the python file is stored for the files that contain the word 'config'
    files = os.listdir(directory)
    config_files = [x for x in files if "config" in x]
    
    for y, file in enumerate(config_files):
        print(f"{y+1}: {file}")
    choice = int(input("Enter which of the select files you would like to compare: "))
    selected_file = config_files[choice - 1]

    with open(selected_file, 'r') as file:
        selected_config = file.read()
    current_config = net_connect.send_command("show running-config")

    if current_config == selected_config:
        print("The current config has no changes to the .")
    else:
        print("Here are the differents in the fies:")
        diff = unified_diff(current_config.splitlines(), selected_config.splitlines())
        for line in diff:
             if line.startswith("+") or line.startswith("-"):
                 print(line)
    



option = input("which way would you like to access the router:\nPress 1 for ssh or press 2 for telnet:\n")
if option == "1":
    ssh()
    config_setup(net_connect)
elif option =="2":
    telenet()
    config_setup(net_connect)
elif option == "3": 
    ssh()
    compare_config(net_connect)
else:
    print("please press one of the options")

