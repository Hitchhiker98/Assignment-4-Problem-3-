def calculate_gcd(num1, num2):
  
    # if num2 is zero, we can stop right here and say num1 is the GCD
    if num2 == 0:
        return num1

    while num2:
        # we need a temporary spot to store num2 
        temp = num2
        
        # now, num2 becomes the remainder of num1 divided by the old num2
        num2 = num1 % num2
        
        # and num1 gets the old num2 from the temporary spot
        num1 = temp

    # when num2 finally hits zero, num1 is the GCD
    return num1


print(calculate_gcd(24, 7)) 





