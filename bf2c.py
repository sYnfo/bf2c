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
    balanced_parens = 0
    for n, line in enumerate(src):
        outp.write("#line " + str(n) + '"%s"\n'%sys.argv[1])
        for l in line:
            if l == "[":
                balanced_parens += 1
            elif l == "]":
                balanced_parens -= 1
            if balanced_parens < 0:
                sys.exit("Unbalanced parenthesis.")
            if l in bf2c:
                outp.write(bf2c[l] + "\n")
if balanced_parens:
    sys.exit("Unbalanced parenthesis.")

subprocess.call(["gcc", "-g", "bf_runtime.c", "-o", "bf"])
