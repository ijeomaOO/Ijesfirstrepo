# Create dictionary for each sign
zodiacCon = {"Aries":"Ram",
    "Taurus": "Bull",
    "Gemini": "Twins",
    "Cancer": "Crab",
    "Leo" : "Lion",
    "Virgo": "Virgin",
    "Libra": "Scale",
    "Scoprio" : "Scorpion",
    "Sagittarius" : "Archer",
    "Capricorn" : "Goat",
    "Aquarius" : "Waterbearer",
    "Pisces" : "Fish"}

sign = input("What is your Zodiac Sign? ")

def findSign(sign, zodiacCon):
    if sign == "Aries" or sign == "aries":
        return("Your sign is " + zodiacCon["Aries"])
    elif sign == "Taurus" or sign == "taurus":
        return("Your sign is " + zodiacCon["Taurus"])
    elif sign == "Gemini" or sign == "gemini":
        return("Your sign is " + zodiacCon["Gemini"])
    elif sign == "Cancer" or sign == "cancer":
        return("Your sign is " + zodiacCon["Cancer"])
    elif sign == "Leo" or sign == "leo":
        return("Your sign is " + zodiacCon["Leo"])
    elif sign == "Virgo" or sign == "virgo":
        return("Your sign is " + zodiacCon["Virgo"])
    elif sign == "Scorpio" or sign == "scorpio":
        return("Your sign is " + zodiacCon["Scorpio"])
    elif sign == "Sagittarius" or sign == "sagittarius":
        return("Your sign is " + zodiacCon["Sagittarius"])
    elif sign == "Capricorn" or sign == "capricorn":
        return("Your sign is " + zodiacCon["Capricorn"])
    elif sign == "Aquarius" or sign == "aquarius":
        return("Your sign is " + zodiacCon["Aquarius"])
    elif sign == "Pisces" or sign == "pisces":
        return("Your sign is " + zodiacCon["Pisces"])

print(findSign(sign, zodiacCon))