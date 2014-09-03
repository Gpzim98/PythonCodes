# coding:utf8
import random

points = 11
name = ''
phrase_congrat =\
    """Parabéns %s, você obteve um excelente
     desempenho com %d pontos""" % (name, points)

phrase_bad =\
    """Volte em breve para praticar mais %s seus pontos
    foram apenas %d, isso não foi legal!
    """ % (name, points)

phrases_lvl_1 = {
    'My first name': 'Meu primeiro nome',
    'My Middle name': 'Meu nome do meio',
    'My Last name': 'Meu último nome',
    'My Address': 'Meu endereço',
    'My Phone number is': 'Meu número de telefone é',
    'What"s the ZIP Code': 'Qual é o código postal'}


def play(level=1):
    print "Are you ready?"
    print "Go!!!"
    while True:
        global points
        sorted = raffles(level)
        print "Sua frase é: " + sorted[0]
        if raw_input("Digite a tradução: ") == sorted[1]:
            points += 1
            print 'Parabens %s, sua pontuação é %d: ' % (name, points)
        else:
            print 'Você errou! A tradução correta é: ' + sorted[1]

        if raw_input('Caso queira parar pressione 0 ... ') == '0':
            print phrase_congrat if points > 10 else phrase_bad
            break


def raffles(level):
    tpl = ()
    srt = 0
    if level == 1:
        srt = random.choice(phrases_lvl_1.keys())
        tpl = srt, phrases_lvl_1[srt]
        return tpl


def store_score(name):
    #arq = open('learn_english.txt', 'a')
    pass


name = raw_input("Olá, vamos jogar! Qual o seu nome?")
store_score(name)
level = input("1: To level begginer\n2: To level intermediate")
play(level)
