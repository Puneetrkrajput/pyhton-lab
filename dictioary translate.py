mydict={
    "gobi": "cauliflower",
    "ullu": "owl",
    "pankha": "fan"
}
print("option are", mydict.keys())
a=input("Enter any hindi word/n ")
#print("The given value of the word is",mydict[a]) #will throw an errorif value isnt there
print("The given value of the word is",mydict.get(a)) #will not throw an errorif value isnt there