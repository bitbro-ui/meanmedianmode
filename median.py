import csv 
with open("C:/Users/arkma/Dropbox/My PC (DESKTOP-F2428EU)/Desktop/SOCR-HeightWeight.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    new_data = []
    for i in range(len(file_data)):
        number = file_data[i][1]
        new_data.append(float(number))
    n = len(new_data)
    new_data.sort()
    if n%2 == 0:
        med1 = float(new_data[n//2])
        med2 = float(new_data[n//2-1])
        med = (med1+med2)/2
    else :
        med = new_data[n//2]
        print(n)
    print("median is "+str(med))  