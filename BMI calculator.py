                  #bmi calculator#
def function1():
    f=float(input("first your height in feets then in inches..."))
    i=float(input("now enter inches!"))
    fi=f*12
    inches=fi+i
    meter=(inches/39.37)
    print(meter)
   
name=str(input("enter your name ="))
a=int(input("if you want to convert your height in meters then press 1 otherwise press 0 =="))
if(a == 1 ):
    function1()
    
height=float(input("enter your height in meters ="))
weight=float(input("enter your weight in kgs ="))
bmi=weight/(height ** 2)
if(bmi < 18.5):
    print(name,"you are underweight (>__<)")
elif( 18.5 <= bmi <= 24.9):
    print(name,"your weight is normal (^_^)")
elif(25 <= bmi <= 30 ):
    print(name,"you are overweight (-__-)")
elif(bmi >= 31): 
    print(name,"you are obese (O_O)")
   