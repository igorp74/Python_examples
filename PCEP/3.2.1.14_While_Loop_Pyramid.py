blocks = 2 #int(input("Enter the number of blocks: "))

height = 0
inlayer = 1
add = ''
while inlayer <= blocks:

    height += 1
    blocks -= inlayer
    inlayer += 1

    print(' H:',height, ' B:',blocks, ' L:',inlayer)

if blocks:
    add = 'in'
print(f"The height of the {add}complete pyramid: ", height)
