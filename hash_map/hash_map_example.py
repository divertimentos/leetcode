from os import system
system('clear')

hashmap = {0: 0, 2: 3}
print(hashmap)

hashmap[1] = 1
print(hashmap)

hashmap[1] = 2
print(hashmap)

print(f"The value of key 1 is: {str(hashmap[1])}")
del hashmap[2]

print(hashmap)

if 2 not in hashmap:
    print("\nKey 2 isn't in the hashmap")

hashmap["pi"] = 3.1415
print(hashmap)

print('\nLength of the hashmap:')
print(len(hashmap))
print(str(len(hashmap)))

for key in hashmap:
    print(f"{(str(key), str(len(hashmap)))}")

print(hashmap)
print(hashmap.keys())

hashmap.clear()
print(hashmap)
print(len(hashmap))
