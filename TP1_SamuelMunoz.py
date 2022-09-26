#Cree par Samuel Munoz
#Cree en septembre 2022
#But:compter les nombres des mots dans un pharase syntaxique ou pas syntaxique

phrase = input("ecrivez une phrase quelconque")
def word_count(phrase):
    
    nbr_des_mots = str(len(phrase.split(" "))) #on se pare les mots en diffrents sous chianes et on nomme les nbr des chaines
    return nbr_des_mots

print("il y a",word_count(),"mots") #on print le resultat
