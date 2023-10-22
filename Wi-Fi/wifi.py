import subprocess
import sys


class WiFi:

    def __init__(self):
        pass

    def ip_forward(self):
        subprocess.run(
            ['sysctl', '-w', 'net.ipv4.ip_forward=1'])

    def begin_stage1(self):
        print("\033[92mStage 1 is about to start...\033[0m")
        # Allow forwarding on the raspberry pi
        print("\033[92mEnabling port forwarding on the Pi...\033[0m")
        self.ip_forward()
        if subprocess.run(['sysctl', '-n', 'net.ipv4.ip_forward']).returncode == 0:
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
            print("\033[94m" + dog_wifi_ascii + "\033[0m")
            print("\033[94m+++++++++++++++++++++ Dog WiFi +++++++++++++++++++++\033[0m")
            stage = input("\033[92mWhich WiFi stage are you in? (1 or 2):\033[0m")

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
                print("\033[94m+++++++++++++++++++++ Dog WiFi +++++++++++++++++++++\033[0m")


wifi = WiFi()
wifi.start()
