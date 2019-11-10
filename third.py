def thing ():
    print('Hello')
    print('Fun')
    
thing()
print('zip')
thing()

big=max('Hello world')
print(big)

tiny=min('Hello world')
print(tiny)

print(float(99) / 100)

i=42
type(i)
f =float(i)
print(f)
type(f)
print(1+2*float(3) / 4-5)

sval='123'
type(sval)
inval=int(sval)
type(inval)
print(inval+1)

x=5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x=x+2
print(x)

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
    

def greet():
    return "Hello"
    
print(greet(),"Glenn")
print(greet(), "Sally")

def addtwo(a,b):
    added = a + b
    return added
    
x=addtwo(3,5)
print(x)
