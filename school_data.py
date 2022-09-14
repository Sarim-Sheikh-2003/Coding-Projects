# school_data.py
# Sheikh Muhammad Sarim, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays
school_names = { 'Centennial High School': '1224',                  #This Dictionary contains the names of all the schools and their corresponding codes
        'Robert Thirsk School': '1679',
        'Louise Dean School': '9626',
        'Queen Elizabeth High School': '9806',
        'Forest Lawn High School': '9813',
        'Crescent Heights High School': '9815',
        'Western Canada High School': '9816',
        'Central Memorial High School': '9823',
        'James Fowler High School': '9825',
        'Ernest Manning High School': '9826',
        'William Aberhart High School': '9829',
        'National Sport School': '9830',
        'Henry Wise Wood High School': '9836',
        'Bowness High School': '9847',
        'Lord Beaverbrook High School': '9850',
        'Jack James High School': '9856',
        'Sir Winston Churchill High School': '9857',
        'Dr. E. P. Scarlett High School': '9858',
        'John G Diefenbaker High School': '9860',
        'Lester B. Pearson High School': '9865'}

schooldata_2018_to_2019 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)                    #imports the SchoolData_2018_2019 excel file as an array and then equates to a variable
schooldata_2019_to_2020 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)                    #imports the SchoolData_2019_2020 excel file as an array and then equates to a variable
schooldata_2020_to_2021 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)                    #imports the SchoolData_2020_2021 excel file as an array and then equates to a variable

# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    '''The bottom three lines of codes the arrays that were imported from the excel files'''
    print('Array data for 2020 - 2021:\n', schooldata_2020_to_2021)
    print('Array data for 2019 - 2020:\n', schooldata_2019_to_2020)
    print('Array data for 2018 - 2019:\n', schooldata_2018_to_2019)

    # Add request for user input here
    user_input = str(input('Please enter the high school name or school code: '))                   #Prompts for the initial input from the user which can be the name of the school or its corresponding code
    x = True
    while x == True:                     #This loop verifies wehther the input from the user is in the dictionary which contains the names of the schools and their codes 
        if user_input in school_names.keys():                       #If the user inputted a name of a school then this if statement verifies if the input is in the list containing the school names, which is derived from the original dictionary
            x = False                   #If the if statement is correct then x becomes false which breakes the loop
        elif user_input in school_names.values():                   #If the user inputted a code of a school then this elif statement verifies if the input is in the list containing the school codes, which is derived from the original dictionary
            x = False
        else:                   #If both the above if and elif statements are not false then this else statement prompts the user to retype a valid input
            print('You munst enter a valid school name or code.')
            user_input = str(input('Please enter the high school name or school code: '))
            x = True
    
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    '''The bottom two lines of code turn the dictionary into lists, one for keys and one for values'''
    school_names_key_list = list(school_names.keys())
    school_names_values_list = list(school_names.values())
    if user_input in school_names_key_list:                 #This if statement takes the user input and if it is a name of the school it finds the corresponding code
        school_code = school_names_values_list[school_names_key_list.index(user_input)]                 #This line of code finds the index at which the school name exists in the list of the school names and uses that index in the list containing the code to find the corresponding code
        school_name = user_input
    elif user_input in school_names_values_list:                    #This if statement takes the user input and if it is the code of the school it finds the corresponding school name
        school_name = school_names_key_list[(school_names_values_list.index(user_input))]                   #This line of code finds the index at which the school code exists in the list of the school codes and uses that index in the list containing the school names to find the corresponding name of the school
        school_code = user_input

    school_object = School(school_name, school_code)                    #Creates an object which is related to the class
    school_object.print_all_stats()                 #Uses the object in the class to print the name of the school and its code

    # Add data processing and plotting here
    i = 0
    for i in range(len(school_names_values_list)):                  #This if statement finds the index at which the school code exists in the list containing all the codees
        if school_names_values_list[i] == school_code:
            array_index = i
            
    mean_enrolement_grade10 = (schooldata_2018_to_2019[array_index][1] + schooldata_2019_to_2020[array_index][1] + schooldata_2020_to_2021[array_index][1]) // 3                    #Uses the index found above and plugs into the three imported arrays to find the value corresponding to the code in the first column and then adds the three values and divides by three to find the average 
    print(f'Mean enrollment for Grade 10: {mean_enrolement_grade10:.0f}')               #Prints the value that was found in the above line of code
    mean_enrolement_grade11 = (schooldata_2018_to_2019[array_index][2] + schooldata_2019_to_2020[array_index][2] + schooldata_2020_to_2021[array_index][2]) // 3                    #Uses the index found above and plugs into the three imported arrays to find the value corresponding to the code in the second column and then adds the three values and divides by three to find the average
    print(f'Mean enrollment for Grade 11: {mean_enrolement_grade11:.0f}')
    mean_enrolement_grade12 = (schooldata_2018_to_2019[array_index][3] + schooldata_2019_to_2020[array_index][3] + schooldata_2020_to_2021[array_index][3]) // 3                    ##Uses the index found above and plugs into the three imported arrays to find the value corresponding to the code in the third column and then adds the three values and divides by three to find the average
    print(f'Mean enrollment for Grade 12: {mean_enrolement_grade12:.0f}')
    total_graduates = (schooldata_2018_to_2019[array_index][3] + schooldata_2019_to_2020[array_index][3] + schooldata_2020_to_2021[array_index][3])                 #Finds the three values in the third column from the three imported arrays and adds them to find the total
    print(f'Total number of students who graduated in the past three years: {total_graduates:.0f}')

    plt.figure(1)
    grade_level = np.array([10, 11, 12])                    #Makes an array containg all the grade levels
    enrolled_student_2020_to_2021 = np.array([schooldata_2020_to_2021[array_index][1], schooldata_2020_to_2021[array_index][2], schooldata_2020_to_2021[array_index][3]])                   #Creates an array with the number of all the students enrolled in 2020 to 2021
    enrolled_student_2019_to_2020 = np.array([schooldata_2019_to_2020[array_index][1], schooldata_2019_to_2020[array_index][2], schooldata_2019_to_2020[array_index][3]])                   #Creates an array with the number of all the students enrolled in 2019 to 2020
    enrolled_student_2018_to_2019 = np.array([schooldata_2018_to_2019[array_index][1], schooldata_2018_to_2019[array_index][2], schooldata_2018_to_2019[array_index][3]])                   #Creates an array with the number of all the students enrolled in 2018 to 2019
    '''The bottom three lines of code plot the three arrays above on the fraph with respects to the array containg the grade levels as well as the formatting that the graph needs to have'''
    plt.plot(grade_level, enrolled_student_2020_to_2021, 'ob', label = '2021 Enrollment')
    plt.plot(grade_level, enrolled_student_2019_to_2020, 'og', label = '2020 Enrollment')
    plt.plot(grade_level, enrolled_student_2018_to_2019, 'or', label = '2019 Enrollment')
    plt.xticks(grade_level)                 #Formats the x axis to only show the values in the array and nothing else
    plt.title('Grade Enrollement by Year')                  #Adds a title to the graph that is created
    plt.xlabel('Grade Level')                   #labels the x axis
    plt.ylabel('Number of Students')                    #labels the y axis
    plt.legend()                    #cretaes a legend

    plt.figure(2)
    school_year = np.array([2019, 2020, 2021])                    #Makes an array containg the three years from the data provided
    enrolled_student_grade10 = np.array([schooldata_2018_to_2019[array_index][1], schooldata_2019_to_2020[array_index][1], schooldata_2020_to_2021[array_index][1]])                     #Creates an array with the number of students enrolled in the grade 10 levels in the three years
    enrolled_student_grade11 = np.array([schooldata_2018_to_2019[array_index][2], schooldata_2019_to_2020[array_index][2], schooldata_2020_to_2021[array_index][2]])                     #Creates an array with the number of students enrolled in the grade 11 levels in the three years
    enrolled_student_grade12 = np.array([schooldata_2018_to_2019[array_index][3], schooldata_2019_to_2020[array_index][3], schooldata_2020_to_2021[array_index][3]])                     #Creates an array with the number of students enrolled in the grade 12 levels in the three years
    plt.subplot(3, 1, 1)                    #This code makes sure that instead of one graph containing all the information like figure 1 the information is seperated into seperate graphs, in this case this means that the figure will have three rows and one column and the graph that is created will be in the first row
    plt.plot(school_year, enrolled_student_grade10, linestyle = '--', color = 'gold', label = 'Grade 10')                   #plots the first of the three arrays relative to the array containing the three years and specifies the formatting of the graph
    plt.ylabel('Number of Students')                    #Labels the y axis of the graph
    plt.xticks(school_year)                 #Formats the x axis to only show the values in the array and nothing else
    plt.title('Enrollment by Grade')                    #Gives a title to the graph
    plt.legend()                    #Cretaes a legend
    plt.subplot(3, 1, 2)                    #Specifies that the next graph in the figure created will be in the second row
    plt.plot(school_year, enrolled_student_grade11, linestyle = '--', color = 'magenta', label = 'Grade 11')                    #plots the second of the three arrays relative to the array containing the three years and specifies the formatting of the graph
    plt.ylabel('Number of Students')                    #Labels the y axis of the graph
    plt.xticks(school_year)                 #Formats the x axis to only show the values in the array and nothing else
    plt.legend()                    #Creates a legend
    plt.subplot(3, 1, 3)                    #Specifies that the next graph in the figure will be in the third row
    plt.plot(school_year, enrolled_student_grade12, linestyle = '--', color = 'cyan', label = 'Grade 12')                    #plots the third of the three arrays relative to the array containing the three years and specifies the formatting of the graph
    plt.ylabel('Number of Students')                    #Labels the y axis of the graph
    plt.xlabel('Enrollment Year')                   #Labels the x axis of the graph
    plt.xticks(school_year)                 #Formats the x axis to only show the values in the array and nothing else
    plt.legend()                    #Creates a legend
    plt.show()

# Do not modify the code below
if __name__ == '__main__':
    main()