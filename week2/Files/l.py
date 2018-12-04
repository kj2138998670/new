out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file) # or outFile.write(name)
out_file.close()