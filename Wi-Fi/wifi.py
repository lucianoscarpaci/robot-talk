import subprocess
import sys
import os
import time


class WiFi:

    def __init__(self):
        self.go = subprocess.run

    def ip_forward(self) -> bool:
        try:
            self.go(['sysctl', '-w', 'net.ipv4.ip_forward=1'])
        except Exception:
            print("\033[91mIP forwarding Failed.\033[0m")
            return False
        else:
            print("\033[92mIP forwarding enabled.\033[0m")
            return True

    def masquerade_nano_traffic(self) -> bool:
        try:
            self.go(['iptables', '-t', 'nat', '-A',
                     'POSTROUTING', '-o', 'wlan2', '-j', 'MASQUERADE'])
            self.go(['iptables', '-A', 'FORWARD', '-i',
                     'eth0', '-o', 'wlan2', '-j', 'ACCEPT'])
            self.go(['iptables', '-A', 'FORWARD', '-i', 'wlan2', '-o', 'eth0',
                     '-m', 'state', '--state', 'RELATED,ESTABLISHED', '-j', 'ACCEPT'])
            self.go(['ifconfig', 'wlan2', 'up'])
        except Exception:
            print("\033[91mPutting nano traffic behind the Pi Failed.\033[0m")
            return False
        else:
            print("\033[92mAll nano traffic is behind the Pi.\033[0m")
            return True

    def remove_default_gateway(self) -> bool:
        try:
            self.go(['ip', 'r', 'd', 'default', 'via', '192.168.123.1'])
            self.go(['ip', 'r', 'd', 'default', 'via', '192.168.12.1'])
        except Exception:
            print("\033[91mRemoving default gateway Failed.\033[0m")
            return False
        else:
            print("\033[92mDefault gateway removed.\033[0m")
            return True

    def show_new_gateway(self):
        print("\033[92m" + self.go("ip route | grep 'dhcp src'",
              shell=True, capture_output=True, text=True).stdout.strip() + "\033[0m")

    def begin_stage1(self):
        # Allow forwarding on the raspberry pi
        print("\033[92mEnabling port forwarding on the Pi...\033[0m")
        self.ip_forward()
        print("\033[92mPutting all nano traffic behind the Pi...\033[0m")
        self.masquerade_nano_traffic()
        print("\033[92mRemoving default gateway...\033[0m")
        self.remove_default_gateway()
        print("\033[92mShowing new gateway...\033[0m")
        self.show_new_gateway()
        print("\033[92mPlease wait...\033[0m")
        # check code until this point
        time.sleep(15)
        print("\033[92mEnabling Wi-Fi...\033[0m")
        self.begin_stage2()

    def begin_stage2(self):
        print("\033[92mEnabling port forwarding on the Pi...\033[0m")
        self.ip_forward()
        print("\033[92mPutting all nano traffic behind the Pi...\033[0m")
        self.masquerade_nano_traffic()
        print("\033[92mRemoving default gateway...\033[0m")
        self.remove_default_gateway()
        print("\033[92mShowing new gateway...\033[0m")
        self.show_new_gateway()
        print("\033[92mWi-Fi has been enabled...\033[0m")

    def start(self):
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

        self.begin_stage1()


wifi = WiFi()
wifi.start()
