import csv
import sys
from person import Person
import csv

def open_csv(file_name):
    person_list = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')

        for line in reader:
            person_list.append(Person(line[0], line[1]))




def get_csv_file_name(argv_list):
    if len(argv_list) == 1:
        return
    return argv_list[1]


def format_output(person):
    if person == None:
        return "No match found."
    return "This number belongs to: " + person.name

def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if person.is_phone_number_matching(user_input_phone_number):
            return person


def main():
    file_name = get_csv_file_name(sys.argv)

    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
