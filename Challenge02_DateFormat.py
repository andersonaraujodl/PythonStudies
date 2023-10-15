print("I am gonna print your birthday date! Give me the information:")
day = input("Day (DD): ")
month = input("Month (MM): ")
year = input("Year (YYYY): ")
dateFormat = input("Choose a date format (type a number):\n1) Text \"You were born on...\""
                   "\n2) DD/MM/YYYY \n3) YYYY/MM/DD\n4) MM/DD/YYYY\n")
if dateFormat == str(1):
    monthText = "January"
    if month == "02":
        monthText = "February"
    elif month == "03":
        monthText = "March"
    elif month == "04":
        monthText = "April"
    elif month == "05":
        monthText = "May"
    elif month == "06":
        monthText = "June"
    elif month == "07":
        monthText = "July"
    elif month == "08":
        monthText = "August"
    elif month == "09":
        monthText = "September"
    elif month == "10":
        monthText = "October"
    elif month == "11":
        monthText = "November"
    elif month == "12":
        monthText = "December"
    print("You were born on", day, monthText, "of", year)
elif dateFormat == str(2):
    print("You were born on", day + "/" + month + "/" + year)
elif dateFormat == str(3):
    print("You were born on", year + "/" + month + "/" + day)
elif dateFormat == str(4):
    print("You were born on", month + "/" + day + "/" + year)