import json
import drink as d
import brew_methods as brew

ins = drink.Drink()
print(ins.size)

inp = input("What would you like your coffee?")
while inp != 'Done':
    inp = input('\n')
    print("Ok, I hear you said ", inp, ".")
