def wish(name):
    print('good evening ', name)

greeting=wish

hi=greeting

print(id(wish))
print(id(greeting))
print(id(hi))

wish("lokesh")
greeting("lokesh")


del wish



greeting("lokesh")

del greeting

hi("lokesh")