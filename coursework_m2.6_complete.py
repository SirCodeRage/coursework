# Import all the required libraries
import netmiko
import getpass
import difflib
import os
from netmiko import ConnectHandler

# Function to establish SSH connection to router
def ssh():
    # imformation to pass to the route to all to convect
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.56.101',  # IP address of the router
        'username': 'cisco',     # Router's username
        'password': getpass.getpass("Enter password:")  # password is hidden when entered 
    }

    # Establishing the SSH connection
    net_connect = ConnectHandler(**iosv_l2)

    # varible to store commands 
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']

    # Sends commands to the router and saves the output
    config = net_connect.send_config_set(command)
    print(config)

    # Writing the output to a file
    with open("config_setup_ssh.txt", "w") as file:
        file.write(config)

    # excute the config_setup def while passing the net_connect varible 
    config_setup(net_connect)
    return net_connect

# Function to establish Telnet connection to a router
def telenet():
    # Router connection parameters for Telnet
    iosv_l2 = {
        'device_type': 'cisco_ios_telnet',
        'ip': '192.168.56.101',
        'username': 'cisco',
        'password': getpass.getpass("Enter password:")
    }

    # Establishing the Telnet connection
    net_connect = ConnectHandler(**iosv_l2)

     # varible to store commands 
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']

    config = net_connect.send_config_set(command)
    print(config)

    # Writing the output to a file
    with open("config_setup_telnet.txt", "w") as file:
        file.write(config)

    # excute the config_setup def while passing the net_connect varible 
    config_setup(net_connect)
    return net_connect

# Function to compare running and startup configurations of the router
def config_setup(net_connect):
    # Fetchs the running config
    running_config = net_connect.send_command("show running-config")

    # Writing running configation to a text file
    with open("config_running.txt", "w") as file:
        file.write(running_config)

    # Fetchs startup configuration
    start_config = net_connect.send_command("show startup-config")

    # Writing startup configuration to a texy file
    with open("startup_config_running.txt", "w") as file:
        file.write(start_config)

    # Compares the running config and the start config and prints the differences 
    if running_config == start_config:
        print("The running config is the same as the starting configuration")
    else:
        print("The files are different, and here are the differences:")
        diff = list(difflib.unified_diff(start_config.splitlines(), running_config.splitlines()))
        for line in diff:
            if line.startswith("+") or line.startswith("-"):
                print(line)

# Function compares  the current configuration with a selected local config file
def compare_config(net_connect):
    # finds all the config files saved in the same directory as the program 
    directory = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(directory)
    config_files = [x for x in files if "config" in x]

    # Displays the configuration files and allows user to choice 
    for y, file in enumerate(config_files):
        print(f"{y + 1}: {file}")
    choice = int(input("Enter which of the selected files you would like to compare: "))
    selected_file = config_files[choice - 1]

    # opens selected file as read only and saves to selected varible 
    with open(selected_file, 'r') as file:
        selected_config = file.read()

    # gets the current configuation and save it 
    current_config = net_connect.send_command("show running-config")

    # Comparing current configuration with the selected file
    if current_config == selected_config:
        print("The current config has no changes compared to the selected file.")
    else:
        print("Here are the differences in the files:")
        diff = difflib.unified_diff(current_config.splitlines(), selected_config.splitlines())
        for line in diff:
            if line.startswith("+") or line.startswith("-"):
                print(line)

# Main script execution starts here
option = input("Which way would you like to access the router:\nPress 1 for SSH or press 2 for Telnet Or 3 for comparison:\n")
if option == "1":
    net_connect = ssh()  # Establish SSH connection and proceed
    config_setup(net_connect)
elif option == "2":
    net_connect = telenet()  # Establish Telnet connection and proceed
    config_setup(net_connect)
elif option == "3":
    net_connect = ssh()  # Establish SSH connection and compare configurations
    compare_config(net_connect)
else:
    print("Please press one of the options")  # Prompt for correct input if none of the valid options are chosen
  
