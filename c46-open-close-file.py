# Open and close file

study = open("stu.txt", "r+")
for est in study:
    print(est)
print(study.readlines())
study.close()
