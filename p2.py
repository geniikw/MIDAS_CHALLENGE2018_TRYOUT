import sys

dir = []

def AddNumber(email):
    m = email
    count = 2
   
    while( m in dir):
        m = email + str(count)
        count+=1
    
    return m

def CreateEmail(name, company):
    nameSplit = name.split()
    First = nameSplit[0][0]
    Last = ""

    if(len(nameSplit) == 2):
        Last = nameSplit[1]
    else:
        Last = nameSplit[2]
    
    Last = Last.replace("-","")

    emailName = Last+First
    if(emailName in dir):
        emailName = AddNumber(emailName)
  
    dir.append(emailName)
    email =  emailName+"@"+company+".com"
    return email.lower()


company = sys.stdin.readline().rstrip()
nameArr = list(sys.stdin.readline().rstrip().split(','))
nameArrz = list(filter(lambda x : len(x)!= 0,nameArr))

email = ""
for n in range(len(nameArrz)):
    if( n != 0 ):
        email += ", "
    
    email += CreateEmail( nameArrz[n], company )
     
print(email)