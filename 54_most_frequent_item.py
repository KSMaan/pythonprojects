from collections import Counter

text = "Welcome to RetroPie. RetroPie allows you to turn your Raspberry Pi into a retro-gaming machine. " \
       "It builds upon Raspbian," \
       " EmulationStation, RetroArch and many other projects to enable you to play your favourite Arcade, " \
       "home-console, and classic PC games with the minimum set-up. " \
       "For power users it also provides a large variety of configuration tools to customise the system as you want." \
       "RetroPie sits on top of a full OS,"

words = text.split()
print(words)

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
