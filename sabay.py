##  Copy the linux command from http://remotedesktop.google.com/headless  ##
CRP1 = 'DISPLAY= /opt/google/chrome-remote-desktop/start-host --code="4/0AX4XfWhRKggHaGvxaW_ZSXbiPjVYcdj2VFu4zPNsDyovy6grKLnGM9TnJNzZLPOgKB2Pxw" --redirect-url="https://remotedesktop.google.com/_/oauthredirect" --name=$(hostname)'
Pin = 123456 ## rdp pin
Name = "RDP"    ## rdp name
import os,subprocess
username = "user" 
password = "root"
print("Creating User and Setting it up")
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
print("User Created and Configured")
CRP = CRP1.replace("$(hostname)",Name)
class CRD:
    def __init__(self):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        
        self.finish()
    @staticmethod
    def installCRD():
        print("Installing Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")
        os.system("wget https://raw.githubusercontent.com/jrkeiter/pika/main/ett.sh && chmod 777 ett.sh && bash ./ett.sh >/dev/null 2>&1")
    

    @staticmethod
    def finish():
        print("Finalizing")
        os.system(f"adduser {username} chrome-remote-desktop")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {username} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        print("Finished Succesfully")

try:
    if username:
        if CRP == "":
            print("Please enter authcode from the given link")
        elif len(str(Pin)) < 6:
            print("Enter a pin more or equal to 6 digits")
        else:
            CRD()
except NameError as e:
    print("username variable not found")
    print("Create a User First")
