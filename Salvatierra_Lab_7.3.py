from datetime import date, datetime

NAPOLEON_BIRTHDAY = date(1769, 8, 15)
PEARL_HARBOR = date(1941, 12, 7)
FIRST_FLIGHT = date(1903, 12, 17)
DATE_FORMAT = '%m-%d-%Y'

def get_months_between_to_dates(newest_date, older_date):
    months = (newest_date.year - older_date.year) * 12\
        + (newest_date.month - older_date.month)
    
    if newest_date.day < older_date.day:
        months -= 1
    
    return months

def get_years_between_to_dates(newest_date, older_date):
    years = newest_date.year - older_date.year

    if newest_date.month < older_date.month or\
            (newest_date.month == older_date.month and 
             newest_date.day < older_date.day):
        years -= 1
    
    return years


print(
    'Enter the a valid date in the format MM-DD-YYYY, if the system cannont '
    'parse the string to a correct date the system will use the system '
    'current date'
)
current_date = input('Enter date (MM-DD-YYYY): ')
try:
    current_date = datetime.strptime(current_date, DATE_FORMAT).date()
    print(f'Using custom user date -> {current_date.strftime(DATE_FORMAT)}')
except ValueError:
    current_date = date.today()
    print(f'Using system current date -> {current_date.strftime(DATE_FORMAT)}')

print(
    f'It has been {(current_date - NAPOLEON_BIRTHDAY).days} days, or '
    f'{get_months_between_to_dates(current_date, NAPOLEON_BIRTHDAY)} months, '
    f'or {get_years_between_to_dates(current_date, NAPOLEON_BIRTHDAY)} years '
    'since the birthdate of Napoleon Bonaparte'
)
print(
    f'It has been {(current_date - PEARL_HARBOR).days} days, or '
    f'{get_months_between_to_dates(current_date, PEARL_HARBOR)} months, '
    f'or {get_years_between_to_dates(current_date, PEARL_HARBOR)} years '
    'since the bombing of Pearl Harbor'
)
print(
    f'It has been {(current_date - FIRST_FLIGHT).days} days, or '
    f'{get_months_between_to_dates(current_date, FIRST_FLIGHT)} months, '
    f'or {get_years_between_to_dates(current_date, FIRST_FLIGHT)} years '
    'since the Wright Brothers 1st flight'
)