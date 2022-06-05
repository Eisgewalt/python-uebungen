def fakultaet(Zahl):
    """
    Berechnet die Fakultät einer Zahl
    """
    if Zahl > 1:
        Ergbnis = Zahl*fakultaet(Zahl-1)
    else:
        Ergbnis = 1
    return Ergbnis


faku = fakultaet(3)
print(faku)