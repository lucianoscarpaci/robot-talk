import subprocess
import sys


class WiFi:

    def __init__(self):
        pass

    def ip_forward(self) -> bool:
        try:
            subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=1'])
        except Exception:
            print("\033[91mIP forwarding Failed.\033[0m")
            return False
        else:
            print("\033[92mIP forwarding enabled.\033[0m")
            return True

    def masquerade_nano_traffic(self) -> bool:
        try:
            subprocess.run(['iptables', '-t', 'nat', '-A',
                           'POSTROUTING', '-o', 'wlan2', '-j', 'MASQUERADE'])
            subprocess.run(['iptables', '-A', 'FORWARD', '-i',
                           'eth0', '-o', 'wlan2', '-j', 'ACCEPT'])
            subprocess.run(['iptables', '-A', 'FORWARD', '-i', 'wlan2', '-o', 'eth0',
                           '-m', 'state', '--state', 'RELATED,ESTABLISHED', '-j', 'ACCEPT'])
            subprocess.run(['ifconfig', 'wlan2', 'up'])
        except Exception:
            print("\033[91mPutting nano traffic behind the Pi Failed.\033[0m")
            return False
        else:
            print("\033[92mAll nano traffic is behind the Pi.\033[0m")
            return True

    def remove_default_gateway(self) -> bool:
        try:
            subprocess.run(['ip', 'r', 'd', 'default', 'via', '192.168.123.1'])
            subprocess.run(['ip', 'r', 'd', 'default', 'via', '192.168.12.1'])
        except Exception:
            print("\033[91mRemoving default gateway Failed.\033[0m")
            return False
        else:
            print("\033[92mDefault gateway removed.\033[0m")
            return True

    def show_new_gateway(self):
        print("\033[92m" + subprocess.run("ip route | grep 'dhcp src'",
              shell=True, capture_output=True, text=True).stdout.strip() + "\033[0m")

    def enable_vnc_server(self) -> bool:
        try:
            subprocess.run(['iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'tcp', '-i', 'wlan2',
                           '--dport', '5913', '-j', 'DNAT', '--to-destination', '192.168.123.13:5900'])
        except Exception:
            print("\033[91mEnabling the VNC Failed.\033[0m")
            return False
        else:
            print("\033[92mVNC server enabled.\033[0m")
            return True

    def begin_stage1(self):
        print("\033[92mStage 1 is about to start...\033[0m")
        # Allow forwarding on the raspberry pi
        print("\033[92mEnabling port forwarding on the Pi...\033[0m")
        self.ip_forward()
        print("\033[92mPutting all nano traffic behind the Pi...\033[0m")
        self.masquerade_nano_traffic()
        print("\033[92mRemoving default gateway...\033[0m")
        self.remove_default_gateway()
        print("\033[92mShowing new gateway...\033[0m")
        self.show_new_gateway()
        # check code until this point
        print("\033[92mEnabling VNC...")
        self.enable_vnc_server()

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
