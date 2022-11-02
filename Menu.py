print("MENU")

print("*"*6)

print("1.Tea")

print("2.Coffee")

print("3.Chocolate")

response=input("What would you like?")

response=response.lower()

if  response == "tea":

    print("Here is your ",response)

elif response == "coffee":

    print("Here is your", response)

elif response == "hot chocolate":

    print("Here is your",response)

else:

    print("Thats all we have")
