def madlib():
    verb1 = input('verb: ')
    prep1 = input('preposition: ')
    art1 = input('article: ')
    prep2 = input('preposition: ')
    prep3 = input('preposition: ')
    art2 = input('article: ')
    distance_mes = input('What will be the distance: ')
    madlib=f"Without water no animal {verb1} survive. {prep1} desert regions {art1} greatest threat to life is \
drying up. But many creatures are able {prep2} make use of the little water that exists {prep3} arid areas. \
One of nature’s masterpieces among creatures equipped to cope with desert life is the hardy camel. \
Stories range {art2} desert lands far and wide about remarkable endurance feats by camels. It is said \
that camels can cover a distance of about 800 {distance_mes} in eight days through continuous travel without \
an intake of a single drop of water.The popular belief the camels store water in the humps is correct. \
in a way; water is indeed stored there but in the form of fat."
    print(madlib)

if __name__ == '__main__':
    madlib()
