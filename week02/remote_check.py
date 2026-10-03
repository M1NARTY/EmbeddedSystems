import platform
import socket
from pathlib import Path

print("Host: ", socket.gethostname())
print("OS: ", platform.system())
print("CPU: ", platform.machine())
print("file: ", Path(__file__).resolve())