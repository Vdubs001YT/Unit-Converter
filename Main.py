Unit = str(input("Unit:"))
Number = float(input("Number:"))
Convert2 = str(input("Converting to:"))

#Metric units
if Unit == "cm" and Convert2 == "m":
    print(Number/100)

if Unit == "m" and Convert2 == "cm":
    print(Number*100)

if Unit == "mm" and Convert2 == "cm":
    print(Number*10)

if Unit == "km" and Convert2 == "m":
    print(Number*1000)

if Unit == "m" and Convert2 == "km":
    print(Number/1000)

if Unit == "mm" and Convert2 == "cm":
    print(Number/10)

if Unit == "km" and Convert2 == "mm":
    print(Number*1000000)

if Unit == "mm" and Convert2 == "km":
    print(Number/1000000)

if Unit == "m" and Convert2 == "mm":
    print(Number*1000)

if Unit == "mm" and Convert2 == "m":
    print(Number/1000)

if Unit == "mm" and Convert2 == "cm":
    print(Number/10)

if Unit == "cm" and Convert2 == "mm":
    print(Number*10)

if Unit == "cm" and Convert2 == "m":
    print(Number/100)

if Unit == "m" and Convert2 == "cm":
    print(Number*100)

if Unit == "km" and Convert2 == "cm":
    print(Number*1000000)

if Unit == "km" and Convert2 == "cm":
    print(Number/1000000)

if Unit == "km" and Convert2 == "m":
    print(Number*1000)

if Unit == "m" and Convert2 == "km":
    print(Number/1000)

#freedom units

if Unit == "foot" and Convert2 == "m":
    print(Number/3.281)

if Unit == "m" and Convert2 == "foot":
    print(Number*3.281)

if Unit == "foot" and Convert2 == "mm":
    print(Number*304.8)

if Unit == "foot" and Convert2 == "mm":
    print(Number/304.8)

