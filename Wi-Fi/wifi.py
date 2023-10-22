import subprocess
import sys


class WiFi:

    def __init__(self):
        self.ip_forward = subprocess.run(
            ['sysctl', '-w', 'net.ipv4.ip_forward=1'])

    def begin_stage1(self):
        print("\033[92mStage 1 is about to start...\033[0m")
        # Allow forwarding on the raspberry pi
        print("\033[92mEnabling port forwarding on the Pi...\033[0m")
        if self.ip_forward.returncode == 0:
            print("\033[92mDone.\033[0m")
        else:
            print("\033[91mIP forwarding Failed.\033[0m")
        print("\033[92mPutting all nano traffic behind the Pi...\033[0m")

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
            print(dog_wifi_ascii)
            print("+++++++++++++++++++++ Dog WiFi +++++++++++++++++++++")
            stage = input("Which WiFi stage are you in? (1 or 2):")

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
                print("+++++++++++++++++++++ Dog WiFi +++++++++++++++++++++")


wifi = WiFi()
wifi.start()
