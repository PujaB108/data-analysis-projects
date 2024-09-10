# 1. Declare and assign the variables here:
ShuttleName = ('Determination')
ShuttleSpeed = 17500
Mars = 225000000
Moon = 384400
MilesPerKm = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
type(ShuttleName)
type(ShuttleSpeed)
type(Mars)
type(Moon)
type(MilesPerKm)

# Code your solution to exercises 3 and 4 here:
MilesToMars = Mars * MilesPerKm
HoursToMars = Mars / ShuttleSpeed
DaysToMars = HoursToMars / 24
print (ShuttleName + " will take " + str(DaysToMars) + " days to reach Mars.")

# Code your solution to exercise 5 here
MilesToMoon = Moon * MilesPerKm
HoursToMoon = Moon / ShuttleSpeed
DaysToMoon = HoursToMoon / 24
print (ShuttleName + " will take " + str(DaysToMoon) + " days to reach the Moon.")

