"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open("green-eggs.txt").read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    contents = open_and_read_file("green-eggs.txt")
    
    words = contents.split()
    value = []



    for i in range(0,len(words)- 2):

        key = (words[i], words[i + 1])
        #print(key, '****')
        if key in chains:
            chains[key].append(words[i+2])
        else:
            chains[key] = [words[i + 2]]


    # your code goes here

    for i in range(0,len(words)- 2):
        
        key2 = (key[1], words[i+2])

        if key2 in chains:
            chains[key2].append(words[i+2])
        else:
            chains[key2] = [words[i+2]]
        # chains = chains.get(chains[key2]) 
    # for new_word in key2:
    #     if new_word in chains:
    #         new_words.append([chains[key]])
        #else:
            #chains[key2] = [new_words[chains[key]]]


    # for keys in key:
    #     chains[key].append([words[i+2]])
   
        # if value not in key:
        #     chains[key] = [words[i + 2]]
        # else:
        #     value.append(words[i+2])
            #chains[key] = chains[key].get([words[i+2]])
        
        # print ((words[i], words[i + 1]) , words[i+2])
    #print(chains)
    # your code goes here
    



    

    return chains
    


def make_text(chains):
    """Return text from chains."""
    additional_words = random.choice(words)
    rndm_output = [additional_words]

    for i in range(30):
        chains.append(random.choice(chains[rndm_output[-1]]))

 
       
    
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
