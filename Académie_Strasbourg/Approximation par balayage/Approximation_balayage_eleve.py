# (pour fonctionner, necessite que la fonction f soit creee au prealable)

def balayage():
    
    x=1
    while x<2:
        print("f(",x,")=",f(x))
        x = x+0.1
    
    return None
        
    