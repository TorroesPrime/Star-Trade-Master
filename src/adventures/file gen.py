with open("testfile.txt",'w') as a:
    for i in range(200):
        a.write("this is a test file, line number "+str(i)+"\n")
