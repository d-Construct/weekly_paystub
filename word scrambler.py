
secret_word = input('What word do you want to discombobulate?')
sliced_word = secret_word[::2]+secret_word[1::2]
print(sliced_word)