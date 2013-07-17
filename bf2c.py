import sys
import subprocess

bf2c = {">": "INCD()",  #increment data pointer \
        "<": "DECD()",  #decrement data pointer \
        "+": "INC()",   #increment byta at data pointer \
        "-": "DEC()",   #decrement byta at data pointer \
        ".": "PRINT()", #output byte at data pointer \
        ",": "IN()",    #store input at data pointer \
        "[": "JUMPF()", #jump forward to ] if zero \
        "]": "JUMPB()"} #jump backward to [ if nonzero

with open(sys.argv[1]) as src, open("bf.c", "w") as outp:
    for n, line in enumerate(src):
        outp.write("#line " + str(n) + '"%s"\n'%sys.argv[1])
        for l in line:
            if l in bf2c:
                outp.write(bf2c[l] + "\n")

subprocess.call(["gcc", "-g", "prelude.c", "-o", "bf"])
