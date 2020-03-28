import math
import matplotlib.pyplot as plt 
def polynomial_successive_differentiation(l,alpha):
    i=0
    l_f=[]
    t=[]
    l_dio=[]
    l_dfo=[]
    ans=0
    for x in l:
        if x[1]<alpha:
            l.remove(x)
        else:
            ans+=(math.gamma((x[1]+1)/math.gamma(x[1]-alpha+1)))
    print(ans)
    i=0
    while(i<10):
        t.append(i)
        f=0
        dio=0
        dfo=0
        for x in l:
            f+=(pow(t[-1],x[1]))
            dio+=(x[1]*pow(t[-1],x[1]-1))
            dfo+=((math.gamma(x[1]+1)/math.gamma(x[1]-alpha+1))*pow(t[-1],(x[1]-alpha)))
        l_f.append(f)
        l_dio.append(dio)
        l_dfo.append(dfo)
        i+=0.01

    #print(len(t),len(f),len(dio),len(dfo))
    plt.plot(t,l_f,color="blue")
    plt.plot(t,l_dio,color="red")
    plt.plot(t,l_dfo,color="green")

#function call:
polynomial_successive_differentiation([[1.23,1.2]],0.1)