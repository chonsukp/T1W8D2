# try except block - try catch block

class NegativeError(Exception):
    pass

try: 
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n < 0 or d < 0:
        raise NegativeError("No negative numbers please!")

    q = n / d

    print(q)

except ZeroDivisionError:
    print("Denominator cannot be zero")

except ValueError:
    print("Please enter numbers only")

except NegativeError:
    print("Please donot put negative numbers")

except Exception as e:
    print(e)
    print("Something went wrong")

else:
    # whenever try block is successfully executed without throwing any exceptions
    print("Else block")

finally:
    # this will run at the end whether any error was thrown or not
    print("Finally block")


print("The end of the program!")

# file handiling example
# try:
    # open a file
    # try to do something
    # write into the file - it may thow error
# except:
    # do something to handle the error
# finally:
    # close the file