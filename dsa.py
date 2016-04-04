import random

def mod(a,k,b):	#function to calculate (a**k)mod b for large numbers
	rems=[]
	i=0
	rem=a
	store=a
	if(a%b==0):
		return 0
	while(rem!=0):
		rems.insert(i,rem)
		a=a+store
		rem=a%b
		i=i+1
	no=a**k
	i=store
	index=0
	while(i<no):
		i=i+store
		index=(index+1)%len(rems)
	return rems[index]
		

p=int(raw_input("p:"))
q=int(raw_input("q:"))
g=int(raw_input("g:"))
h=int(raw_input("h:"))
x=int(raw_input("private key:"))
y=int(raw_input("public key:"))
flag=1  #for executing loop
while(flag==1):
	flag=0
	k=random.randint(1,q)
	print k
	r=(mod(g,k,p)%q)
	s=x*r
	s=s+h
	s=s%q
	s=s/k
	print r," ",s
	if s==0:
		flag=1
	if s>q:
		flag=1
