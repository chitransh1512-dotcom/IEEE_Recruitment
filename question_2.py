def count_palindrome(text):
    words = text.split()
    palindrome = []
    for word in words:
        w = word.lower().strip(',;:.!?"\'')#normalising words
        if len(w) > 1 and w == w[::-1]:  # ignore 1-letter words
            palindrome.append(w)
    if palindrome:
        print (palindrome[:])
    else:
        print('0')
para = input("enter a para of less than 100 words: ")
count_palindrome(para)