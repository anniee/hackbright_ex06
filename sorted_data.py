rest_ratings_file = open("scores.txt")

all_ratings = {}

for each_line in rest_ratings_file:

    current_line = each_line.rstrip()
    line = current_line.split(":")

    rest_name = line[0]
    rest_rating = line[1] 
    # print rest_name
    # print rest_rating 
    all_ratings[rest_name] = rest_rating

print "all_ratings is a " + str(type(all_ratings))

sorted_ratings = {}

sorted_ratings = sorted(all_ratings.items())
print sorted_ratings
print "sorted_ratings is a " + str(type(sorted_ratings))

for each in sorted_ratings:
    print "Restaurant %r is rated at %r" % each
