list1 = [0, 1, 2, 3, 4, 5]

class errors:
    IndexError = "< ! > INDEX ERROR >> out of range"
    TypeError = "< ! > TYPE ERROR"
    ValueError = "< ! > VALUE ERROR >> invalid value"
    ZeroDivisionError = "< ! > ZERO DIVISION ERROR"


try:
    print(list1[5])

except IndexError:
    print(errors.IndexError)
except TypeError:
    print(errors.TypeError)
except ValueError:
    print(errors.ValueError)
except ZeroDivisionError:
    print(errors.ZeroDivisionError)
else:
    print("No errors")

finally:
    print("The code has run")