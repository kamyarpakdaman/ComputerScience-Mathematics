# The Gale Shapely algorithm is used for solving the matching problem, where we have some candidates and some positions,
# each of which with a specific set of preferences. The algorithm tries to maximize the utility for all sides, maintaining
# some guidelines.

def stableMatching(n, menPreferences, womenPreferences):

    # Initially, all n men are unmarried

    unmarriedMen = list(range(n))

    # None of the men has a spouse yet, we denote this by the value None.

    manSpouse = [None] * n                      

    # None of the women has a spouse yet, we denote this by the value None.

    womanSpouse = [None] * n                      

    # Each man made 0 proposals, which means that his next proposal will be to the woman number 0 in his list.

    nextManChoice = [0] * n                       
    
    # While there exists at least one unmarried man:

    while unmarriedMen:
          
        # Pick an arbitrary unmarried man.

        he = unmarriedMen[0]               

        # Store his ranking in this variable for convenience.

        hisPreferences = menPreferences[he]       

        # Find a woman to propose to.

        she = hisPreferences[nextManChoice[he]] 

        # Store her ranking in this variable for convenience.

        herPreferences = womenPreferences[she]

        # Find the present husband of the selected woman (it might be None).

        currentHusband = womanSpouse[she]         

        # Now "he" proposes to "she". We decide whether "she" accepts, and update the following fields:
        # manSpouse
        # womanSpouse
        # unmarriedMen
        # nextManChoice
        
        if currentHusband == None:
              
          manSpouse[he] = she
          womanSpouse[she] = he
          unmarriedMen.remove(he)
          nextManChoice[he] += 1

        elif herPreferences.index(currentHusband) > herPreferences.index(he):
              
          manSpouse[he] = she
          womanSpouse[she] = he
          unmarriedMen.remove(he)
          unmarriedMen.append(currentHusband)
          nextManChoice[he] += 1

        elif herPreferences.index(currentHusband) < herPreferences.index(he):
          nextManChoice[he] += 1

    return manSpouse

print('\nThanks for reviewing')

# Thanks for reviewing
