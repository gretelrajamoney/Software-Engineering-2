def stateCoverage(x,y):
        if(x < y):
            if(x * 3 >= y * 2):
                print("False #1")      
        if(x > y * y):
            print("False #2")
        if(x * 2 < y):
            print("False #3")
        print("True")

x = 5
y = 6

stateCoverage(x,y)
    