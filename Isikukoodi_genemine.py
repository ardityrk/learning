import random
from datetime import date, timedelta

def genereeri_isikukood():
    print("If thou brave, do proceed...for others http://no.nonsense.ee/isikukood.php ...")

    isikukood = ""
    esimene_kaalud = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    teine_kaalud = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

    synni_sajand_map = {"18": ("1", "2"), "19": ("3", "4"), "20": ("5", "6"), "21": ("7", "8")}

    days_to_1800 = date.today() - date(1800, 1, 1)

    random_day = date(1800, 1, 1) + timedelta(days=random.randint(0, days_to_1800.days))
    year_month_day = random_day.strftime("%Y%m%d")

    synni_sajand = random.choice(synni_sajand_map[year_month_day[:2]])

    synni_aeg = random_day.strftime("%Y%m%d")[2:]

    jarjekorra_number = str(random.randint(0, 999)).zfill(3)

    isikukood += synni_sajand + synni_aeg + jarjekorra_number

    kontroll_number = 0
    esimese_kaalu_summa = 0
    for arg in range(len(esimene_kaalud)):
        esimese_kaalu_summa = esimese_kaalu_summa + (esimene_kaalud[arg] * int(isikukood[arg]))
    if esimese_kaalu_summa % 11 != 10:
        kontroll_number = esimese_kaalu_summa % 11
        isikukood += str(kontroll_number)
    else:
        teise_kaalu_summa = 0
        for arg in range(len(teine_kaalud)):
            teise_kaalu_summa = teise_kaalu_summa + (teine_kaalud[arg] * int(isikukood[arg]))
        if teise_kaalu_summa % 11 != 10:
            kontroll_number = teise_kaalu_summa % 11
            isikukood += kontroll_number
        else:
            kontroll_number = 0
    return isikukood

if __name__ == "__main__":
    print(genereeri_isikukood())