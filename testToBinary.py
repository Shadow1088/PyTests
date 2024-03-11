test_str = "binary"

print("The original string: " + test_str)

res = ''.join(format(ord(i), '08b') for i in test_str)

print("In binary: " + res)