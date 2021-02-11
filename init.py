def main():
    digits = input("Please enter a three-digit number: ")
    sum = 0

    if len(digits) < 3:
        print("The value you entered doesn't has 3 digits.")
    elif not digits.isnumeric():
        print("You have not entered a numeric value")
    else:
        for digit in list(digits):
            sum += int(digit)
    print(f'The sum is {sum}.')
    return None

if __name__ == '__main__':
    main()
    