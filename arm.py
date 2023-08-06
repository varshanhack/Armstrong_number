#Armstrong number
import sys,subprocess
while True:
    l=[]
    n=input("Enter the number ==> ")
    ln=len(n)
    print("")
    for i in n:
        no=int(i)**ln
        l.append(no)
    lsum=sum(l)
    if int(n)==lsum:
        print("The number",n,"is an Armstrong number")
    else:
        print("The number",n,"is not an Armstrong number")
    print("")
    input("Press enter to continue...")
    subprocess.run("cls",shell=True)
