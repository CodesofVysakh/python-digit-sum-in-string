string = "hello123456letmetry"
sum_ = 0

for digit in string:
    if digit.isdigit():
        sum_ = sum_ + int(digit)

print("Sum: ", sum_)