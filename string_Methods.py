# .format()
# {} are place holders

print('Insert another string wiht curly braces: {}'.format('Guido Van Rossum'))

print('First Name {0} {1} Middle Name  Lastname {2}'.format('Durga', 'Prasad', 'Ravula'))

print('This is a string with an {p}'.format(p='insert'))

print('one: {p} two: {p} three {p}'.format(p='hi'))

print('one: {a} two: {b} three: {c}'.format(a='apple', b=10, c=12.3))

s = "&"


print(s)

print(s.join(s))

#tuple data

seq = ("a", "b", "c")

print("Calling a variable i.e ",s, id(s), type(s), len(s))

print("")

joiner = '_'

title = "10 20 30 Abc"

print(title)

print(joiner.join(seq))
