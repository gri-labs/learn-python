from datetime import datetime
import datetime



def date_by_year_month():
    current_date = datetime.datetime.now()
    current_year, current_month = current_date.year, current_date.month
    print("Digite el año en que nacio")
    birth_year = int(input())
    print("Digite el mes en que nacio en digitos (1 es Enero, 2 Febrero, etc.)")
    birth_month = int(input())

# Logica detras del calculo, se considera si el mes actual es mayor al mes de nacimiento.
    if birth_month >= current_month:
        lived_years = (current_year - birth_year - 1)
        lived_months = (current_month + 12 - birth_month)
    else:
        lived_years = current_year - birth_year
        lived_months = current_month - birth_month

    total_lived_months = lived_years*12 + lived_months
    return total_lived_months
