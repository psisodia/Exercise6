from sys import argv
script, filename = argv

def data_to_dict(filename):
    restaurant_scores = {}
    my_file = open(filename)

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

    dict_variable = data_to_dict(filename)
    alphabetize(dict_variable)

if __name__ == "__main__":
    main()


