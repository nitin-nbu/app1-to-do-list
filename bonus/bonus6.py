## Day 6
## Suppose we have 2 list, list 1. have name of the files and list 2. have contents of the file and
# we need to put appropriate content in appropriate file.

contents = ["These are content of doc file", "These are content of report file", "These are content of presentation file"]
filenames = ["doc.txt", "reports.txt", "presentation.txt"]

for content, filename in zip(contents,filenames): #we are using zip function to get the below output
    #    print(content, filename)
    file = open(f"../files/{filename}", "w")# here we mentioned .. so the program can sear dir files 2 dir up
    file.write(content)


