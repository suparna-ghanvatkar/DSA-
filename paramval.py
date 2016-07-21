from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
        print s
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

print probably_prime(2003,50)
'''
def val(p,q,g):
    print "Validating the parametrs with following conditions:"
    a=probably_prime(p,500)
    b=probably_prime(q,100)
    c=(p-1)%q==0
    d=(g**q)%p==1
    e=p<(2**1024)
    f=q<(2**160)
    h=(g<p) and g>1
    print "Is p prime?",a
    print "Is q prime?",b
    print "Is (p-1)%q==0?",c
    print "Is (g**q)%p==1?",d
    print "Is p a 1024 bit number?",e
    print "Is q a 160-bit number?",f
    print "Is 1<g<p?",h
    val=1
    if a==False or b==False or c==False or d==False or e==False or f==False or h==False:
        val=0
    if val==0:
        print "Parameters are not valid!"
    else:
        print "Parameters are valid!"

''''''
Various possible inputs for DSA parameters:
p=31, q=5, g=4
q = 11, p = 23, g = 4
p=7, q=3, g=4
''''''
p=int(raw_input("Enter p:"))
q=int(raw_input("Enter q:"))
g=int(raw_input("Enter g:"))
val(p,q,g)

''''''
OUTPUT

[student@localhost ~]$ python paramval.py 
Enter p:7
Enter q:3
Enter g:9
Validating the parametrs with following conditions:
Is p prime? True
Is q prime? True
Is (p-1)%q==0? True
Is (g**q)%p==1? True
Is p a 1024 bit number? True
Is q a 160-bit number? True
Is 1<g<p? False
Parameters are not valid!

[student@localhost ~]$ python paramval.py 
Enter p:7
Enter q:3
Enter g:4
Validating the parametrs with following conditions:
Is p prime? True
Is q prime? True
Is (p-1)%q==0? True
Is (g**q)%p==1? True
Is p a 1024 bit number? True
Is q a 160-bit number? True
Parameters are valid!
'''
