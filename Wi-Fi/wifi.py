import subprocess
import sys


class WiFi:

    def __init__(self):
        pass

    def begin_stage1(self):
        print("Stage 1 has been selected")

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
		    print("++++ Dog WiFi ++++")
		    stage = input("Which WiFi stage are you in? (1 or 2):")

		    if stage == "1":
		        self.begin_stage1()
		        break
		    elif stage == "2":
		        self.begin_stage2()
		        break
		    else:
		        print("Error: wrong input. Type '1' or '2' ")      


wifi = WiFi()
wifi.start()
