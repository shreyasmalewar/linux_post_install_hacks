#opening /etc/os/release

import subprocess
import os

with open("/etc/os-release", "r") as f:
    for line in f.read().split("\n")[3:4:5]:
        os_name = line[8::]
        f.close()

print(os.getcwd())

debian_directory = '/home/shreyas/Documents/linux_post_install_hacks/Distros/Debian Based'
arch_directory   = '/home/shreyas/Documents/linux_post_install_hacks/Distros/Arch Based'
suse_directory   = '/home/shreyas/Documents/linux_post_install_hacks/Distros/SUSE Based'
redhat_directory = '/home/shreyas/Documents/linux_post_install_hacks/Distros/RedHat Based'

if os_name == 'ubuntu':
    subprocess.call([os.chdir(debian_directory), '0'], shell=True)

elif os_name == 'arch':
    subprocess.call([os.chdir(arch_directory), '0'], shell=True)

elif os_name == 'suse':
    subprocess.call([os.chdir(suse_directory), '0'], shell=True)

elif os_name == 'redhat':
    subprocess.call([os.chdir(redhat_directory), '0'], shell=True)



    



