def madlib():
    disc_of_moon = input("Who did the discovery of Jupiter's moon: ")
    invention = input("He invented: ")
    art1 = input("article: ")
    which_planet = input("which planet's moon he discovered?: ")
    art2 = input("article: ")
    modern_astro = input("Father of modern astronomy: ")
    planet_laws = input("Three laws of planetary motion was given by: ")
    art3 = input("article: ")
    geo_theory = input("Who gave controversial geocentric theory of the universe: ")
    prep1 = input("preposition: ")
    art4 = input("article: ")
    art5 = input("article: ")
    prep2 = input("preposition: ")
    swing_clock = input("swinging weight in clock: ")


    madlib = f"{disc_of_moon} used mathematical calculation as well as observation of nature and was the first\
astronomer to use a {invention}. With {art1} instrument of his own construction Galileo observed {which_planet} and 4\
of its moons, the phases of Venus and {art2} spots on the sun. His observations and calculations \
confirmed that {modern_astro} and {planet_laws} were right. He saw with his own eyes and made other people \
see too that {art3} earth was not the fixed center of the universe as {geo_theory} had said. \
Galileo also made some important discoveries {prep1} mechanics. He did not as legend says drop cannon \
balls from the Leaning Tower of Pisa to prove that all bodies fall at the same speed, but \
he did roll balls down a slope to show that {art4} distance a body falls is proportionate \
to the square of the time it takes to fall. Galileo also noticed {art5} regular swinging {prep2} \
the lamps in Pisa cathedral; this gave him the idea of the {swing_clock}, a device that enabled him \
to make the clock a scientific instrument for the first time."
    
    print(madlib)
