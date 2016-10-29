
def main():

	groceryList = []

	input1 = "zero"

	while input1 != "done":
		input1 = input("Add item to list ('done' when finished): ")
		
		if input1 != "done":
			groceryList.append(input1)

	print("Final shopping list: ", groceryList)


	total = 0
	counter = 0
	newList = groceryList

	#I don't need the counter to increase (counter += 1) because everytime I REMOVE an item from the list
	#the entire list shifts one to the left - I can keep working with the first ( [0] ) position of list
	while len(groceryList) > 0:

		price = float(input("How much did "+ str(groceryList[counter])+" cost? " ))
		
		total += price

		groceryList.remove(groceryList[counter])


			

	print("Your shopping trip cost $%f" % (total))
	print("Shopping list at the end of trip:", newList)



main()
