
steps = 0
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    #
    # YOUR IMPLEMENTATION GOES HERE
    #
    acending = False
     #Makes sure that the length is long enough to run in the rest of the code. If not then true anyways.
    if len(lst) <= 2:
        print("List is short")
        return True
    
    #Starts the loop from i = 0 up to the second to last index because the if statement checks the last item on the list
    for i in range(0, len(lst) - 1):
        if lst[i] < lst[i + 1]:
                acending = True
        elif lst[i] > lst[i + 1]:
            if acending == True:
                return False
            else:
                #goes into its own for loop so it doesn't have to check the first if
                for n in range(i, len(lst) - 1):
                    if lst[n] < lst[n + 1]:
                        return False
                return True
    return True
print(monotonic([1,2,3,2]))
print(monotonic([1,2,3,3]))
print(monotonic([5,2,3,3]))
print(monotonic([5,2,3,5]))
