import sys

def CheckNE(input):
    isEnglish = False
    isNumber = False
    for n in range(len(input)):
        ch = input[n]
        if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
            isEnglish = True
        if((ch >= '0' and ch <= '9')) :
            isNumber = True
    return isEnglish and isNumber

def CheckC(input):
    c = 0
    prev = ''
    for n in range(len(input)):
        if(n != 0 and (ord(input[n]) - ord(prev)) == 1 ):
            c += 1
        else:
            c = 0
        if(c >= 2):
            return False
    
        prev = input[n]
    return True

def check(id, pw):

    idlen = len(id)
    pwlen = len(pw)

    if(6 > idlen or idlen > 13 ):
        return "F"
    if(8 > pwlen or pwlen > 17):
        return "F"
    if(not(CheckNE(id) and CheckNE(pw))):
        return "F"    
    if(not(CheckC(id) and CheckC(pw))):
        return "F"
    return "T"

id = sys.stdin.readline()
pw = sys.stdin.readline()

print(check(id,pw))
