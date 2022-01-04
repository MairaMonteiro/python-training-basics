num=int(input('Is this number triangular?'))
n=1
multi=n * (n+1) * (n+2)
while multi < num :
    n=n+1
    multi=n*(n+1)*(n+2)
if multi == num :
    print('é triangular')
else :
    print('não é triangular')
