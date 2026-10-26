def premier(n):
    i=2
    prem=True
    while i<=n//2 and prem==True:
        if n%i==0:
            prem=False
        else:
            i=i+1
    return prem
def sc(n):
    s=0
    ch=str(n)
    for i in range (len(ch)):
        s=s+int(ch[i])
    return s
def saisir():
    n=int(input('donner un entier n'))
    while not 100<=n:
         n=int(input('donner un entier n'))
    return n 
def harshad(n):
    if n%sc(n)==0:
        return True
    else:
        return False
def afficher(n,m):
    for i in range (n+1,m+1):
        if harshad(i) and premier(i-1):
            print(i,'est harshard et son predecesseur',i-1,'est premier')
            
n=saisir()
m=int(input('donner m'))
while n>=m:
    m=int(input('donner m'))
afficher(n,m)