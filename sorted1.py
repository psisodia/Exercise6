

def data_to_dict():
    #from sys import argv
    #filename = argv[1]
    restaurant_scores = {}
    my_file = open("score.txt")

    for line in my_file:
        line = line.rstrip()
        names, scores = line.split(':')
        restaurant_scores[names] =  scores
    return restaurant_scores

def alphabetize(restaurant_scores):
    keylist = restaurant_scores.keys()
    keylist.sort()
    for key in keylist:
        print "Restaurant %s is rated %s." % (key, restaurant_scores[key])

def main():
    #from sys import argv
    #filename = argv[1]
    dict_variable = data_to_dict()
    alphabetize(dict_variable)

if __name__ == "__main__":
    main()


