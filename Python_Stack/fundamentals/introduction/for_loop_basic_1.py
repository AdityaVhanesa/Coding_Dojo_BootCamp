# Print all integers from 0 to 150

for i in range(151):
    print(i)


# Print all the multiple of fives in 5 to 1000

for i in range(5, 1000, 5):
    print(i)


# Print Dojo Way.

for i in range(101):
    if i % 5 == 0 and i % 10 != 0:
        print("Coding")
    elif i % 5 != 0 and i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
        
# Add integers
sum = 0
for i in range(500001):
    sum += i
    
print("Sum is --> {}".format(sum))

# Count Down By four
for i in range(2018, 0, -4):
    print(i)

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)

