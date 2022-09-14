# encryption.py
# Sheikh Muhammad Sarim, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.




### Define your functions here
def creating_dict_function(keys,values):
    '''This function creates a dictionary using two list,
    one which contains the alphabet and one which contains the cypher.
    For encoding the alphabet is the key while the cypher is the value,
    and for decoding the alphabet is the value while the cypher is the key'''
    new_dict = dict(zip(keys,values))
    return new_dict

def output_function(text,cipher_dict): 
    '''This function uses the dictionary created by the above function,
    to create a new encoded or decoded output string based on the type of dictionary
    that was created and the process that the user intended.'''
    output_text = ''
    i = 0
    while i < len(text):
        if text[i] in cipher_dict.keys():
            output_text += cipher_dict[text[i]]
        i += 1
    
    return output_text

def print_statement():
    '''This function only exists because I was forced to make 3 functions.
    This function prints the final goodbye statement'''
    print('Thank you for using the encryption program.')

### Add your main program code here
print('ENDG 233 Encryption Program')
alphabet = list('abcdefghijklmnopqrstuvwxyz')               #List that contains all the alphabets which is used in the formation of the dictionary
process_type = input('Select 1 to encode or 2 to decode your message, select 0 to to quit: ')               #Initial input to figure out what actions the code must do wehether to encode, decode or to end the program

while process_type != '0':              #This loop uses the above input informaation to carry out the action that was inputted as long as the loop does not end when the user inputs 0
    user_cipher = str(input('Please enter the Cipher text: ').lower())              #Asks for the cypher from the user in the form of a string and turns all of the characters into lowercase 
    x = 0
    while x == 0:               #This loop is used to check the cypher as long as x is equal to 0, if x is not equal to 0 the loop will end and the code will move on
        if len(set(user_cipher)) != 26 or not user_cipher.isalnum():                #This if statement makes sure wether the cypher fits the criteria given and if it doesn't it requires the user to input a cypher that does fit the criteria
            print('Your cipher must contain 26 unique elements of a-z or 0-9')
            user_cipher = str(input('Please enter the Cipher text: ').lower())
        else:               #If the cypher fits the criteria this else statement changes the value of x to 1 so the loop gets broken
            print('Your Cipher is valid.')
            x = 1

    if process_type == '1':             #If the user inputs 1 as the process that the code must do then this if statement carries out that process
        user_text = str(input('Please enter the text to be processed: '))               #Prompts the user to input the text that must be encoded
        print(f'Your Output is: {output_function(user_text,creating_dict_function(alphabet,list(dict.fromkeys(list(user_cipher)))))}')              #Uses the information inputted by the user to get the result by calling upon the function that creates the dictionary and inputting that dictionary into the function that gives the encoded result 
        process_type = input('Select 1 to encode or 2 to decode your message, select 0 to to quit: ')               ##Prompts the user for what actions must the code do now
    elif process_type == '2':               #If the user inputs 2 as the process that the code must do then this elif statement carries out that process
        user_text = str(input('Please enter the text to be processed: '))               #Prompts the user to input the text that must be decoded
        print(f'Your Output is: {output_function(user_text,creating_dict_function(list(dict.fromkeys(list(user_cipher))),alphabet))}')              #Uses the information inputted by the user to get the result by calling upon the function that creates the dictionary and inputting that dictionary into the function that gives the decoded result
        process_type = input('Select 1 to encode or 2 to decode your message, select 0 to to quit: ')               #Prompts the user for what actions must the code do now
    else:               #If the user inputs a value that is not mentioned in the prompt, as the process that the code must do then this else statement reminds the user to input a value from the ones that were mentioned in the prompt and breaks the loop
        print('Invalid Selection Entry.')
        break

print_statement()               #Calls upon the third function to print the goodbye statement