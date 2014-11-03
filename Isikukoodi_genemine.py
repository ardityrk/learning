import random
from datetime import date, timedelta

"""
print ("Valige isikukoodi genereerimise viis:")
print ("Sisestage '1' kui genereerida automaatselt")
print ("Sisestage '2' kui soovite täpsemad genereerimise parameetrid määrata")
"""


def genereeri_isikukood():
    isikukood = ""

    synni_sajand_map = {"18": ("1", "2"), "19": ("3", "4"), "20": ("5", "6"), "21": ("7", "8")}

    days_to_1800 = date.today() - date(1800, 1, 1)

    randomDay = date(1800, 1, 1) + timedelta(days=random.randint(0, days_to_1800.days))
    year_month_day = randomDay.strftime("%Y%m%d")

    synni_sajand = random.choice(synni_sajand_map[year_month_day[:2]])

    synni_aeg = randomDay.strftime("%Y%m%d")[2:]

    jarjekorra_number = str(random.randint(0, 999)).zfill(3)

    isikukood += synni_sajand + synni_aeg + jarjekorra_number

    return isikukood


if __name__ == "__main__":
    print(genereeri_isikukood())
