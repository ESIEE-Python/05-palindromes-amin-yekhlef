#### Fonction secondaire


def ispalindrome(p):

    #p = str.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")

    if p == "" or len(p) == 1:
        return True

    if p[0] != p[-1]:
        return False
    
    return ispalindrome(p[1:-1])

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()