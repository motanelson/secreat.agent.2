import os
print("\033c\033[47;31m")
print("give me a file to check ...")
a=input().strip()
os.system("objdump -m i386 --disassembler-options=intel --adjust-vma=0x101000 -b binary -D $1".replace("$1",a))
