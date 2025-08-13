from datetime import datetime as dt

def getDate():
    try:
        str_date=str(input(': '))
        datee=dt.strptime(str_date,'%Y-%m-%d').date()
        return True,datee
    except ValueError:
        print('Invalid Date Formate...')
        return False,''
    