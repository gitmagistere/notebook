def f(x):
    return x**2

def balayage(n):
    x=1
    for k in range(1,n):
        pas=1/10**k
        
        while f(x)<2:
            x = x+pas
            
        x=x-pas
       
    return x
        
    