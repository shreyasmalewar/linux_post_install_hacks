#opening /etc/os/release

f = open('/etc/os-release', 'r')
os_details = f.read()
print(os_details)