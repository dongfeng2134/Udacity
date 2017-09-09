#For Loops [demonstration]
print("The absolute value of", my_negative, "is", abs(my_negative))
print(my_integer, "squared is equal to", my_integer ** 2)
print("Does", my_fraction, "equal", my_float, "?", does_half_equal_point_five)


print("1 - demonstrating for loop")
for i in [0,1,2,3,4,5]:
    print(i)


print("2 - demonstrating for loop with range()")
for i in range(6):
    print(i)


for left_num in range(5):
    for right_num in range(5):
        product = left_num * right_num
        print(left_num, "x", right_num, "=", product)

