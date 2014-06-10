from sys import argv
script, filename = argv

def text_to_dict(filename):
    Words_as_keys = {}
    my_file = open(filename)

    for line in my_file:
        line = line.rstrip()
        word_list = line.split(' ')
        for occurance in word_list:
            #print occurance
            #for word, counter in Words_as_keys.iteritems():
            if occurance in Words_as_keys:
                Words_as_keys[occurance] += 1
                print Words_as_keys
            else:
                Words_as_keys[occurance] = 1
        return Words_as_keys

def main():
    words = text_to_dict(filename)
    #print words

if __name__ == "__main__":
    main()