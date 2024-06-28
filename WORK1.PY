name=[]
while True:
    print("1.Add \n2.Display \n3.Update \n4.Delete \n5.Exit \n")

    a=int(input("Enter a choice :"))
    if a==1:
        b=int(input("Enter how many students :"))
        for i in range(b):
            n=input("Enter Students Name :")
            name.append(n)
    elif a==2:
        for i in name:
            print(i)
    elif a==3:
        a_name=(input("Enter the name :"))
        if a_name in name:
            new_name=input("Enter a new name")
            pos=new_name.index(new_name)
            name[pos]=new_name
        else:
            print("is not in the list ")
    elif a==4:
        b_name=input("Enter which name to delete :")
        if b_name in name:
            name.remove(b_name)
            for i in name:
                print("Remaining students are :", i)
        else:
            print("is not in the list")
    elif a==5:
        break
    else:
        print("incorect choice")