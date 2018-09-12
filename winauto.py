# Another pywinautu example

from pywinauto import Desktop, Application, keyboard
import time

# Open Calculator in Windows 10 and do some calculation
app = Application(backend='uia').start("calc.exe")
dlg = Desktop(backend="uia").Calculator
dlg.type_keys('3')
# Add some delay between each key stroke
time.sleep(1)
dlg.type_keys('/')
time.sleep(1)
dlg.type_keys('7')
time.sleep(1)
dlg.type_keys('=')
# Get calculation result
txt = dlg.Static3.texts()
# Get only the numeric value
txt = txt[0].split(' ')[2]

# Open Notepad from Windows 10
app2 = Application(backend='uia').start("notepad.exe")
time.sleep(1)
app2.Untitled.edit.type_keys(txt)
time.sleep(1)
# All {key code} are self explained
keyboard.SendKeys('{ENTER}')
app2.Untitled.edit.type_keys(u'Automate{SPACE}any{SPACE}Windows{SPACE}Application')
keyboard.SendKeys('{ENTER}')
app2.Untitled.edit.type_keys(u'BY...{ENTER}Python')



