#!/usr/bin/python

# Initialize the amounts
emperors = int(raw_input('Emperor butterflies: '))
goldens = int(raw_input('Golden stags: '))
elephants = int(raw_input('Elephant beetles: '))
cyclos = int(raw_input('Cyclommatus stags: '))
goliaths = int(raw_input('Goliath beetles: '))
atlases = int(raw_input('Atlas beetles: '))

# Compute total
total = 0
total += emperors * 2500
total += goldens * 12000
total += elephants * 8000
total += cyclos * 8000
total += goliaths * 6000
total += atlases * 8000

# Assume bell bloom ordinance
total *= 1.2

# Print results
print('Total: ' + str(total) + '!')
