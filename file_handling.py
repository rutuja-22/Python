
f = open('D:/PICT/Python/Myfile','a')
f1 = open('D:/PICT/Python/Myfile','r')
f2 = open('D:/PICT/Python/MCopy','a')
if(f):
    print("File opened")
    f.write("Hello!!!!")
    f.write("This is the example of file handling.")
    f.write("Thank you!!")
else:
    print("Something went wrong")

if(f1):
    f1.readline()
    print(f1)
else:
    print("Something went wrong")

if(f1 and f2):
    for data in f1:
        print(data)
        f2.write(data)
else:
    print("Something went wrong")