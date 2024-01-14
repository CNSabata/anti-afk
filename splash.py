from pyfiglet import Figlet

f = Figlet(font='slant')


def print_splash_screen_intro():
    print(f.renderText('ANTI-AFK'))
    print(f"{'Original By Walkoud, Edited by CNSabata': >40}")
    print("\n\n")
    print('Type "m" to activate or deactivate the anti-afk')
    print('Type "!" to exit')
