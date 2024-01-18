#dict comprehension
univ = 'inha'
counts_alpahbet = {letter: univ.count(letter) for letter in univ}
print(counts_alpahbet)

#basic
univ = 'inha'
counts_alpahbet = dict()
for letter in univ:
    counts_alpahbet[letter] = univ.count(letter)
print(counts_alpahbet)