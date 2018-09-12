from pywinauto import Desktop, Application, keyboard

import time

app = Application(backend='uia').start("calc.exe")
dlg = Desktop(backend="uia").Calculator
dlg.type_keys('3')
time.sleep(1)
dlg.type_keys('/')
time.sleep(1)
dlg.type_keys('7')
time.sleep(1)
dlg.type_keys('=')
txt = dlg.Static3.texts()
txt = txt[0].split(' ')[2]

app2 = Application(backend='uia').start("notepad.exe")
time.sleep(1)
app2.Untitled.edit.type_keys(txt)
time.sleep(1)
keyboard.SendKeys('{ENTER}')
app2.Untitled.edit.type_keys(u'Automate{SPACE}any{SPACE}Windows{SPACE}Application')
keyboard.SendKeys('{ENTER}')
app2.Untitled.edit.type_keys(u'BY...{ENTER}Boon')



