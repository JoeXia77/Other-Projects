# Calculate-Pi
Aim: Calculate the value of Pi, like 10000 digit accuracy

Language: Python 3

points I learned from programming it:
1. for high precision, need more digit to contain an number so, 
  import decimal
	use a = decimal.Decimal(number) and a**2 and a.sqrt() to solve it

2. after prove this method is right, we want to know:
	if you want keep it accurate at 10000th digit, how many loops you need to run 
  the conclusion is you need to run 10000 * 1.6590389016018308 + 20 (plus 20 for safty, you know float number is not that accurate and the tendency calculated by graph also has  a little error, so extra looping times are needed to achiece the result)
	
Note: it will take too much time to run 10000 digit accuracy currently, but under 3000 digits will be fine.















