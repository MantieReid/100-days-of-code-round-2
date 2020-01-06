
def isNStraightHand( hand: List[int], W: int) -> bool:

    hand.sort() # sort the hand list
    while hand: # start iterating through the hand
      try:

        base = hand[0] # base will equal the first element in hand
        for i in range(W): # make numbers from 1 to w.
          hand.remove(base + i) # remove selected elements from the hand.

      except:
        print("false") # if not able to remove W amount of elements, then return false
        return False
    print("true")  # if able to remove W amount of elements, then return true.
    return True






