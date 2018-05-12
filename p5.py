import sys

compareToken = ["!=", "==", ">", "<", ">=", "<="]
#crn(n-3) ,ct(n-2) ,cln(n-1),?(n),rn(n+1),:(n+2), ln(n+3)

def Cal3(i, ex):
    if(i < 3 or i+3 > len(ex)):
        return False
    crn = ex[i-3]
    ct = ex[i-2]
    cln = ex[i-1]
    rn = ex[i+1]
    t = ex[i+2]
    ln = ex[i+3]     

    if(not crn.isdigit() or not cln.isdigit() or not rn.isdigit() or not ln.isdigit()):
        return False
    if(not ct in compareToken):
        return False
    if(t != ':'):
        return False
    result = False

    if(ct == "!="):
        result = int(crn) != int(cln)
    elif(ct == "=="):
        result = int(crn) == int(cln)
    elif(ct == ">"):
        result = int(crn) > int(cln)
    elif(ct == "<"):
        result = int(crn) < int(cln)
    elif(ct == ">="):
        result = int(crn) >= int(cln)
    elif(ct == "<="):
        result = int(crn) <= int(cln)

    
    if(result):
        del ex[i+3]
        del ex[i+2]
    else:
        del ex[i+2]
        del ex[i+1]
    
    del ex[i]
    del ex[i-1]
    del ex[i-2]
    del ex[i-3]

    return True

split = sys.stdin.readline().split()


allq = [i for i, x in enumerate(split) if x == '?']
error = False
for i in reversed(allq):
    if(not Cal3(i,split)):
        error = True
        break
    
if(error or len(split)!= 1 or not split[0].isdigit()):
    print(-1)
else: 
    print(split[0])



