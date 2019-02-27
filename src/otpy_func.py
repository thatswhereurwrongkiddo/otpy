import os

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def checksys():
    import platform
    from __init__ import title
    platsys = platform.system()
    if platsys == "Windows":
        os.system("title {0}".format(title))
    else:
        pass
def vernotice():
    from __init__ import ver
    #print version notice
    print("(otpy v{0} PRE-ALPHA TEST VERSION)".format(ver))
    print("""

    """)
