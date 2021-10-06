class node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def setroot(givendata):
	global root
	if root == None:
		newnode = node(givendata)
		root = newnode
		print("Inserted ", givendata, " at ", "root\n")
		return
	else:
		print("Can't insert ",givendata,"at root")
		print("Because root of the binarytree has already been assigned to ",root.data,"\n")
		return

def searchdata(checknode,givendata):
	global root
	if checknode.data == givendata:
		return checknode
	if checknode.left is not None:
		temp1 = searchdata(checknode.left,givendata)
		if temp1 is not None:
			return temp1
	if checknode.right is not None:
		temp2 = searchdata(checknode.right,givendata)
		if temp2 is not None:
			return temp2
	return None


def inorder_traversal(givendata):
	if givendata != None:
		inorder_traversal(givendata.left)
		print(givendata.data,end = " ")
		inorder_traversal(givendata.right)
			

def postorder_traversal(givendata):
	if givendata != None:
		postorder_traversal(givendata.left)
		postorder_traversal(givendata.right)
		print(givendata.data,end = " ")


def preorder_traversal(givendata):
	if givendata != None:	
		print(givendata.data,end = " ")
		preorder_traversal(givendata.left)
		preorder_traversal(givendata.right)


def insertleft(givendata,refdata):
	global root
	newnode = node(givendata)
	refnode = searchdata(root,refdata)
	if refnode == None:
		print("Can't find ",refdata," in binarytree\n")
		return

	if refnode.left == None:
		refnode.left = newnode
		print("Inserted ",givendata," left of ",refdata,"\n")
		return
	else:
		print("Can't insert ",givendata," left of ",refdata)
		print("Because left child of ",refdata," has already been assigned to ",refnode.left.data,"\n")


def insertright(givendata,refdata):
	global root
	newnode = node(givendata)
	refnode = searchdata(root,refdata)
	if refnode == None:
		print("Can't find ",refdata," in binarytree\n")
		return

	if refnode.right == None:
		refnode.right = newnode
		print("Inserted ",givendata," right of ",refdata,"\n")
		return
	else:
		print("Can't insert ",givendata," right of ",refdata)
		print("Because right child of ",refdata," has already been assigned to ",refnode.right.data,"\n")
		return


root = None
print("Please follow below syntax to give input")
print("Eg: Insert 20 at root")
print("Eg: Insert 30 left of 40")

while True:
	print("OPTIONS:")
	print("1. Insert <data> at root")
	print("2. Insert <data> left of <data>")
	print("3. Insert <data> right of <data>")
	print("4. Search <data>")
	print("5. Print Inorder traversal")
	print("6. Print Preorder traversal")
	print("7. Print Postorder traversal")
	print("8. Quit")
	print("\n")
	print("What would you like to do?\nGive Input:",end = " ")
	activity = input()
	activity = activity.split()
	print("\n")

	if activity[0].lower() == "insert":
		givendata = int(activity[1])

		if activity[2].lower() == "at":
			setroot(givendata)

		elif activity[2].lower() == "left":
			refdata = int(activity[4])
			insertleft(givendata,refdata)

		elif activity[2].lower() == "right":
			refdata = int(activity[4])
			insertright(givendata,refdata)


	elif activity[0].lower() == "search":
		givendata = int(activity[1])

		if searchdata(root,givendata) != None:
			print("Found ",givendata," in binarytree\n")

		else:
			print("Can't find ",givendata," in binarytree\n")


	elif activity[0].lower() == "print":
		if activity[1].lower() == "inorder":
			inorder_traversal(root)
			print("\n")
			print("\n")

		elif activity[1].lower() == "preorder":
			preorder_traversal(root)
			print("\n")
			print("\n")

		elif activity[1].lower() == "postorder":
			postorder_traversal(root)
			print("\n")
			print("\n")


	elif activity[0].lower() ==  "quit":
		print("\n")
		break


	else:
		print("Give proper input!\n")



