def calculator(num1,num2,operation):
   if(operation == "+"):
    result = num1 + num2
   elif(operation == "-"):
     result = num1 - num2
   elif(operation == "*"):
     result =  num1 * num2
   elif(operation == "/"):
     result =  num1 / num2 
   else:
     return "Invalid operation. Please use +, -, *, or /."
   return result

print(calculator(5, 3, '-')) 
print(calculator(5, 3, '*'))  
print(calculator(5, 3, '/'))  
print(calculator(5, 3, '+'))  
print(calculator(5, 3, '^'))  