import sys
a=sys.argv[2]
f=open(sys.argv[1], "r")
dict={}
for i in f :
    person, uni = i.split(":")
    if uni.endswith("\n"):
        uni = uni[:-1]
    dict[person] = uni.split(",")
try:
    for j in a.split(","):
        print("Student:"+str(j)+" University: "+str(dict[j][0])+" Department: "+str(dict[j][1]))
except KeyError:
    print("\nNo record of '{}' was found.!".format(j))
