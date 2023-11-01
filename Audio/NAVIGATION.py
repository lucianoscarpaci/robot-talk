import subprocess
import time

# Get the process ID of the command using ps and grep
ps_command = "ps -aux | grep wsaudio"
output = subprocess.check_output(ps_command, shell=True).decode()

# Find the process ID line in the output
pid_line = next(line for line in output.split('\n') if 'wsaudio' in line)

# Extract the PID from the line
pid = pid_line.split()[1]

# Kill the process using sudo and the extracted PID
kill_command = f"echo '123' | sudo -S kill -9 {pid}"
subprocess.call(kill_command, shell=True)

# Wait for 20 seconds
time.sleep(20)

# Execute the aplay command
aplay_command = "aplay -D plughw:2,0 /home/unitree/talk/NAVIGATION_button.wav"
subprocess.call(aplay_command, shell=True)