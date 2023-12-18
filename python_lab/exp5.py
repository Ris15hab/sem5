class HighValueError(Exception):
    pass
class LowValueError(Exception):
    pass

while True:
    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        if num1>100 or num2>100:
            raise HighValueError
        if num1<0 or num2<0:
            raise LowValueError
        result = num1/num2
    except ValueError:
        print("Invalid input! Please enter an integer")
        print()
    except RuntimeError:
        print("Runtime Error occrued")
        print()
    except ZeroDivisionError:
        print("Can't divide by zero")
        print()
    except ImportError:
        print("Import error occured")
        print()
    except KeyboardInterrupt:
        print("keyboard interrupt... exiting the code")
        print()
    except SyntaxError:
        print("Syntax error in code")
        print()
    except HighValueError:
        print("value too high ... enter value in the range of 0-100")
        print()
    except LowValueError:
        print("value too low ... enter value in the range of 0-100")
        print()
    else:
        print(f"Result: {result}")
        break