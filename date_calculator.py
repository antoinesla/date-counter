from datetime import datetime
import os

def get_date_from_string(date_input):
    '''
    returns False if input is not a date, 
    otherwise returns input as datetime object
    '''
    # TODO consider that date input without year before the current date is 
    #   next year
    # TODO add shortcuts for common dates (e.g. before Christmas and end 
    #   of financial year)

    only_day_month = False

    # split date input to count how many elements the user input
    input_list = date_input.split('/')

    # add current year if input doesn't mention it
    if len(input_list) == 2:
        date_input += f'/{datetime.now().year}'
        only_day_month = True
    
    try:
        date_object = datetime.strptime(date_input, "%d/%m/%Y")
        if only_day_month:
            if date_object < datetime.now():
                date_object = date_object.replace(year=2022)
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

def print_dates(first_date, second_date):
    '''prints start and end of therapy dates in a nice format'''
    

def main():
    '''main function that loops and asks for user input'''
    # TODO refactor so that user input is put into a function

    # clear terminal (called in main loop)
    clear = lambda: os.system('cls')

    while True:
        clear()
        user_input = ''


        print("enter 'quit' to quit the application")

        first_date, second_date = '', ''

        while not get_date_from_string(user_input):
            user_input = input('enter first date: ')
            if get_date_from_string(user_input): 
                first_date = get_date_from_string(user_input)
            elif user_input == 'quit':
                break
            else:
                print('incorrect date')
        
        if user_input == 'quit': break

        user_input = ''
        while not get_date_from_string(user_input):
            user_input = input('enter second date: ')
            if get_date_from_string(user_input): 
                second_date = get_date_from_string(user_input)
            elif user_input == 'quit':
                break
            else:
                print('incorrect date')

        if user_input == 'quit': break


        if first_date == second_date:
            print('these are the same dates')
        elif first_date > second_date:
            # write and use print dates method 
            print(f'start of therapy: {first_date}')
            print(f'end of therapy: {second_date}')
            print('first date is further in the futur than second date')
        else:
            # write and use print dates method 
            delta = second_date - first_date
            print(f'start of therapy: {first_date}')
            print(f'end of therapy: {second_date}')
            print(format_timedelta(delta))


        # wait for user to press enter before starting loop again
        while True:
            input('press enter to restart')
            break

if __name__ == '__main__':
    main()