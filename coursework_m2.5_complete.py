# Import the libraries that are used
import netmiko
import getpass
import difflib
import os
from netmiko import ConnectHandler

def ssh():  # Defines the function for SSH router
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.56.101',  # IP address
        'username': 'cisco',  # Router's username
        'password': getpass.getpass("Enter password:")  # Hides the password when typed
    }

    net_connect = ConnectHandler(**iosv_l2)
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']  # Set of commands for the router
    config = net_connect.send_config_set(command)
    print(config)
    with open("config_setup_ssh.txt", "w") as file:
        file.write(config)
    config_setup(net_connect)
    return net_connect

def telenet():  # Defines the function for Telnet
    iosv_l2 = {
        'device_type': 'cisco_ios_telnet',
        'ip': '192.168.56.101',
        'username': 'cisco',
        'password': getpass.getpass("Enter password:")
    }

    net_connect = ConnectHandler(**iosv_l2)
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']
    config = net_connect.send_config_set(command)
    print(config)
    with open("config_setup_telnet.txt", "w") as file:
        file.write(config)
    config_setup(net_connect)
    return net_connect

def config_setup(net_connect):
    running_config = net_connect.send_command("show running-config")
    with open("config_running.txt", "w") as file:
        file.write(running_config)
    start_config = net_connect.send_command("show startup-config")
    with open("startup_config_running.txt", "w") as file:
        file.write(start_config)
    
    if running_config == start_config:
        print("The running config is the same as the starting configuration")
    else:
        print("The files are different, and here are the differences:")
        diff = list(difflib.unified_diff(start_config.splitlines(), running_config.splitlines()))
        for line in diff:
            if line.startswith("+") or line.startswith("-"):
                print(line)

def compare_config(net_connect):
    directory = os.path.dirname(os.path.abspath(__file__))  # Search for files in the same directory as the Python file
    files = os.listdir(directory)
    config_files = [x for x in files if "config" in x]

    for y, file in enumerate(config_files):
        print(f"{y + 1}: {file}")
    choice = int(input("Enter which of the selected files you would like to compare: "))
    selected_file = config_files[choice - 1]

    with open(selected_file, 'r') as file:
        selected_config = file.read()
    current_config = net_connect.send_command("show running-config")

    if current_config == selected_config:
        print("The current config has no changes compared to the selected file.")
    else:
        print("Here are the differences in the files:")
        diff = unified_diff(current_config.splitlines(), selected_config.splitlines())
        for line in diff:
            if line.startswith("+") or line.startswith("-"):
                print(line)

# Main script
option = input("Which way would you like to access the router:\nPress 1 for SSH or press 2 for Telnet:\n")
if option == "1":
    net_connect = ssh()
    config_setup(net_connect)
elif option == "2":
    net_connect = telenet()
    config_setup(net_connect)
elif option == "3":
    net_connect = ssh()  # Or telenet(), depending on your requirement
    compare_config(net_connect)
else:
    print("Please press one of the options")
