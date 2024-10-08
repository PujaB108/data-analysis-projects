engine_indicator_light = 'red blinking'
fuel_level = 21000
engine_temperature = 1200


# 5) Implement the following checks using if/else if/else statements:

# a) If fuel_level is above 20000 AND engine_temperature is at or below 2500, print "Full tank. Engines good."

# b) If fuel_level is above 10000 AND engine_temperature is at or below 2500, print "Fuel level above 50%.  Engines good."

# c) If fuel_level is above 5000 AND engine_temperature is at or below 2500, print "Fuel level above 25%. Engines good."

# d) If fuel_level is at or below 5000 OR engine_temperature is above 2500, print "Check fuel level. Engines running hot."

# e) If fuel_level is below 1000 OR engine_temperature is above 3500 OR engine_indicator_light is red blinking print "ENGINE FAILURE IMMINENT!" 

# f) Otherwise, print "Fuel and engine status pending..." 

# Code 5a - 5f here:
if fuel_level < 1000 or engine_temperature > 3500 or engine_indicator_light == 'red blinking':
    print("ENGINE FAILURE IMMINENT!")
elif fuel_level <= 5000 or engine_temperature > 2500:
    print("Check fuel level. Engines running hot.")
elif fuel_level > 20000 and engine_temperature <= 2500:
    print("Full tank. Engines good.")
elif fuel_level > 10000 and engine_temperature <= 2500:
    print("Fuel level above 50%. Engines good.")
elif fuel_level > 5000 and engine_temperature <= 2500:
    print("Fuel level above 25%. Engines good.")
else:
    print("Fuel and engine status pending...")
# The code returns the output "ENGINE FAILURE IMMINENT!". Line 21 begins the chained conditional.
# The boolean expression engine_indicator_light = "red blinking" evaluates to True in the or conditions.
# Neither line 24, line 26, line 28, line 30 or line 32 runs. Since line 22 is satisfied first,
# the rest of the conditionals are skipped.

# 6) a) Create the variable command_override, and set it to be true or false. If command_override is false, then the shuttle should only launch if the fuel and engine check are OK. If command_override is true, then the shuttle will launch regardless of the fuel and engine status.
command_override = True # Code 1 where command_override is True) or False (Code 2 where command_override is False)

# 6) b) Code the following if/else check:
# Code 1 command_override = True
# If fuel_level is above 20000 AND engine_indicator_light is NOT red blinking OR command_override is true print "Cleared to launch!" Else print "Launch scrubbed!"
if fuel_level > 20000 and engine_indicator_light != "red blinking" or command_override == True:
    print("Cleared to launch!")
else:
    print("Launch scrubbed")
# The above code when run results in the output "Cleared to launch!"

# Code 2 command_override = False
# If fuel_level is above 20000 AND engine_indicator_light is NOT red blinking OR command_override is true print "Cleared to launch!" Else print "Launch scrubbed!"
command_override = False

if fuel_level > 20000 and engine_indicator_light != "red blinking" or command_override == True:
    print("Cleared to launch!")
else:
    print("Launch scrubbed!")
# The above code when run results in the output "Launch scrubbed!"

