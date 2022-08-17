def liters_100km_to_miles_gallon(liters):
    res = 3.785411784/0.01609344/liters
    return res

def miles_gallon_to_liters_100km(miles):
    res = 3.785411784/0.01609344/miles
    return res

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
