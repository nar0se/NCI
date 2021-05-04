import os, subprocess

os.system('cls')
print('----- Using os module -----')
os.system('ls -a')
os.system('cat /etc/passwd | cut -d: -f1')

print()
print('---- Using subprocess module ----')
subprocess.run(['ls', '-a'])