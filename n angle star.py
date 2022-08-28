from turtle import *
error=None
color("#c2002a","#f0ae00")
width(3)
begin_fill()
try:
    N=int(numinput("Enter in","Please enter in N=?"))
    error=False
except TypeError:
    pu()
    goto(-150,0)
    write("You cancelled the window, run the code again!",font=("黑体",14,"normal"))
    error=True
    done()
if error==False:
    if N%2==1 and N!=1:
        pd()
        for i in range(N):
            forward(100)
            right(180-180/N)
        end_fill()
        done()
    elif N%2==0:
        pu()
        goto(-200,0)
        write("Please enter N as an eval number, run the code again!",font=("黑体",14,"normal"))
        done()
    else:
        pu()
        goto(-150,0)
        write("Don't enter in zero, run the code again!",font=("黑体",14,"normal"))
        done()
elif error==None:
    pu()
    goto(-150,0)
    write("Error",font=("黑体",14,"normal"))
    done()