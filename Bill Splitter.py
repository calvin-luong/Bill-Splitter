preTotal = 0.00
tip = 0.00
tax = 0.00
postTotal = 0.00
tipPercent = 0.00
taxPercent = 0.00

# Prompts the user to input preTotal, tip, tax


def scanner():
    global preTotal
    global tip
    global tax
    global postTotal
    cycle = True

    # Getting preTotal
    while cycle:
        # Scanner
        inputTotal = input("enter the total of all the items: \n")
        inputTotal = check_number(inputTotal)

        # Checking if valid input
        if inputTotal >= 0:
            preTotal = inputTotal
            cycle = False
        else:
            print("Please enter a valid input")

    cycle = True

    # Getting tip
    while cycle:
        # Scanner
        inputTip = input("enter the tipped amount: \n")
        inputTip = check_number(inputTip)

        # Checking if valid input
        if inputTip >= 0:
            tip = inputTip
            cycle = False
        else:
            print("Please enter a valid input")

    cycle = True

    # Getting tax
    while cycle:
        # Scanner
        inputTax = input("enter the tax: \n")
        inputTax = check_number(inputTax)

        # Checking if valid input
        if inputTax >= 0:
            tax = inputTax
            cycle = False
        else:
            print("Please enter a valid input")

    postTotal = preTotal + tip + tax


def check_number(input):
    try:
        # Convert it into float with 2 decimal points
        val = "{:.2f}".format(float(input))
        return float(val)
    except ValueError:
        return -1


def setPercentage():
    global taxPercent
    global tipPercent
    taxPercent = tax / preTotal
    tipPercent = tip / preTotal


def spliiter():
    return 0


# Runner method
if __name__ == "__main__":
    scanner()
    print("input " + str(preTotal) + " " + str(tip) +
          " " + str(tax) + " " + str(postTotal))
    setPercentage()
