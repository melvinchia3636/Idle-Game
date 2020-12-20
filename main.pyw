from sss import *
from tkinter import *
from tkinter.font import Font
import os
from itertools import zip_longest
from functools import partial
import json
from copy import deepcopy

def button_on_enter(e): #clickme detection
  if type(e.widget) == Button:
    e.widget['background'] = '#363636'
    e.widget['fg'] = '#01FF70'
def button_on_leave(e): #clickme detection
  if type(e.widget) == Button:
    e.widget['background'] = '#111111'
    e.widget['fg'] = '#01FF70'

if os.path.exists('game.json'):
  data = json.load(open('game.json', 'r'))

else:
  data =  {
      'balance': 0,
      'rps': 1,

      'item': {
          'TCL': {
              'amount': 0,
              'cost': 10
          },
          'BUTTON': {
              'amount': 0,
              'cost': 10**3
          },
          'ENTRY': {
              'amount': 0,
              'cost': 10**6
          },
          'LABEL': {
              'amount': 0,
              'cost': 10**9
          },
          'CHECKBUTTON': {
              'amount': 0,
              'cost': 10**12
          },
          'RADIOBUTTON': {
              'amount': 0,
              'cost': 10**15
          },
          'TEXT': {
              'amount': 0,
              'cost': 10**18
          },
          'LISTBOX': {
              'amount': 0,
              'cost': 10**21
          }
      }
  }
  json.dump(data, open('game.json', 'w'))

mpsnum = str(ShortScale(int(data['rps'])))

def quitwin(e):
  root.destroy()
  quit()
def fullscr(e):
  if fs:
    root.attributes("-fullscreen", False)
    fs=False
  else:
    root.attributes("-fullscreen", True)
    fs=True

root = Tk()
root.geometry('1920x1080+0+0')
root.config(bg='#222222')
root.title('Idle TCL')
fs = True
root.attributes("-fullscreen", True)
root.bind('<Escape>', quitwin)
root.bind('<F11>', fullscr)
root.attributes('-alpha', 0.8)

numfont = Font(size=50, family='Bahnschrift SemiBold')
buttonfont = Font(size=20, family='Bahnschrift Light')
mpsfont = Font(size=15, family='Bahnschrift Light')

def upgrade(selected):
  if data['balance'] >= data['item'][selected]['cost']:
    data['balance']-=data['item'][selected]['cost']
    data['item'][selected]['amount']+=1
    data['item'][selected]['cost'] +=int(data['rps']//4*10)
    data['rps']+=data['rps']
    item_button[data['item'][selected]['button']].config(text=selected+'\n'+str(ShortScale(data['item'][selected]['amount']))+'\n'+str(ShortScale(data['item'][selected]['cost']))+' root')
    item_button[data['item'][selected]['button']].update()
    now.set(current_money())
    num.update()
    mpsnum = str(ShortScale(int(data['rps'])))
    moneypersec.set(mpsnum)
    mps.update()

buttonFrame = [[Frame(root, bg='#01FF70', width=314, height=128) for j in range(4)] for i in range(6)]
item_button = [Button(root, text=i+'\n'+str(ShortScale(data['item'][i]['amount']))+'\n'+str(ShortScale(data['item'][i]['cost']))+' root', command=partial(upgrade, i), font=buttonfont, width=20, padx=1,fg='#01FF70', bg='#111111', activebackground='#363636', activeforeground='#01FF70', relief=FLAT) for i in data['item'].keys()]
for i in range(len(data['item'])): data['item'][list(data['item'].keys())[i]]['button'] = i

def addlol():
  now.set(current_money())
  num.update()

result = ShortScale(int(data['balance']))

num = Label(
  root,
  font=numfont,
  bg='#222222',
  fg='#01FF70',
  relief=FLAT
  )

moneypersec = StringVar()
moneypersec.set(mpsnum)

mps = Label(
  root,
  textvariable = moneypersec,
  fg='#01FF70',
  bg='#111111',
  font = mpsfont
  )

num.grid(row=0, column=0, columnspan=4, pady=20)

for i in range(6):
  for j in range(4):
    buttonFrame[i][j].grid(row=i+1, column=j, padx=84, pady=10)

for i in range(len(item_button)):
  item_button[i].grid(row=i%6+1, column=i//6, padx=84, pady=10)

mps.grid(row=12, column=0, pady=10, columnspan=4)

root.bind('<Enter>', button_on_enter)
root.bind('<Leave>', button_on_leave)

def current_money():
    data['balance']+=data['rps']
    return str(ShortScale(int(data['balance'])))+' root'

now = StringVar()
num["textvariable"] = now

def onUpdate():
  now.set(current_money())
  json.dump(data, open('game.json', 'w'))
  num.after(500, onUpdate)

onUpdate()

root.mainloop()
