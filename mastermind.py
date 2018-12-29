import random
def gen():
  res=""
  for i in range(4):res=res+str(random.randint(1,6))
  return res
#end
def spr(kod,pr):
  lk=list(kod)
  lp=list(pr)
  lc=0
  for i in range(4):
    if lk[i]==lp[i]:
       lc=lc+1
       lk[i]=-1
       lp[i]=-2
    #end
  lb=0
  for i in range(4):
    for j in range(4):
      if lk[i]==lp[j]:
           lb=lb+1
           lk[i]=-1
           lp[j]=-2
#end
  return(lc,lb)
#end def
#print(spr('1234','1234'))
#print(spr('1225','1234'))

kod=gen()
while True:
  pr=input(">>")
  wyn=spr(kod,pr)
  print(" ",wyn)
  if wyn ==(4,0):break
#end
print("gratulacje")