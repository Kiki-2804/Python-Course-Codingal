sp=int(input("type your selling price"))
cp=int(input("type your cost price"))
if sp<cp:
    print("you have a loss of", cp-sp)
else:
    print("you have a profit of", sp-cp)