#numbers of girls and bed
girls=int(input("no. of girls="))
bed=int(input("no. of bed="))
if bed>girls:
    print("add" ,bed-girls ,"more girls")
elif bed<girls:
    print("need",girls-bed," more bed")
else:
    print("equal")