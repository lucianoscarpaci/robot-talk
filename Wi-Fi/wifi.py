import subprocess
import sys


class WiFi:

    def __init__(self):
        pass

    def ip_forward(self):
        subprocess.run(
            ['sysctl', '-w', 'net.ipv4.ip_forward=1'])

    def masquerade_nano_traffic(self):
        subprocess.run(['iptables', '-t', 'nat', '-A',
                       'POSTROUTING', '-o', 'wlan2', '-j', 'MASQUERADE'])
        subprocess.run(['iptables', '-A', 'FORWARD', '-i',
                       'eth0', '-o', 'wlan2', '-j', 'ACCEPT'])
        subprocess.run(['iptables', '-A', 'FORWARD', '-i', 'wlan2', '-o', 'eth0',
                       '-m', 'state', '--state', 'RELATED,ESTABLISHED', '-j', 'ACCEPT'])
        subprocess.run(['ifconfig', 'wlan2', 'up'])

    def remove_default_gateway(self):
        subprocess.run(['ip', 'r', 'd', 'default', 'via', '192.168.123.1'])
        subprocess.run(['ip', 'r', 'd', 'default', 'via', '192.168.12.1'])

    def begin_stage1(self):
        print("\033[92mStage 1 is about to start...\033[0m")
        # Allow forwarding on the raspberry pi
        print("\033[92mEnabling port forwarding on the Pi...\033[0m")
        try:
            self.ip_forward()

        except Exception:
            print("\033[91mIP forwarding Failed.\033[0m")
        else:
            print("\033[92mIP forwarding enabled.\033[0m")
        print("\033[92mPutting all nano traffic behind the Pi...\033[0m")
        try:
            self.masquerade_nano_traffic()
        except Exception:
            print("\033[91mPutting nano traffic behind the Pi Failed.\033[0m")
        else:
            print("\033[92mAll nano traffic is behind the Pi.\033[0m")
        print("\033[92mRemoving default gateway...\033[0m")
        try:
            self.remove_default_gateway()
        except Exception:
            print("\033[91mRemoving default gateway Failed.\033[0m")
        else:
            print("\033[92mDefault gateway removed.\033[0m")

    def begin_stage2(self):
        print("Stage 2 has been selected")

    def start(self):
        while True:
            dog_wifi_ascii = '''
		                / \__
		               (    @\___
		               /         O
		              /   (_____/
		             /_____/
		            / ______\\
		         /",/|  ( )) |\\
		        /   / |   +--+  \\          
		           /  \|/  |  |
		          /__\__/___|
		    '''

            # Printing the ASCII art
            print("\033[94m" + dog_wifi_ascii + "\033[0m")
            print(
                "\033[94m+++++++++++++++++++++ Dog WiFi +++++++++++++++++++++\033[0m")
            stage = input(
                "\033[92mWhich WiFi stage are you in? (1 or 2):\033[0m")

            if stage == "1":
                self.begin_stage1()
                break
            elif stage == "2":
                self.begin_stage2()
                break
            elif stage == "exit":
                sys.exit()
            else:
                print("\033[91mError: wrong input. Type '1' or '2' \033[0m")
                print(
                    "\033[94m+++++++++++++++++++++ Dog WiFi +++++++++++++++++++++\033[0m")


wifi = WiFi()
wifi.start()
