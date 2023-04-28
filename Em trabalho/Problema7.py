#problema 7
def raiz_trans(a):
    from math import log
    from math import e
    x0 = -1/log(a,e)
    for i in range(1,100):
        x0 = (log(x0,e)/-log(a,e)) 
    return 1/x0
# -------- função acima está funcionando ok 

def pn_primo(n,k):
    from math import e
    return (k/raiz_trans(e**(-k/n)))
    
    
print(pn_primo(10001, 2.718281828459045))