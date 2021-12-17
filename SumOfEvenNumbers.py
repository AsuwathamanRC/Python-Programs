sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)

#or

sum = 0
for i in range(1,101):
    if i%2==0:
        sum += i
print(sum)