score = input("Enter Score: ")
try:
    s = float(score)
except:
    s = -1
if s > 0:
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    elif s <= 0.6:
        print('F')
    else:
        print('The score is out of range. 0 > score < 1')
else:
    print('Please enter a decimal number: 0 > score < 1')
