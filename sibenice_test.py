from sibenice import nahodne_slovo, stav_hadani_slova, vyhodnot, zapis_pismeno, opakuj_hru
import pytest


def test_nahodne_slovo_generuj_spravna_delka():
    assert nahodne_slovo(["ahoj"]) == ("ahoj", "____")

def test_stav_hadani_slova_vyber_obesence():
    assert stav_hadani_slova(["prvni_obesenec", "druhy_obesenec"], 0) == "prvni_obesenec"

def test_stav_hadani_slova_konec_hry():
    assert stav_hadani_slova(["prvni_obesenec", "druhy_obesenec"], 3) == False

def test_vyhodnot_cele_slovo():
    assert vyhodnot("pes") == False

def test_vyhodnot_castecne_odkryte_slovo():
    assert vyhodnot("p_s") == True

def test_zapis_jedno_pismeno():
    assert zapis_pismeno("a", "kočka","_____" ,[]) == (0, ["a"],"kočk_", "____a")

def test_zapis_dalsi_spravne_pismeno():
    assert zapis_pismeno("a", "_oč_a","k__k_" ,["k"]) == (0, ["k","a"],"_oč__", "k__ka")

def test_zapis_vice_pismen():
    assert zapis_pismeno("a","ananas","______",[]) == (0,["a"],"_n_n_s","a_a_a_")

def test_zapis_stejne_pismeno_znovu():
    assert zapis_pismeno("a","ananas","a_a_a_",["a"]) == (0,["a"],"_n_n_s","a_a_a_")

def test_zapis_stejne_pismeno_jako_dalsi():
    assert zapis_pismeno("p", "p__", "_es", ["e","s"]) == (0, ["e", "s", "p"],"___", "pes")

def test_pismeno_se_nevysktytuje_ve_slove():
    assert zapis_pismeno("a","pes","___",[]) == (1,["a"],"pes","___")
