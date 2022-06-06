# %%
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


# %%
class Portishead:
    """"Nothing"""
    def __init__(self) -> None:
        print('Portishead')


class KayneWest(Portishead):
    """"Nothing"""
    def __init__(self) -> None:
        print('Kanye West')
        super().__init__()


class ASAPRocky(Portishead):
    """"Nothing"""
    def __init__(self) -> None:
        print('ASAPRocky')
        super().__init__()


class ASAPSebbie(ASAPRocky, KayneWest):
    """"Nothing"""
    def __init__(self) -> None:
        print('ASAPSebbie')
        super().__init__()


asap_sebbie = ASAPSebbie()
# %%
