from pywinauto import Desktop, Application

app = Application().Start(cmd_line=u'"D:\\Program Files\\Double Commander\\doublecmd.exe"')
dclass = app.DClass
dclass.Wait('ready')
menu_item = dclass.MenuItem(u'C&onfiguration->&Options...')
menu_item.Click()

# app.Double_Commander.print_control_identifiers()

