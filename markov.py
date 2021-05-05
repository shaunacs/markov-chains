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

    # for i in range(0,len(words)- 2):
        
    #     key2 = (key[1], choice(chains[key]))

    #     if key2 in chains:
    #         chains[key2].append(choice(chains[key]))
    #     else:
    #         chains[key2] = []
        # chains = chains.get(chains[key2]) 
   



    #print(chains)
    # your code goes here
    



    

    return chains
    


def make_text(chains):
    """Return text from chains."""
    random_output =[]

  


    #choose random tuple, pick random word from key value
    for key in chains:
        pull_from_list = choice(chains[key])
        pull_from_tuple = choice(list(key))
        if chains[key] == []:
            break
        else:
            random_output.append(pull_from_tuple)
            random_output.append(pull_from_list)
           
           
            # picking= random_output.choice(chains[key])
            # random_output.append(picking)

 
    print(random_output)   
    
    return ' '.join(random_output)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
