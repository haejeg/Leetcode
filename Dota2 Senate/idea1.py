class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = list(senate)
        print(senators)
        voted = []
        unvoted = []
        banned = []
        length = len(senators)
        while length > 0:
            if length == 1:
                voted.append(senators[0])
                if voted and senators[0] != voted[0]:
                    banned.append(voted[0])
                    voted.pop(0)
                    print("REMOVED FIRST VOTED SENATOR")
                senators.pop(0)
                senators = voted
                # length -= 1
                if not voted or voted.count(senators[0]) == len(voted):
                    if senators[0] == 'R':
                        return "Radiant"
                    elif voted[0] == 'D':
                        return "Dire"
                print(senators)
                print("Voted: ", voted)
                print("Banned: ", banned)
            elif senators[0] != senators[1]:
                voted.append(senators[0])
                senators.pop(0)
                length -= 1
                banned.append(senators[0])
                senators.pop(0)
                length -= 1
                print(senators)
                print("Voted: ", voted)
                print("Banned: ", banned)
            elif senators[0] == senators[1]:
                print("Equal Receivance")
                voted.append(senators[0])
                senators.pop(0)
                length -= 1
                print(senators)
                print("Voted: ", voted)
                print("Banned: ", banned)
        print("Voted: ", voted)
        print("Banned: ", banned)
        