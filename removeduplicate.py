def remove(duplicate):
    array=[]
    for element in duplicate:
        if element not in array:
            array.append(element)
    return array
duplicate=[2,3,4,20,2,15,3,20]
print (remove (duplicate))

