from datetime import datetime
import datetime
CurrentDate = datetime.datetime.now()

def datebyyearmonthday():
    CurrentYear, CurrentMonth, = CurrentDate.year, CurrentDate.month
    print("Digite el año en que nacio")
    BirthYear = int(input())
    print("Digite el mes en que nacio en digitos (1 es Enero, 2 Febrero, etc.)")
    BirthMonth = int(input())

# Logica detras del calculo, se considera si el mes actual es mayor al mes de nacimiento.
    if  BirthMonth >= CurrentMonth:
        Livingyears = (CurrentYear - BirthYear - 1)
        Livingmonths = (CurrentMonth + 12 - BirthMonth)
    else:
        Livingyears = CurrentYear - BirthYear
        Livingmonths = CurrentMonth - BirthMonth

    Totallivingmonths = Livingyears*12 + Livingmonths
    return Totallivingmonths
