# for loop
for item in range(5):
    print(item)
    print(item+1)


# list
marks=[95, 98, 97]
print(marks)
print(marks[1])

print(marks[-1])


print(marks[0:2])  

print(marks[1:3])


for score in marks:
    print(score)


# append
marks.append(99)

print(marks)


# insert
marks.insert(0,99)
print(marks)

print(99 in marks)

# len
print(len(marks))