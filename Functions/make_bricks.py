def make_bricks(small,big,goal) :
    if goal<=(small+big*5):
        return True 
    elif goal%5 <= small:
        return True
    else :
        return False   
