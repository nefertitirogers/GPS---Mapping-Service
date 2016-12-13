


def get_address() -> list:
    ''' takes n lines of input and stores input into a list'''
    addresses = []

    number = int(input())

    for destinations in range(0, number):
        x = input()
        addresses.append(x)

    return addresses

def output_spec() -> list:
    ''' takes n lines of input and stores input into a list'''
    output = []

    number = int(input())

    for specifications in range (0, number):
        x = input().strip('').upper()
        output.append(x)

    return output





