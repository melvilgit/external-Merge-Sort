from random import randint
N=1000
f=open("largefile","w")
k=0
while True:
 n=randint(0,N)
 f.write(str(n)+"\n")
 k=k+1
 if k==100:
  f.close()
  break



