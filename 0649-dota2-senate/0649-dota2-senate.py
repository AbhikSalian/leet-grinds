class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        while True:
            if senate[0]=='R':
                if 'D' not in senate:
                    return 'Radiant'
                else:
                    for i in range(1,len(senate)):
                        if senate[i]=='D':
                            senate=senate[0:i]+senate[i+1:]
                            break
                    senate=senate[1:]+senate[0]
            elif senate[0]=='D':
                if 'R' not in senate:
                    return 'Dire'
                else:
                    for i in range(1,len(senate)):
                        if senate[i]=='R':
                            senate=senate[0:i]+senate[i+1:]
                            break
                    senate=senate[1:]+senate[0]

