import netmiko, getpass,difflib,os
from netmiko import ConnectHandler
def connection():
    connection_option = input("Do you want to connect via SSH or Telnet? ").lower()
    if connection_option == "ssh":
        device_type = "cisco_ios"
    elif connection_option == "telnet":     
        device_type = "cisco_ios_telnet"
    elif connection_option == "test":
        iosv_l2 = {
            'device_type': 'cisco_ios',
            'ip': '192.168.56.101',  # IP address of the router
            'username': 'cisco',     # Router's username
            'password': 'cisco123!', # Example password
        }

        net_connect = ConnectHandler(**iosv_l2)
        menu(net_connect)
    
    else:
        print("Please enter a valid response.")
        connection()
        return

    if connection_option != "test":
        while True:
            try:
                iosv_l2 = {
                    'device_type': device_type,
                    'ip': '192.168.56.101',  # IP address of the router
                    'username': 'cisco',     # Router's username
                    'password': getpass.getpass("Enter password:")  # password is hidden when entered
                }
                net_connect = ConnectHandler(**iosv_l2)
                menu(net_connect)
                break  # Exit the loop if connection is successful
            except Exception as e:
                print("Authentication failed:", e)
    return(net_connect)
def config_setup(net_connect): ## need to sort out files. 
    start_config = net_connect.send_command("show startup-config")
      # varible to store commands 
    command = ["exit", "show ip int brief", 'enable', 'config t', 'hostname R1']

    # Sends commands to the router and saves the output
    config = net_connect.send_config_set(command)
    print("command has been sent")

    # Writing the output to a file
    with open("config_setup.txt", "w") as file:
       file.write(config)
    with open("config_setup.txt", "w") as file:
      file.write(start_config)
    
    running_config = net_connect.send_command("show running-config")
    with open("config_running.txt", "w") as file:
        file.write(running_config)
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
    menu()
def advance_setup(net_connect):
    option = input("which of the folowing would you like to setup 1.Loopback 2. OSPF   3.EIGRP 4. RIP \n ")
    loop = True
    while loop == True:
        if option == "1":
            keyword = "loopback"
            loop = False
        if option == "2":
            keyword = "OSPF"
            loop = False
        if option == "3":
            keyword = "EIGRP"
            loop = False
        if option == "3":
            loop = False
            keyword = "EIGRP"
        else:
            print("please enter a valid number")
                  
    start_reading = False 
    command = []             
    with open("commands.txt", 'r') as file: # this code the txt file commands.txt then does though the file line by line looking for the keyword then saves the commands as commands 
        for line in file:
            if line.strip() == f"# {keyword}":
                start_reading = True
                continue
            if start_reading:
                if line.startswith("#"): # if # is detected it stops `      `
                    break
                command.append(line.strip())
   
    config = net_connect.send_config_set(command)
    print (command," have been sent to the route and here is the output" , config)
    menu()
def menu(net_connect):
    option = input("Welcome\n Now that you have connect which of the following option would you to do.\n 1) set up the router basic\n 2) Compare the configuations\n 3) advanced setup ")
    if option == "1":
        config_setup(net_connect)
    elif option == "2":
        compare_config(net_connect)
    elif option == "3":
        advance_setup(net_connect)
    else:
        print("please enter 1,2 or 3")
        menu()
    

connection()
