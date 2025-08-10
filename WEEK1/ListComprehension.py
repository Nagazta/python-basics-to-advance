print("Lists!")
names = ["Kyle", "Jhon", "Ryle"]
newlist = []
again = True

while(again): 
    search = input("Enter a letter or word: ")

    #Searching a certain letters or words based on the variable "Search"
    for x in names:
        if search in x:
            newlist.append(x)
    
    #Checking if the search is found or not
    if newlist:
        print(newlist)
    else: 
        print("Not found")

    #Trying again in a loop
    again = input("Do you want to search again? Press Y if yes and N if No: ")
    if again == "Y": 
        newlist.clear()
        again =True
    else:
        again =False