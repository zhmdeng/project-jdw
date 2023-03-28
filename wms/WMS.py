a = {'group1':'lk01','group2':'lk20','group3':'lk11','group4':'lk21','group5':'lk22'}
f = {value:key for key,value in dict(sorted(a.items(),key = lambda x:x[1])).items()}
print(f)
# print(dict(sorted(c)).items())