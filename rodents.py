class Rodent:
    def __init__(self,tag_id):
        self.tag_id = tag_id
        self.weights = []

    def plot(self):
        return self.tag_id[0]

    def add_weight(self,weight):
        return self.weights.append(weight)
   
    def max_weight(self):
        return max(self.weights)

    def min_weight(self):
        return min(self.weights)

    def numb_weights(self):
        return len(self.weights)

    def summary(self):
        n = self.numb_weights()
        mx = self.max_weight()
        mi = self.min_weight()
        mean = reduce(lambda x,y: x+y,self.weights)/float(n)
        var = reduce(lambda x,y: x+(y-mean)**2,self.weights) / float(n)
        return (n,mx,mi,mean,var)

import sys

filename = sys.argv[1]

f = open(filename,'r')

rodent_dic = {}

for line in f:
    line = (line.strip()).split(",")
    if len(line) != 2:
        break
    t = line[0]
    w =float(line[1])
    if t in rodent_dic:
        rodent_dic[t].add_weight(w)
    else:
        rodent_dic[t] = Rodent(t)
        rodent_dic[t].add_weight(w)

print "Added a total of {} rodents.".format(len(set(rodent_dic)))

max_weight = 0
max_rod = rodent_dic.keys()[0]

for r in rodent_dic:
    if rodent_dic[r].max_weight() > max_weight:
        max_weight = rodent_dic[r].max_weight()
        max_rod = r
        
print "The largest mouse is {} and it weights {}g.".format(max_rod,max_weight)

max_sights = 0
max_rod = rodent_dic.keys()[0]

for r in rodent_dic:
    if rodent_dic[r].numb_weights() > max_sights:
        max_sights = rodent_dic[r].numb_weights()
        max_rod = r

print "The mouse {} has the most sightings with {} sightings.".format(max_rod,max_sights)

print "rodent min max mean var"
for r in rodent_dic:
    n,mx,mi,mean,var = rodent_dic[r].summary()
    print r,n,mi,mx,mean,var
