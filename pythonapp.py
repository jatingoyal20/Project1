from collections import defaultdict

a={'rr': ['4']}
for key,value in a.iteritems():
    print key
    for values in value:
        print values