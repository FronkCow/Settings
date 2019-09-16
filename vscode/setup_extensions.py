#import sys
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Import vscode extensions.")
parser.add_argument("-m", help="select mode, \"install\" or \"load\" (to file)")
args = parser.parse_args()
if args.m == "load":
    f = open("extensions.txt", "w")
    cmd = ["code", "--list-extensions"]
    subprocess.call(cmd, stdout=f)
elif args.m == "install":
    f = open("extensions.txt", "r")
    lines = f.readlines()
    for line in lines:
        cmd = ["code", "--install-extension", line.strip("\n")]
        subprocess.call(cmd)
else:
    print("unsupported option, please use \"install\" or \"load\"")