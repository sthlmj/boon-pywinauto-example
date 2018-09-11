from pywinauto import Desktop, Application

app = Application().start('pidgen.exe')

app.PIDGen.edit2.set_text('aaaa')
app.PIDGen.edit3.set_text('bbb')
app.PIDGen.OK.click()
