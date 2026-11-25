def myFun():
    print("Hello There")
    print(__name__) # it give __main__ for this file but for other imported file it give module



if __name__ == "__main__": # if this code is directly executed by running file its present in then only this code runs
    myFun()
    print(__name__)    # here __Name__ give main because it is called in this.