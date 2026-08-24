import math
import streamlit as st 

st.set_page_config(page_title='korlat kalkulator')

def szog(x):
    return math.radians((x-1)*15)


def allas(x):
    return (x/15)+1


a = int(input("hányasban volt eredetileg az egyik korlát?"))
b = int(input("hányasban volt eredetileg a második korlát?"))
c = int(input("hányasban van rögzítve most az egyik korlát?"))

sina = (math.sin(szog(a)))
sinb = (math.sin(szog(b)))
sinc = (math.sin(szog(c)))

tav = 2-(sina+sinb)
matav = 2-sinc
d = (math.degrees((math.asin(matav-tav))))

print("rakd a mozgatható korlátot: ", allas(d))
