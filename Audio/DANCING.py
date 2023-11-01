import subprocess

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

# Execute the aplay command
aplay_command = "aplay -D plughw:2,0 /home/unitree/talk/DANCING_button.wav"
subprocess.call(aplay_command, shell=True)
