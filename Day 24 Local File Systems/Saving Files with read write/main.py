
#store away and open the example textfile
file = open("my_file.txt")

#store the read contents of a file
contents = file.read()

print(contents)

#close the file to reduce the number of resources used up while program is running, IE performance saving methods
file.close()

#secondary method
#with method of opening a file will self manage the opened file to close after usage
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#writing to the file
#file operational modes: "a" appends to file, "r" read-only, "w" write to file
with open("my_file.txt", mode="w") as file:
    file.write("New Text. Written to the file.")

with open("my_file.txt", mode= "a") as file:
    file.write("\nappended text to file")

#create a new file
with open("new_file.txt", mode="w") as file:
    file.write("new file")

#Find file outside relative working directory
with open("/Users/Terry/Desktop/NestedFile.txt") as file:
    print(file.read())