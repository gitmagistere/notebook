from microbit import*
from maqueen import Maqueen

mq=Maqueen()

while True:
    d=mq.distance()
    if d>10:
        mq.avance(15)
    else:
        mq.recule()

