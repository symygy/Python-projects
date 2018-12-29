
import time
import datetime

#print("Start")
#x=time.time() #wyswietla aktualny czas w formie sekund od 1 stycznia 1970
#time.sleep(2)
#y=time.time()-x
#print("Stop ")

#print(str(x))
#print(str(y))

################################################

#timer=time.time()
#timer2=time.time()
#while True:
#   if time.time()-timer > 2:
#        print("2 sekundy")
#        timer=time.time()
#    if time.time()-timer2 > 6:
#        print("6 ssekunda")
#        timer2=time.time()
#        break

#############################

print(datetime.datetime.now())
print(datetime.datetime(year=2010, month=12, day=17))

teraz = datetime.datetime.now()

print(str(teraz.hour)+":"+str(teraz.minute))

print(teraz.strftime("%H:%M %p %d.%m.%Y"))

print(teraz.strftime("%I:%M %p %d.%B.%Y"))  #da sie ustawic polski jezyk w pythonie

