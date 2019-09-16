import sys
import subprocess

arg = sys.argv[1]
if arg == "-l":
    cmd = ["code", "--list-extensions", ">|", "extensions.txt"]
    subprocess.call(cmd)
elif arg == "-i":
    f = open("extensions.txt", "r")
    lines = f.readlines()
    for line in lines:
        cmd = ["code", "--install-extension", line.strip("\n")]
        subprocess.call(cmd)
else:
    print("unsupported option, please use -l or -i")