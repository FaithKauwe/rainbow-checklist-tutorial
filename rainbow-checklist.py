# https://github.com/FaithKauwe/rainbow-checklist-tutorial.git

# print("Hello World")

checklist = list()
checklist.append('Blue')

checklist.append('Orange')


# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

# call the test funciton
test()