import pexpect
#enable
# copy flash:CONFIG3 running-config
#show run | section line vty
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8',
timeout=20)
results = session.expect(['Username:', pexpect.TIMEOUT])

if results != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering username: ', username)
    exit()
# Session is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()
# Display a success message if it works
print('------------------------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
print('')
print('------------------------------------------------------')
session.sendline('quit')
session.close()