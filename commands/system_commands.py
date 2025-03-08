import os
import subprocess
import time


def execute_system_command(command):
    """Handle macOS system operations"""
    cmd = command.lower()

    if 'sleep' in cmd:
        os.system("pmset sleepnow")
        return "Putting system to sleep"

    elif 'shutdown' in cmd or 'power off' in cmd:
        subprocess.run(["osascript", "-e", 'tell app "System Events" to shut down'])
        return "Shutting down system"

    elif 'lock' in cmd or 'secure' in cmd:
        subprocess.run(["/usr/bin/pmset", "displaysleepnow"])
        return "Locking system"

    else:
        return None