my_list=[1,2,3,"stop",5,"stop",4.1]
for i in my_list:
    print(i)
    for i in my_list:
        print(i)
        if i =="stop":
           print("THE CODE WILL STOP !")
           break
print("This is outside of the loop")
