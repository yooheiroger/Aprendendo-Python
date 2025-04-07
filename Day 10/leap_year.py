def leap_year (year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return  False
        else:
            return True
    else:
        return False


year = int(input('please enter the year: \n'))
leap = leap_year(year)
print(leap)
