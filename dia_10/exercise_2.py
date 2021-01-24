def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(eval_year, eval_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if is_leap(eval_year) :
      if eval_month == 2:
          return "Year is leap with 29 days"
      else:
          return f"Year is leap with {month_days[eval_month-1]} days"
  else:
      return f"Year is not leap with  {month_days[eval_month-1]} days"
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)