def main():
    # set n and k values
    n, k = map(int, input().split())
    
    # initialize the number of anagrams to 0
    non_anagram_count = 0
    
    # create a dictionary to store the sorted words
    sorted_words = {}

    for i in range(n):
        # read the input word
        word = input()
        
        # sort the letters based on ASCII and create a new string with the characters
        sorted_word = ''.join(sorted(word))
        
        # if the word exists in the dictionary, increase the count of the value
        if sorted_word in sorted_words:
            sorted_words[sorted_word] += 1
        else:
            # else create a new key-value pair
            sorted_words[sorted_word] = 1

    # loop through the values and increment the non_anagram_count if there is only 1 match
    for num in sorted_words.values():
        if num == 1:
            non_anagram_count += 1

    # print to console
    print(non_anagram_count)

if __name__ == "__main__":
    main()
