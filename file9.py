import matplotlib.pyplot as p
x=[1,2,3,4,5]
y=[1,8,9,12,15]
p.figure(1)
p.subplot(121)
p.grid()
p.plot(x,y,'r^')
p.subplot(122)
p.plot(x,y,'ro')
p.show()