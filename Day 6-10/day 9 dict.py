bug={"key":"value"}
print(bug["key"])
bug[123]="no need for comma in number"
print(bug)#you can add more elements like this, no need to write at once

#you can create a empty dictionary using empty={}

#also you can wipe an existing dictionary using bug={}

#you can edit a dictionary value using bug[123]="hello"



#looping thorugh a dict
for key in bug:
    print(key)
    print(bug[key])
