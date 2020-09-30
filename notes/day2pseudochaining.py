# Slot
# Index Chain (linked list)
# ----- -------------------------------
#  0    -> HashEntry("qux",10) -> None
#  1    -> HashEntry("plugh",20) -> HashEntry("foo",1) -> None
#  2    -> HashEntry("xyzzy",50) -> HashEntry("baz",999) -> HashEntry("bar",30) -> None
#  3    -> None

# put("foo", 12)   # hashes to 1
# put("bar", 30)   # hashes to 2
# put("baz", 999 ) # hashes to 2--collision with "bar"!
# put("qux", 10)   # hashes to 0
# put("plugh", 20) # hashes to 1 (collision!)
# put("xyzzy", 50) # hashes to 2 (collision!)
# get("bar")       # hashes to 2

# GET(key):
#     get the index for the key
#     search the linked list at that index for the key
#     if found, return the value
#     else return None

# PUT(key):
#     get the index for the key
#     search the linked list at the index for the key
#     if the key is found, overwrite the value stored there
#     else insert the key and value at the head of the list at that index

# DELETE(key):
#     get the index for the key
#     search the linked list for the key at that index
#     if found, delete it, return it
#     else return None