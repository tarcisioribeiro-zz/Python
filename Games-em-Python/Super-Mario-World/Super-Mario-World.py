from pygame import mixer
mixer.init()

mixer.music.load("supermarioworld.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()
while True:
    print()
    print("\033[0;33mAperte 'p' para parar\033[m")
    print("\033[0;33mAperte 'r' para resumir\033[m")
    print("\033[0;33mAperte 'v' para ajustar o volume\033[m")
    print("\033[0;33mAperte 'e' para sair\033[m")
    print()
    ch = input("\033[0;33mO que deseja fazer? ['p','r','v','e']>>> \033[m")
    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("\033[0;33mDigite o volume(0 até 1): \033[m"))
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break
