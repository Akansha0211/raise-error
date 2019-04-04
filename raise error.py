a=[1,2,3,'33',4,0,'4fg',8]
for i in a:
    try:
        h=1/int(i)
    except ZeroDivisionError:
        raise ZeroDivisionError('forcely generated error')
    except:
        pass
