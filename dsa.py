import random,math

def mod(base,exponent,modulus):	#function to calculate (a**k)mod b for large numbers
	if modulus == 1:
		return 0 
	c=1
	for e_prime in range(1,exponent):
		c = (c * base)%modulus
	return c
		
def checkprime(no):
	if no%2==0:    #even no
		return False
	else:
		i=3
		while i<(math.sqrt(no)+1):
			if no%i==0:
				return False
			else:
				i=i+2
		
def siggen():
	global p,q,g,h,x,y,k,r,s
	flag=1  #for executing loop
	while(flag==1):
		flag=0
		k=random.randint(1,q)
		r=(mod(g,k,p)%q)
		s=x*r
		s=s+h
		s=s%q
		s=s/k
		if s==0:
			flag=1
		if s>q:
			flag=1
	print r," ",s
	sigver()

def sigver():
	global p,q,g,h,x,y,s,r,k
	#signature generated now verify
	c1=r<q
	c2=s<q
	w=(1/s)%q
	u1=(h*w)%q
	u2=(r*w)%q
	v=((mod(g,u1,p)*mod(y,u2,p))%p)
	v=v%q
	if (v==r):
		print "Signature correvt and verified"
	else:
		print " Invalid signture generated! again generaating signature"
		siggen()

def main():
	global p,q,g,h,x,y,s,r,k
	p=int(raw_input("p:"))
	q=int(raw_input("q:"))
	g=int(raw_input("g:"))
	c1=checkprime(p)
	c2=checkprime(q)
	c3=(p-1)%q==0
	c4=(g**q)%p==1
	if c1==False or c2==False or c3==False or c4==False:
		print "Enter valid parameter tuple!"
		main()
	h=int(raw_input("h:"),16)
	x=int(raw_input("private key:"))
	y=int(raw_input("public key:"))
	siggen()

if __name__ == "__main__":
    main()
