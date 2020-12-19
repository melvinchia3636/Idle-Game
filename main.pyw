from sss import *
from tkinter import *
from tkinter.font import Font
import os

def button_on_enter(e): #clickme detection
  if type(e.widget) == Button:
    e.widget['background'] = '#363636'
    e.widget['fg'] = '#01FF70'
def button_on_leave(e): #clickme detection
  if type(e.widget) == Button:
    e.widget['background'] = '#111111'
    e.widget['fg'] = '#01FF70'


global n

if os.path.isfile('game.txt'):
  reader = open('game.txt', 'r')
  reader = ''.join(reader.readlines()).split(',')
  n = int(reader[0].split('.')[0])
  addn = int(reader[1])
  tkintercost = int(reader[2])
  tkinteramount = int(reader[3])
  buttoncost = int(reader[4])
  buttonamount = int(reader[5])
  entrycost = int(reader[6])
  entryamount = int(reader[7])
  labelcost = int(reader[8])
  labelamount = int(reader[9])
  checkbuttoncost = int(reader[10])
  checkbuttonamount = int(reader[11])
  radiobuttoncost = int(reader[12])
  radiobuttonamount = int(reader[13])
  textcost = int(reader[14])
  textamount = int(reader[15])
  listboxcost = int(reader[16])
  listboxamount = int(reader[17])
else:
  n=1
  addn = 1
  tkintercost = 10
  tkinteramount = 0
  buttoncost = 1000
  buttonamount = 0
  entrycost = 1000000
  entryamount = 0
  labelcost = 1000000000
  labelamount = 0
  checkbuttoncost = 10**12
  checkbuttonamount = 0
  radiobuttoncost = 10**15
  radiobuttonamount = 0
  textcost = 10**18
  textamount = 0
  listboxcost = 10**21
  listboxamount = 0
  writer = open('game.txt', 'w')
  writer.write(str(n)+','+
               str(addn)+','+
               str(tkintercost)+','+
               str(tkinteramount)+','+
               str(buttoncost)+','+
               str(buttonamount)+','+
               str(entrycost)+','+
               str(entryamount)+','+
               str(labelcost)+','+
               str(labelamount)+','+
               str(checkbuttoncost)+','+
               str(checkbuttonamount)+','+
               str(radiobuttoncost)+','+
               str(radiobuttonamount)+','+
               str(textcost)+','+
               str(textamount)+','+
               str(listboxcost)+','+
               str(listboxamount))
  writer.close()

mpsnum = str(ShortScale(int(addn)))

def quitwin(e):
  main.destroy()
  quit()
def fullscr(e):
  global fs
  if fs==True:
    main.attributes("-fullscreen", False)
    fs=False
  else:
    main.attributes("-fullscreen", True)
    fs=True

main = Tk()
main.geometry('1920x1080+0+0')
main.config(bg='#111112')
main.title('Idle LOL')
fs = True
main.attributes("-fullscreen", True)
main.bind('<Escape>', quitwin)
main.bind('<F11>', fullscr)
main.attributes('-alpha', 0.90)

numfont = Font(size=50, family='Bahnschrift SemiBold')
buttonfont = Font(size=20, family='Bahnschrift Light')
mpsfont = Font(size=15, family='Bahnschrift Light')


def upgradetkinter():
  global addn
  global n
  global tkintercost
  global tkinteramount
  global num
  if n >= tkintercost:
    n-=tkintercost
    tkinteramount+=1
    tkintercost +=int(addn//4*10)
    addn+=addn
    tkinterbutton.config(text='BUY TKINTER'+'\n'+str(ShortScale(tkinteramount))+'\n'+str(ShortScale(tkintercost))+' root')
    tkinterbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()
    
def upgradebutton():
  global addn
  global n
  global buttoncost
  global buttonamount
  global num
  if n >= buttoncost:
    n-=buttoncost
    buttonamount+=1
    buttoncost +=int(addn//4*1000)
    addn+=addn
    buttonbutton.config(text='BUY BUTTON'+'\n'+str(ShortScale(buttonamount))+'\n'+str(ShortScale(buttoncost))+' root')
    buttonbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def upgradeentry():
  global addn
  global n
  global entryamount
  global entrycost
  global num
  if n >= entrycost:
    n-=entrycost
    entryamount+=1
    entrycost +=int(addn//2*10000)
    addn+=addn*2
    entrybutton.config(text='BUY ENTRY'+'\n'+str(ShortScale(entryamount))+'\n'+str(ShortScale(entrycost))+' root')
    entrybutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def upgradelabel():
  global addn
  global n
  global labelamount
  global labelcost
  global num
  if n >= labelcost:
    n-=labelcost
    labelamount+=1
    labelcost +=int(addn*10000)
    addn+=addn*2
    labelbutton.config(text='BUY LABEL'+'\n'+str(ShortScale(labelamount))+'\n'+str(ShortScale(labelcost))+' root')
    labelbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def upgradecheckbutton():
  global addn
  global n
  global checkbuttonamount
  global checkbuttoncost
  global num
  if n >= checkbuttoncost:
    n-=checkbuttoncost
    checkbuttonamount+=1
    checkbuttoncost +=int(addn*10000)
    addn+=addn*10
    checkbuttonbutton.config(text='BUY CHECKBUTTON'+'\n'+str(ShortScale(checkbuttonamount))+'\n'+str(ShortScale(checkbuttoncost))+' root')
    checkbuttonbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def upgraderadiobutton():
  global addn
  global n
  global radiobuttonamount
  global radiobuttoncost
  global num
  if n >= radiobuttoncost:
    n-=radiobuttoncost
    radiobuttonamount+=1
    radiobuttoncost +=int(addn//2*10000)
    addn+=addn*2
    radiobuttonbutton.config(text='BUY RADIOBUTTON'+'\n'+str(ShortScale(radiobuttonamount))+'\n'+str(ShortScale(radiobuttoncost))+' root')
    radiobuttonbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def upgradetext():
  global addn
  global n
  global textamount
  global textcost
  global num
  if n >= textcost:
    n-=textcost
    textamount+=1
    textcost +=int(addn//2*10000)
    addn+=addn*2
    textbutton.config(text='BUY TEXT'+'\n'+str(ShortScale(textamount))+'\n'+str(ShortScale(textcost))+' root')
    textbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def upgradelistbox():
  global addn
  global updateclickme
  global n
  global listboxamount
  global listboxcost
  global num
  if n >= listboxcost:
    n-=listboxcost
    listboxamount+=1
    listboxcost +=int(addn//2*10000)
    addn+=addn*2
    listboxbutton.config(text='BUY LISTBOX'+'\n'+str(ShortScale(listboxamount))+'\n'+str(ShortScale(int(listboxcost)))+' root')
    listboxbutton.update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(addn)))
    moneypersec.set(mpsnum)
    mps.update()

def addlol():
  now.set(current_money())
  num.update()

result = ShortScale(int(n))

num = Label(
  main,
  font=numfont,
  bg='#111111',
  fg='#01FF70',
  relief=FLAT
  )

buttonFrame = [[Frame(main, bg='#01FF70', width=314, height=128) for j in range(4)] for i in range(6)]

tkinterbutton = Button(
  main,
  text='BUY TCL'+'\n'+str(ShortScale(tkinteramount))+'\n'+str(ShortScale(tkintercost))+' root',
  command=upgradetkinter,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='#01FF70',
  relief=FLAT
  )

buttonbutton = Button(
  main,
  text='BUY BUTTON'+'\n'+str(ShortScale(buttonamount))+'\n'+str(ShortScale(buttoncost))+' root',
  command=upgradebutton,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='#01FF70',
  relief=FLAT
  )

entrybutton = Button(
  main,
  text='BUY ENTRY'+'\n'+str(ShortScale(entryamount))+'\n'+str(ShortScale(entrycost))+' root',
  command=upgradeentry,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='#01FF70',
  relief=FLAT
  )

labelbutton = Button(
  main,
  text='BUY LABEL'+'\n'+str(ShortScale(labelamount))+'\n'+str(ShortScale(labelcost))+' root',
  command=upgradelabel,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='#01FF70',
  relief=FLAT
  )

checkbuttonbutton = Button(
  main,
  text='BUY CHECKBUTTON'+'\n'+str(ShortScale(checkbuttonamount))+'\n'+str(ShortScale(checkbuttoncost))+' root',
  command=upgradecheckbutton,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='#01FF70',
  relief=FLAT
  )

radiobuttonbutton = Button(
  main,
  text='BUY RADIOBUTTON'+'\n'+str(ShortScale(radiobuttonamount))+'\n'+str(ShortScale(radiobuttoncost))+' root',
  command=upgraderadiobutton,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='white',
  relief=FLAT
  )

textbutton = Button(
  main,
  text='BUY TEXT'+'\n'+str(ShortScale(textamount))+'\n'+str(ShortScale(textcost))+' root',
  command=upgradetext,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='white',
  relief=FLAT
  )

listboxbutton = Button(
  main,
  text='BUY LISTBOX'+'\n'+str(ShortScale(listboxamount))+'\n'+str(ShortScale(int(listboxcost)))+' root',
  command=upgradelistbox,
  font=buttonfont,
  width=20,
  padx=1,
  fg='#01FF70',
  bg='#111111',
  activebackground='#363636',
  activeforeground='white',
  relief=FLAT
  )

moneypersec = StringVar()
moneypersec.set(mpsnum)

mps = Label(
  main,
  textvariable = moneypersec,
  fg='#01FF70',
  bg='#111111',
  font = mpsfont
  )

num.grid(row=0, column=0, columnspan=4, pady=20)

for i in range(6):
  for j in range(4):
    buttonFrame[i][j].grid(row=i+1, column=j, padx=84, pady=10)

tkinterbutton.grid(row=1, column=0, padx=84)
buttonbutton.grid(row=2, column=0, padx=84, pady=10)
entrybutton.grid(row=3, column=0, padx=84)
labelbutton.grid(row=4, column=0, padx=84, pady=10)
checkbuttonbutton.grid(row=5, column=0, padx=84)
radiobuttonbutton.grid(row=6, column=0, padx=84)
textbutton.grid(row=1, column=1, padx=84)
listboxbutton.grid(row=2, column=1, padx=84)


mps.grid(row=12, column=0, pady=10, columnspan=4)

main.bind('<Enter>', button_on_enter)
main.bind('<Leave>', button_on_leave)

def current_money():
    global n
    n+=addn
    return str(ShortScale(int(n)))+' root'

now = StringVar()
num["textvariable"] = now

def onUpdate():
  now.set(current_money())
  writer = open('game.txt', 'w')
  writer.write(str(n)+','+
      str(int(addn))+','+
      str(int(tkintercost))+','+
      str(int(tkinteramount))+','+
      str(int(buttoncost))+','+
      str(int(buttonamount))+','+
      str(int(entrycost))+','+
      str(int(entryamount))+','+
      str(int(labelcost))+','+
      str(int(labelamount))+','+
      str(int(checkbuttoncost))+','+
      str(int(checkbuttonamount))+','+
      str(int(radiobuttoncost))+','+
      str(int(radiobuttonamount))+','+
      str(int(textcost))+','+
      str(int(textamount))+','+
      str(int(listboxcost))+','+
      str(int(listboxamount)))
  writer.close()
  num.after(500, onUpdate)

onUpdate()

main.mainloop()
