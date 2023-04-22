import calendar
dob = input("Enter your date of birth (dd/mm/yyyy): ")
dob_year = int(dob.split('/')[2])
dob_month = int(dob.split('/')[1])
print(calendar.month(dob_year, dob_month))
