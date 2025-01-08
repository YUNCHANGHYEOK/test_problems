from datetime import date


birth_year, birth_month, birth_day = map(int, input().split())
current_year, current_month, current_day = map(int, input().split())


birth_date = date(birth_year, birth_month, birth_day)
current_date = date(current_year, current_month, current_day)


age = current_year - birth_year
if (current_month, current_day) < (birth_month, birth_day):
    age -= 1


count_age = current_year - birth_year + 1


year_age = current_year - birth_year

print(age)
print(count_age)
print(year_age)
