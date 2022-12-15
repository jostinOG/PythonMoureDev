# Statement: Create a program to transform a decimal number to binary without using language functions that do it directly.
# Create a function that generates a decimal
def generate_decimal():
    import random
    return random.randint(1, 100)


# Create a function that converts a decimal to binary
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


def main():
    decimal = generate_decimal()
    print("Decimal: " + str(decimal))
    print("Binary: " + decimal_to_binary(decimal))


if __name__ == '__main__':
    main()
