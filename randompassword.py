import datetime

with open("words.txt") as file:
    lines = file.readlines()

password = ''
n = 13
while (len(password) <= 10):
    current = datetime.datetime.now()
    hours = int(current.strftime('%H'))
    minutes = int(current.strftime('%M'))
    seconds = int(current.strftime('%S'))

    if (len(password) == 0):
        password = password+(lines[hours*minutes])[:1]
    elif (len(password) <= 5):
        password = password+(lines[len(lines) % (seconds*n)])[:1]
    else:
        password = password+(lines[len(lines) % (3*n)])[:1]
    n -= 1

print(password)
