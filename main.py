# coding=utf-8

import secrets
import telegram
from random import shuffle

main_categories = ["Animalier", "Rétro", "Natalizio", "Terribilino"] * 2
side_categories = ["Fluo", "Soft porno", "Peloso", "Indossabile"] * 2
exceptions = [("Animalier", "Fluo"), ("Natalizio", "Fluo")]


def main():
    shuffle(side_categories)
    while True:
        print "Generating categories pairs..."
        shuffle(main_categories)
        categories = zip(main_categories, side_categories)
        print categories
        if are_valid_categories(categories):
            break

    ids = secrets.users.keys()
    while True:
        print "Generating people pairs..."
        shuffle(ids)
        people = zip(secrets.users.keys(), ids)
        print people
        if are_valid_people(people):
            break

    draw = [(d[0][0], d[0][1], d[1][0], d[1][1]) for d in zip(categories, people)]

    bns_bot = telegram.Bot(token=secrets.bns_bot_token)
    for d in draw:
        message = "DIN-DON! Si è appena concluso il sorteggio!\nDovrai fare un regalo a " + secrets.users.get(d[3]) + \
                  ".\nLe categorie estratte per il tuo regalo sono: '" + d[0] + "' + '" + d[1] + \
                  "'.\nSi preannuncia un Natale spumeggiante!\n\nAl prossimo anno, yohoho-ooooooh!"
        bns_bot.sendMessage(chat_id=d[2], text=message)


def are_valid_categories(categories):
    return len(filter(lambda p: p in exceptions, categories)) == 0


def are_valid_people(people):
    if len(filter(lambda p: p[0] == p[1], people)) > 0:
        print "One person with himself"
        return False

    pairs = [(p[0], p[1]) for p in people] + [(p[1], p[0]) for p in people]
    if len(filter(lambda p: p in secrets.exceptions, pairs)) > 0:
        print "Forbidden people pair"
        return False

    return True


if __name__ == "__main__":
    main()
