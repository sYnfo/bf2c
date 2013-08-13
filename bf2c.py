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

def balanced_parens(s):
    balance = 0
    for l in s:
        if l == "[":
            balance += 1
        elif l == "]":
            balance -= 1
            if balance < 0:
                return False
    if balance:
        return False
    return True

with open(sys.argv[1]) as src, open("bf.c", "w") as outp:
    if not balanced_parens(src):
        sys.exit("Unbalanced parentheses.")
    src.seek(0)
    for n, line in enumerate(src):
        outp.write("#line " + str(n) + '"%s"\n'%sys.argv[1])
        for l in line:
            if l in bf2c:
                outp.write(bf2c[l] + "\n")

subprocess.call(["gcc", "-g", "bf_runtime.c", "-o", "bf"])
