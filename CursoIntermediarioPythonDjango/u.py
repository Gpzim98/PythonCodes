# -*- encoding: utf-8 -*-

u = u"Olá"
s_utf = u.encode("utf-8")
s_latin1 = u.encode("latin1")
# UnicodeError:
# u2 = s_latin1.decode("utf-8") # decodificador incorreto
u2 = s_latin1.decode("latin1")
print type(u), type(s_utf), type(s_latin1)
print repr(u), repr(s_utf), repr(s_latin1)
print repr(u), repr(u2), u == u2
