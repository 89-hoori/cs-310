count = 0
dictionary_words = dict()                   # Initializes the dictionary
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue                        # Discards duplicates
        dictionary_words[word] = count      # Value is first time word appears

if 'Python' in dictionary_words:
    print('True')
else:
    print('False')


dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts

print(dictionary_days)


dictionary_addresses = dict()                   # Initializes the dictionary
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1  # First entry
        else:
            dictionary_addresses[words[1]] += 1     # Additional counts

print(dictionary_addresses)


dictionary_addresses = dict()                   # Initialize variables
maximum = 0
maximum_address = ''

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dictionary_addresses:
        dictionary_addresses[words[1]] = 1      # First entry
    else:
        dictionary_addresses[words[1]] += 1     # Additional counts

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:     # Checks if new maximum
        # Update the maximum if needed
        maximum = dictionary_addresses[address]
        # Stors the address of maximum
        maximum_address = address

print(maximum_address, maximum)


dictionary_domains = dict()                       # Initialize variables

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')               # Position of '@'
        domain = words[1][atpos+1:]              # Store characters after '@'
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1       # First entry
        else:
            dictionary_domains[domain] += 1      # Additional counts

print(dictionary_domains)

