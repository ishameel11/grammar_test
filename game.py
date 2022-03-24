def madlib():
    whnouns = input("wh-word: ")
    verb1 = input("verb: ")
    art1 = input("article: ")
    pronoun1 = input("pronoun: ")
    verb2 = input("preposition: ")
    art2 = input("article: ")
    prep2 = input("preposition: ")
    verb3 = input("verb: ")


    madlib=f" '{whnouns} {verb1} happen to them after us?' This most distressing question continually \
torments {art1} parents of {pronoun1} unfortunate children. So they {verb2} mainly interested in providing \
some kind {prep1} vocational training for them. Hence special schools for such children, spread all \
over {art2} world, lay emphasis {prep2} vocational training. According they {verb3} taught to make paper bags,\
simple wall hangings etc. This, of course, is quite agreeable and admirable. But what about play \
and sport?"

    print(madlib)

if __name__ == '__main__':
    madlib()
