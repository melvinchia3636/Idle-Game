from sss import *
from tkinter import *
from tkinter.font import Font
import os

def buttontkinter_on_enter(e): #clickme detection
  if tkinterbutton['state']==NORMAL:
    tkinterbutton['background'] = '#363636'
    tkinterbutton['fg'] = '#01FF70'
def buttontkinter_on_leave(e): #clickme detection
  if tkinterbutton['state']==NORMAL:
    tkinterbutton['background'] = '#111111'
    tkinterbutton['fg'] = '#01FF70'
def buttonbutton_on_enter(e): #clickme detection
  if buttonbutton['state']==NORMAL:
    buttonbutton['background'] = '#363636'
    buttonbutton['fg'] = '#01FF70'
def buttonbutton_on_leave(e): #clickme detection
  if buttonbutton['state']==NORMAL:
    buttonbutton['background'] = '#111111'
    buttonbutton['fg'] = '#01FF70'
def buttonentry_on_enter(e): #clickme detection
  if entrybutton['state']==NORMAL:
    entrybutton['background'] = '#363636'
    entrybutton['fg'] = '#01FF70'
def buttonentry_on_leave(e): #clickme detection
  if entrybutton['state']==NORMAL:
    entrybutton['background'] = '#111111'
    entrybutton['fg'] = '#01FF70'
def buttonlabel_on_enter(e): #clickme detection
  if labelbutton['state']==NORMAL:
    labelbutton['background'] = '#363636'
    labelbutton['fg'] = '#01FF70'
def buttonlabel_on_leave(e): #clickme detection
  if labelbutton['state']==NORMAL:
    labelbutton['background'] = '#111111'
    labelbutton['fg'] = '#01FF70'
def checkbuttonbutton_on_enter(e): #clickme detection
  if checkbuttonbutton['state']==NORMAL:
    checkbuttonbutton['background'] = '#363636'
    checkbuttonbutton['fg'] = '#01FF70'
def checkbuttonbutton_on_leave(e): #clickme detection
  if checkbuttonbutton['state']==NORMAL:
    checkbuttonbutton['background'] = '#111111'
    checkbuttonbutton['fg'] = '#01FF70'
def radiobuttonbutton_on_enter(e): #clickme detection
  if radiobuttonbutton['state']==NORMAL:
    radiobuttonbutton['background'] = '#363636'
    radiobuttonbutton['fg'] = '#01FF70'
def radiobuttonbutton_on_leave(e): #clickme detection
  if radiobuttonbutton['state']==NORMAL:
    radiobuttonbutton['background'] = '#111111'
    radiobuttonbutton['fg'] = '#01FF70'
def textbutton_on_enter(e): #clickme detection
  if textbutton['state']==NORMAL:
    textbutton['background'] = '#363636'
    textbutton['fg'] = '#01FF70'
def textbutton_on_leave(e): #clickme detection
  if textbutton['state']==NORMAL:
    textbutton['background'] = '#111111'
    textbutton['fg'] = '#01FF70'
def listboxbutton_on_enter(e): #clickme detection
  if listboxbutton['state']==NORMAL:
    listboxbutton['background'] = '#363636'
    listboxbutton['fg'] = '#01FF70'
def listboxbutton_on_leave(e): #clickme detection
  if listboxbutton['state']==NORMAL:
    listboxbutton['background'] = '#111111'
    listboxbutton['fg'] = '#01FF70'


global n

if os.path.isfile('game.txt'):
  reader = open('game.txt', 'r')
  reader = ''.join(reader.readlines()).split(',')
  n = int(reader[0])
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
    tkintercost +=int(addn/4*10)
    addn+=addn/4
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
    buttoncost +=int(addn/4*1000)
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
    entrycost +=int(addn/2*10000)
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
    radiobuttoncost +=int(addn/2*10000)
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
    textcost +=int(addn/2*10000)
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
    listboxcost +=int(addn/2*10000)
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

buttonframe1 = Frame(main, bg='#01FF70', width=314, height=62)
buttonframe2 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe3 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe4 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe5 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe6 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe7 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe8 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe9 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe10 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe11 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe12 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe13 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe14 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe15 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe16 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe17 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe18 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe19 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe20 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe21 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe22 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe23 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe24 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe25 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe26 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe27 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe28 = Frame(main, bg='#01FF70', width=314, height=128)
buttonframe29 = Frame(main, bg='#01FF70', width=314, height=128)

tkinterbutton = Button(
  main,
  text='BUY TKINTER'+'\n'+str(ShortScale(tkinteramount))+'\n'+str(ShortScale(tkintercost))+' root',
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

num.grid(row=0, column=0, columnspan=4)

buttonframe2.grid(row=1, column=0, padx=84)
tkinterbutton.grid(row=1, column=0, padx=84)

buttonframe3.grid(row=2, column=0, padx=84, pady=10)
buttonbutton.grid(row=2, column=0, padx=84, pady=10)

buttonframe4.grid(row=3, column=0, padx=84)
entrybutton.grid(row=3, column=0, padx=84)

buttonframe5.grid(row=4, column=0, padx=84, pady=10)
labelbutton.grid(row=4, column=0, padx=84, pady=10)

buttonframe6.grid(row=5, column=0, padx=84)
checkbuttonbutton.grid(row=5, column=0, padx=84)

buttonframe7.grid(row=6, column=0, padx=84, pady=10)
radiobuttonbutton.grid(row=6, column=0, padx=84)

buttonframe8.grid(row=7, column=0, padx=84)
textbutton.grid(row=7, column=0, padx=84)

buttonframe9.grid(row=1, column=1, padx=84)
listboxbutton.grid(row=1, column=1, padx=84)

buttonframe10.grid(row=2, column=1, padx=84)

buttonframe11.grid(row=3, column=1, padx=84)

buttonframe12.grid(row=4, column=1, padx=84)

buttonframe13.grid(row=5, column=1, padx=84)

buttonframe14.grid(row=6, column=1, padx=84)

buttonframe15.grid(row=7, column=1, padx=84)

buttonframe16.grid(row=1, column=2, padx=84)

buttonframe17.grid(row=2, column=2, padx=84)

buttonframe18.grid(row=3, column=2, padx=84)

buttonframe19.grid(row=4, column=2, padx=84)

buttonframe20.grid(row=5, column=2, padx=84)

buttonframe21.grid(row=6, column=2, padx=84)

buttonframe22.grid(row=7, column=2, padx=84)

buttonframe23.grid(row=1, column=3, padx=84)

buttonframe24.grid(row=2, column=3, padx=84)

buttonframe25.grid(row=3, column=3, padx=84)

buttonframe26.grid(row=4, column=3, padx=84)

buttonframe27.grid(row=5, column=3, padx=84)

buttonframe28.grid(row=6, column=3, padx=84)

buttonframe29.grid(row=7, column=3, padx=84)

mps.grid(row=12, column=0, pady=10, columnspan=4)

tkinterbutton.bind('<Enter>', buttontkinter_on_enter)
tkinterbutton.bind('<Leave>', buttontkinter_on_leave)

buttonbutton.bind('<Enter>', buttonbutton_on_enter)
buttonbutton.bind('<Leave>', buttonbutton_on_leave)

entrybutton.bind('<Enter>', buttonentry_on_enter)
entrybutton.bind('<Leave>', buttonentry_on_leave)

labelbutton.bind('<Enter>', buttonlabel_on_enter)
labelbutton.bind('<Leave>', buttonlabel_on_leave)

checkbuttonbutton.bind('<Enter>', checkbuttonbutton_on_enter)
checkbuttonbutton.bind('<Leave>', checkbuttonbutton_on_leave)

radiobuttonbutton.bind('<Enter>', radiobuttonbutton_on_enter)
radiobuttonbutton.bind('<Leave>', radiobuttonbutton_on_leave)

textbutton.bind('<Enter>', textbutton_on_enter)
textbutton.bind('<Leave>', textbutton_on_leave)

listboxbutton.bind('<Enter>', listboxbutton_on_enter)
listboxbutton.bind('<Leave>', listboxbutton_on_leave)

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
