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
        stage = input("Which WiFi stage are you in? (1 or 2):")

        if stage == "1":
            self.begin_stage1()
        elif stage == "2":
            self.begin_stage2()
        else:
            sys.exit()


wifi = WiFi()
wifi.start()
