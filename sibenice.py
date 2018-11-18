from random import choice
from obesenec import seznam_stavu

def zeptej_se_uzivatele(slovo, skryte_slovo, seznam_pouzitych_pismen):
    """Funkce, ktera vyzve uzivatele k zadani jednoho pismene."""
    while True:
        pismeno_od_uzivatele = input("Zadej pismeno: ").lower()
        if len(pismeno_od_uzivatele) > 1: #uzivatel musi zadat pouze jedno pismeno
            print("Zadej pouze jedno pismeno!")
        elif not pismeno_od_uzivatele.isalpha(): #uzivatel musi zadat pouze pismeno z abecedy, ne cisla nebo znaky
            print("Zadej pouze pismeno z abecedy!")
        else:
            return zapis_pismeno(pismeno_od_uzivatele,slovo, skryte_slovo, seznam_pouzitych_pismen) #zapise pismeno do skryteho slova

def nahodne_slovo(seznam):
    """Funkce, ktera vybere nahodne slovo ze seznamu slov. Vrati pole slozene z _ , ktere ma delku slova a samotne slovo."""
    nahodne_slovo = choice(seznam) #vybere nahodne slovo ze seznamu
    delka_slova = len(nahodne_slovo) #spocita delku nahodneho slova
    skryte_slovo = "_" * delka_slova #ulozi skryte slovo jako retezec z _ stejne delky jako je nahodne vybrane slovo
    return nahodne_slovo, skryte_slovo

def stav_hadani_slova(seznam, pocet_pismen): #vrati obesence, vzhledem k poctu neuhadnutych pismen
    pocet_polozek_v_seznamu = len(seznam)
    if pocet_pismen <= pocet_polozek_v_seznamu - 1:
        return seznam[pocet_pismen]
    else:
        return False

def vyhodnot(slovo):
    """Funkce, ktera vyhodnoti stav hry. Pokud neni ve skrytem slove podtrzitko, hrac vyhral."""
    if "_" in slovo:
        return True #hra stale bezi
    else:
        return False #hrac vyhral


def zapis_pismeno(pismeno, slovo, skryte_slovo, seznam_pouzitych_pismen):
    """Funkce, ktera najde pismeno zadane uzivatelem ve slove a vloziho do skryteho slova. Naopak vytvori slovo zrdcadlove k uzivatelovu
    hadanemu slovu a do nej vlozi podtrziko, na stejne pismeno jako u skryteho."""
    zrcadlove_upravene_skryte_slovo = slovo #zrcadlove upravene slovo ke slovu z pismen, ktere zatim uhadl uzivatel
    pocet = 0 #pocet neuhadnutyh pismen
    seznam_skrytych_slov = [] #seznam skrytych slov - retezec podtrzitek do ktereho se vkladaji pismena uzivatelem
    zrcadlove_upravene_skryte_slovo_seznam = [] #seznam zrdcadlove upravenych slov

    while True:
        pocet_pismen = zrcadlove_upravene_skryte_slovo.count(pismeno)
        if pocet_pismen == 1: #pokud hadane slovo obsahuje jedno hadane pismeno
            index_pismena = zrcadlove_upravene_skryte_slovo.index(pismeno) #zjisti index pismene v hadanem slove
            zrcadlove_upravene_skryte_slovo = zrcadlove_upravene_skryte_slovo[:index_pismena] + "_" + zrcadlove_upravene_skryte_slovo[(index_pismena+1):] #na index zjisteny v kroce vyse, zapise podtrzitko
            seznam_pouzitych_pismen.append(pismeno) #prida pismeno do seznamu pouzitych pismen
            return pocet, seznam_pouzitych_pismen, zrcadlove_upravene_skryte_slovo, skryte_slovo[:index_pismena] + pismeno + skryte_slovo[index_pismena + 1:]
        elif pocet_pismen == 0: #pokud hadane slovo neobsahuje hadane pismeno
            if pismeno not in seznam_pouzitych_pismen:
                seznam_pouzitych_pismen.append(pismeno) #prida pismeno do seznamu pouzitych pismen
                pocet = pocet + 1 #pocet neuhadnutyh pismen se zvysi o jedno - obesenec bude blize k obeseni
                return pocet, seznam_pouzitych_pismen, zrcadlove_upravene_skryte_slovo, skryte_slovo
            else: #pokud nebude obsahovat pismeno a bude uz v seznamu pouzitych pismen, nezvysi se pocet neuhadnutych o jedna - nemam vliv na obeseni
                return pocet, seznam_pouzitych_pismen, zrcadlove_upravene_skryte_slovo, skryte_slovo
        else:
            #pokud hadane slovo obsahuje vice stejnych pismen
            if pismeno not in seznam_pouzitych_pismen: #pokud nebude pismeno v seznamu pouzitych pismen
                seznam_pouzitych_pismen.append(pismeno) #prida pismeno do seznamu pouzitych pismen

            for i in zrcadlove_upravene_skryte_slovo:
                index_pismena = zrcadlove_upravene_skryte_slovo.index(pismeno) #zjisti index pismene v hadanem slove
                zrcadlove_upravene_skryte_slovo = zrcadlove_upravene_skryte_slovo[:index_pismena] + "_" + zrcadlove_upravene_skryte_slovo[(index_pismena+1):] #na index zjisteny v kroce vyse, zapise podtrzitko
                skryte_slovo = skryte_slovo[:index_pismena] + pismeno + skryte_slovo[index_pismena + 1:]
                seznam_skrytych_slov.append(skryte_slovo) #prida slovo do seznamu skrytych slov
                zrcadlove_upravene_skryte_slovo_seznam.append(zrcadlove_upravene_skryte_slovo) #prida zrdcadlove upravene slovo do seznamu
                posledni_slovo = zrcadlove_upravene_skryte_slovo_seznam[-1] #posledni slovo v seznamu
                posledni_vice_pismen = seznam_skrytych_slov[-1] #posledni slovo v seznamu

                if pismeno not in posledni_slovo: #pokud neni hadane pismeno v poslednim zrcadlove upravenem slovem, prida vsechny stejna pismena do slova naraz
                    return pocet, seznam_pouzitych_pismen, posledni_slovo, posledni_vice_pismen



def opakuj_hru(seznam):
    """Funkce, ktera se zepta hrace, zda chce hrat znovu"""
    while True:
        opakuj_uzivatel_odpoved = input("Chces opakovat hru? ano/ne: ")
        if not opakuj_uzivatel_odpoved in ("ano","ne"):   #podminka pro zadani x,o
            print("Zadej pouze ano/ne.")
            continue
        else:
            if opakuj_uzivatel_odpoved == "ano":
                return "ano"
            elif opakuj_uzivatel_odpoved =="ne":
                return "ne"

def sibenice(seznam):
    """Funkce, ktera vygeneruje nahodne slovo a zobrazi jej uzivateli jako retezec podtrzitek
     a nasledne se pta uzivatele na pismeno, ktere by mohlo byt ve slove. Kazde pismeno se zapise do seznamu hadanych pismen.
     Kazde pismeno muze byt hadano pouze jednou. Opakovane zadani neni pocitano za chybu. Pokud uzivatel hada spatne, zobrazi
     hra novy obrazek obesence. Pokud je obesenec obeseny, potom je konec hry. Pokud uzivatel uhadne slovo vyhral. Po ukonceni
     hry se hra zepta, zda chce uzivatel hrat znovu. """

    pocet_neuhadnutych_pismen = 0 #pocet pismen, ktere hrac hada a nejsou ve slove
    slovo, retezec_se_skrytym_slovem = nahodne_slovo(seznam) #vrati nahodne vygenerovane slovo a retezec stejne delky s podtrziky - skryva nahodne slovo
    upravene_hadane_slovo = slovo #defaultne nastaveno na hadane slovo, ale s hadanim uzivatele obsahuje opak toho co se uzivateli odkryva
    seznam_pismen = [] #seznam pouzitych pismen, ktera uzivatel zadal
    pocet_pismen = 0 #pocet neuhadnutych pismen je na zacatku nula

    while "_" in retezec_se_skrytym_slovem:

        pocet_neuhadnutych_pismen = pocet_neuhadnutych_pismen + pocet_pismen
        zobraz_obesence = stav_hadani_slova(seznam_stavu, pocet_neuhadnutych_pismen)

        if zobraz_obesence == False:
            print("Prohrál jsi.")
            print("Hadane slovo bylo: ", slovo)

            chces_opakovat_hru = opakuj_hru(seznam) #zepta se uzivatele, zda chce opakovat hru
            if chces_opakovat_hru =="ano":
                sibenice(seznam)
            else:
                print("Konec hry.")
                exit()

        print(zobraz_obesence) #vytiskne obrazek obesence dle poctu neuhadnutych pismen
        print(retezec_se_skrytym_slovem) #zobrazi slovo skryte s podtrziky, pokud uzivatel uhadne - nahradni pismeno podtrzitko
        pocet_pismen, seznam_pismen, upravene_hadane_slovo, retezec_se_skrytym_slovem = zeptej_se_uzivatele(upravene_hadane_slovo, retezec_se_skrytym_slovem, seznam_pismen)
        print("Seznam pouzitych pismen: ", seznam_pismen)

        vysledek = vyhodnot(retezec_se_skrytym_slovem)
        if vysledek == False: #pokud neni ve slove podtrziko hra se ukonci, vyhral hrac
            print("Hadane slovo bylo: ", slovo)
            print("Konec hry! Vyhrál jsi.")

            chces_opakovat_hru = opakuj_hru(seznam) #zepta se uzivatele, zda chce opakovat hru
            if chces_opakovat_hru =="ano":
                sibenice(seznam)
            else:
                print("Konec hry.")
                exit()
