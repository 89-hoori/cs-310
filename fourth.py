x=5
if x < 10:
    print('smaller')
if x > 20:
    print('Bigger')
    
print('Finis')

x=5
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6 : print('less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')

x=5
print('before 5')
if  x == 5 :
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')

x=42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

x=4
if x > 2 :
    print('Bigger')
else:
    print('Smaller')
    
print('All done')

if x < 2 :
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')

if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')
    
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr=-1
    
print('First',istr)

astr='123'
try:
    istr = int(astr)
except:
    istr = -1
    
print('Second',istr)

astr = 'Bob'
try:
   print('Hello')
   istr= int(astr)
   print('There')
except:
    istr=-1
    
print('Done',istr)

rawstr = input('Enter a number')
try:
    inval= int (rawstr)
except:
    inval=-1
    
if inval > 0 :
    print('Nice work')
else:
    print('Not a number')
    
    
