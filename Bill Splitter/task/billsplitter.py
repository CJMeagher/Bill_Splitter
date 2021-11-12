import random

guest_dict = {}


def get_guests():
    print('Enter the number of friends joining (including you):')
    guest_qty = input()
    assert (guest_qty.isdigit()) and (int(guest_qty) > 0)
    print('\n' + 'Enter the name of every friend (including you), each on a new line:')
    for _ in range(int(guest_qty)):
        guest = input()
        guest_dict[guest] = 0.0
    print()


def split_bill(bill):
    for k in guest_dict.keys():
        guest_dict[k] = round((bill / len(guest_dict)), 2)


def get_lucky_guest():
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if input() == 'Yes':
        return random.choice(list(guest_dict.keys()))


try:
    get_guests()
    assert len(guest_dict) > 0
    print('Enter the total bill value:')
    bill_value = int(input())
    print()
    lucky_guest = get_lucky_guest()
    if lucky_guest:
        print(f'{lucky_guest} is the lucky one!')
        del guest_dict[lucky_guest]
    else:
        print('No one is going to be lucky')
    split_bill(bill_value)
    if lucky_guest:
        guest_dict[lucky_guest] = 0.0
    print(guest_dict)
except AssertionError:
    print('No one is joining for the party')
