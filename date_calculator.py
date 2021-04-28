import datetime
import os

def get_date_from_string(date_input):
    '''
    returns False if input is not a date, 
    otherwise returns input as date time object
    '''
    # TODO consider that date input without year before the current date is 
    #   next year
    # TODO add shortcuts for common dates (e.g. before Christmas and end 
    #   of financial year)

    # split date input to count how many elements the user input
    input_list = date_input.split('/')
    # add current year if input doesnt mention it
    if len(input_list) == 2 :
        date_input += f'/{datetime.datetime.now().year}'
    try:
        date_object = datetime.datetime.strptime(date_input, "%d/%m/%Y")
    except ValueError:
        return False
    else:
        return date_object

def format_timedelta(delta):
    '''returns nicely formatted delta as string with weeks and days'''
    formatted_time_delta = ''

    # checking how many weeks (if any) there are
    if  delta.days // 7 == 1:
        formatted_time_delta += '1 week'
    elif delta.days // 7 >= 2:
        formatted_time_delta += f'{delta.days // 7} weeks'

    # checking if there are both weeks AND days
    if delta.days // 7 >= 1 and delta.days % 7 != 0:
        formatted_time_delta += ', '
    
    # checking how many days (if any) there are
    if delta.days % 7 == 1:
            formatted_time_delta += '1 day'
    elif delta.days % 7 != 0:
        formatted_time_delta += f'{delta.days % 7} days'

    return formatted_time_delta

def main():
    '''main function that loops and asks for user input'''
    # TODO refactor so that user input is put into a function
    while True:
        # clear terminal
        clear = lambda: os.system('cls')
        clear()

        first_date, second_date = '', ''

        user_input = input('enter first date: ')
        if user_input == 'quit': break
        elif get_date_from_string(user_input): 
            first_date = get_date_from_string(user_input)

        user_input = input('enter second date: ')
        if user_input == 'quit': break
        elif get_date_from_string(user_input): 
            second_date = get_date_from_string(user_input)

        
        if first_date != second_date:
            delta = second_date - first_date
            print(format_timedelta(delta))
        else:
            print('these are the same dates')

        while True:
            input('press enter to restart')
            break

main()