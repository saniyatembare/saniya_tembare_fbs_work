#convret the time entered in hh,min and sec into second
hour = int(input('Enter the hours : '))
min = int(input('Enter the minutes : '))
sec = int(input('Enter the secounds : '))

Total_sec = (hour * 3600) + (min * 60) + sec

print(f'Total secounds is : {Total_sec}')