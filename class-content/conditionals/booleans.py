is_raining = True
is_cold = False

print(is_raining)
print(is_cold)

print(not is_raining)

is_raining = False
is_cold = False
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)

is_raining = False
is_cold = True
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)


is_raining = False
is_cold = False
print(is_raining or is_cold)

is_raining = False
is_cold = True
print(is_raining or is_cold)


