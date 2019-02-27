import datetime

def format_date(day, month, year):
    correctDate = None
    try:
        correctDate = datetime.date(year, month, day)
        correctDate = correctDate.strftime("%d %B %Y")
    except ValueError:
        correctDate
    return correctDate

d = format_date(1, 2, 2019)
print(d)