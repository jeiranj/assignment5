class interval(object):
    """represents ths range of integers between lower and upper bounds. the bounds can be inclusive and/or exclusive. The lower should <= the upper bound."""
    def __init__(self, inp):
        intStr=str(inp)
        self.intStr = intStr
        _type_l = 'Exclusive'
        _type_u = 'Exclusive'
        if intStr[0]=='[':
            _type_l='Inclusive'
        if intStr[-1]==']':
            _type_u='Inclusive'
        if _type_l=='Inclusive' and _type_u=='Inclusive':
            _scenario=1
        elif _type_l=='Inclusive' and _type_u!='Inclusive':
            _scenario=2
        elif  _type_l!='Inclusive' and _type_u=='Inclusive':
            _scenario=3
        else:
            _scenario=4
        import re
        b=re.split(r'[\[(,)\]]',intStr)
        lower=int(b[1])
        upper=int(b[2])
        if _scenario==1 and lower>upper:
            raise ValueError('Lower bound %s must be smaller than or equal the upper bound %s'%(lower,upper))
        elif (_scenario==2 or _scenario==3) and lower>=upper:
            raise ValueError('Lower bound %s must be strictly smaller than upper bound %s'%(lower,upper))
        elif _scenario==4 and lower>=upper-1:
            raise ValueError('Lower bound %s must be strictly smaller than uppoer bound %s-1'%(lower,upper))
        if _scenario==1:
            lower=lower
            upper=upper
        elif _scenario==4:
            lower=lower+1
            upper=upper-1
        elif _scenario==2:
            lower=lower
            upper=upper-1
        else:
            lower=lower+1
            upper=upper        
        self._type_l=_type_l
        self._type_u=_type_u
        self.lower=lower
        self.upper=upper
        self._scenario=_scenario        
    def __repr__(self):
        return '%s represents the numbers %d through %d'%(self.intStr,self.lower,self.upper)


def mergeIntervals(int1,int2):
    """marges as many intervals as given in the user input list ints"""
    if not int1 or not int2:
        raise Exception('Not enough user input arguments: at least 2 intervals are required. Try again.')
    int1=[interval(int1).lower,interval(int1).upper]
    int2=[interval(int2).lower,interval(int2).upper]
    ints=[int1,int2]
    ints=sorted(ints,key=lambda ints:ints[0])
    result=[]
    (x,y)=ints[0]
    (xi,yi)=ints[1]
    if xi>y:
        raise Exception('Intervals should overlap. Try again.')
    else:
        y=max(y,yi)
        result=[x,y]
    return result


def mergeOverlapping(intList):
    """marges as many intervals as given in the user input list intList; preserves non-overlaps."""
    if not intList:
        raise Exception('An input is required. Try again.')
    for i in range(0,len(intList)):
        intList[i]=[interval(intList[i]).lower,interval(intList[i]).upper]
    intList=sorted(intList,key=lambda intList:intList[0])
    result=[]
    (x,y)=intList[0]
    for (xi,yi) in intList[1:]:
        if xi<=y:
            y=max(y,yi)
        else:
            result.append([x,y])
            (x,y)=(xi,yi)
    result.append([x,y])
    return result


def insert(intList,newint):
    """inserts new interval newint into intList and merges any if necessary"""
    intList.append(newint)
    return mergeOverlapping(intList)



#
# Python assignment5.py
#
intList=input('List of intervals?')
while True:
    newint=raw_input('New interval?')
    if any(i.isdigit() for i in str(newint)):
        print insert(intList,newint)
        continue
    elif newint in ['quit','Quit']:
        break
    else:
        print "Invalid entry. Try again."
