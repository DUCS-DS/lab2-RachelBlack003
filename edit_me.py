def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    acending = False
    decending = False
     #Makes sure that the length is long enough to run in the rest of the code. If not then true anyways.
    if len(lst) <= 2:
        return True
    
    #Starts the loop from i = 0 up to the second to last index because the if statement checks the last item on the list
    for i in range(0, len(lst) - 1):
        if lst[i] < lst[i + 1]:
            if decending == True:
                return False
            acending = True
        elif lst[i] > lst[i +1]:
            if acending == True:
                return False
            decending = True
    return True
assert monotonic([1,12])
assert monotonic([1,2,2,3])
assert not monotonic([1,2,3,3, 1])
assert not monotonic([5,2,3,3])
