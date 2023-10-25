import pexpect

ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'
session = pexpect.spawn('ssh ' + username + '@' + ip_address,encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
# Session expecting password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
 print('--- Failure! entering enable mode')
 exit()
# Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering enable mode after sending password')
    exit()
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! setting hostname')
# Exit config mode
session.sendline('exit')
# Exit enable mode
session.sendline('exit')
# Display a success message if works
print('------------------------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
print('')
print('------------------------------------------------------')
