# -*- coding: utf-8 -*-

# Notre décorateur
def decorate(func):
    print (u"Je suis dans la fonction 'decorate' et je décore '%s'." % func.__name__)
    print (u"Exécution de la fonction '%s'." % func.__name__)
    return func

# Notre fonction décorée
@decorate
def foobar(*args):
    print (", ".join(args))

# Appel de la fonction
foobar("A", "B", "C", "D")
foobar("A", "B", "C", "D")
