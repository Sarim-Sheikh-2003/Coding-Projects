# calculator.py
# Sheikh Sarim, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
first_value = int(input('Enter First Value = '))                 #input for the first value
second_value = int(input('Enter Second Value = '))                   #input for the second value
third_value = int(input('Enter Third value = '))                   #input for the third value
first_operator = str(input('Enter First Operator = '))                   #input for first operator
second_operator = str(input('Enter Second Operator = '))                 #input for second operator

print('')
print('Entered Expression:', first_value, first_operator, second_value, second_operator, third_value)                  #output of the expression for the entered values and operators

#if the first and second operator is equal to the mathmatical symbol stated in the if and elif statements then the first, second and third values will be put into the equation corresponding to the if/elif statements. 
if first_operator == '+' and second_operator == '-':                    #addition as first operator and subtraction as second operator
    solution = first_value + second_value - third_value                 #equation to find the solution for the input values and operators
    print('Your final answer =', solution)                                    #solution output for the equation written above

elif first_operator == '-' and second_operator == '+':                  #subtraction as first operator and addition as second operator
    solution = first_value - second_value + third_value                 
    print('Your final answer =', solution)                                    

elif first_operator == '+' and second_operator == '+':                  #addition as first and second operator 
    solution = first_value + second_value + third_value                 
    print('Your final answer =', solution)                                    

elif first_operator == '-' and second_operator == '-':                  #subtraction as first and second operator
    solution = first_value - second_value - third_value                 
    print('Your final answer =', solution)                                    

elif first_operator == '*' and second_operator == '+':                  #multiplication as first operator and addition as second operator
    solution = first_value * second_value + third_value                 
    print('Your final answer =', solution)                                    

elif first_operator == '*' and second_operator == '-':                  #multiplication as first operator and subtraction as second operator
    solution = first_value * second_value - third_value                 
    print('Your final answer =', solution)                                    

elif first_operator == '+' and second_operator == '*':                  #addition as first operator and multiplication as second operator
    solution = first_value + second_value * third_value
    print('Your final answer =', solution)

elif first_operator == '-' and second_operator == '*':                  #subtraction as first operator and multiplication as second operator
    solution = first_value - second_value * third_value
    print('Your final answer =', solution)

elif first_operator == '/' and second_operator == '-':                  #division as first operator and subtraction as second operator
    solution = first_value // second_value - third_value
    print('Your final answer =', solution)

elif first_operator == '-' and second_operator == '/':                  #subtraction as first operator and division as second operator
    solution = first_value - second_value // third_value
    print('Your final answer =', solution)

elif first_operator == '/' and second_operator == '+':                  #division as first operator and addition as second operator
    solution = first_value // second_value + third_value
    print('Your final answer =', solution)

elif first_operator == '+' and second_operator == '/':                  #addition as first operator and division as second operator
    solution = first_value + second_value // third_value
    print('Your final answer =', solution)

elif first_operator == '/' and second_operator == '*':                  #division as first operator and multiplication as second operator
    solution = first_value // second_value * third_value
    print('Your final answer =', solution)

elif first_operator == '*' and second_operator == '/':                  #multiplication as first operator and division as second operator
    solution = first_value * second_value // third_value
    print('Your final answer =', solution)

elif first_operator == '*' and second_operator == '*':                  #multiplication as first and second operator
    solution = first_value * second_value * third_value
    print('Your final answer =', solution)

elif first_operator == '/' and second_operator == '/':                  #division as first and second operator
    solution = first_value // second_value // third_value
    print('Your final answer =', solution)

else:
    print('Invalid Operator Entry')                                     #output if there is an invalid entry for the operators