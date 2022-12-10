'''
def measurements(user_input):
    print("test")
    print(user_input)
    a = ''.join(user_input)
    print(a)
    if  (['to', 'liters'] in a or ['how', 'many', 'liters'] in user_input) and "cups" in a:  #current issue is that the user input is being broken down into a list of strings so they are all seperate words therfore does
        #not recognize, need to concatenate string somehow
        try:
            num_of_cups = int(user_input[user_input.index("cups") - 1])
            num_of_liters = num_of_cups * 0.236588
            print(num_of_liters)
            print("test")
        except ValueError:
            print("Could not compute amount, please repeat")
            '''
