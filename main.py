#power of a number
def power(base,exponent):
    if exponent ==0:
        return 1
    else:
        #recursive case: multiply the base by the result of the power ( base, exponent-1 )
        #example 2^3 = 2(2,2)
        return base * power(base, exponent- 1)
    
base = int(input("enter base:"))
exponent = int(input("enter exponent"))

#calculate the power 
answer = power(base,exponent )
print(f"the base {base} to the power of {exponent} is: {answer}")
        

