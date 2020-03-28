import re

def equationsPossible(s):
    return re.match('[0-9]+(\w){1}\^[0-9]+([+|\-|\/|*][0-9]+(\w){1}\^[0-9]+)*',s) 
    

def menu():
    print("1.Polynomail derivative (D^aplha (ax^n+bx^n-1+...))")
    print("2.Single variable derivative (D^aplha(x^mu))" )
    print("3.End")


if __name__=="__main__":
    while(1):
        menu()
        choices=int(input())
        if(choices==3):
            break
        if(choices==1):
            equation="10x^2+20x^3+30"
            print(equationsPossible(equation))

            """
            terms=int(input("Enter number of terms in the equation : "))
            while(terms!=0):
                print("Enter coefficient and power of coefficient : ")
                coeff_and_powers.append(list(map(int,input().split())))
                terms-=1
            print(coeff_and_powers)
            """