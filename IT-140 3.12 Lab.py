input_month = input()
input_day = int(input())

valid_dates = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

if (input_month in valid_dates) and (0 < input_day <= valid_dates[input_month]):
    if ((input_month == "March") and (input_day >= 20)) or (input_month in ["April", "May"]) or ((input_month == "June") and (input_day <= 20)):
        print("Spring")
    elif ((input_month == "June") and (input_day > 20)) or (input_month in ["July", "August"]) or ((input_month == "September") and (input_day <= 20)):
        print("Summer")
    elif ((input_month == "September") and (input_day > 20)) or (input_month in ["October", "November"]) or ((input_month == "December") and (input_day <= 20)):
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
