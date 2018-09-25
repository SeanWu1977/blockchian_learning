import hashlib


class seancoin:
    @staticmethod
    def sha256(message):
        return hashlib.sha256(message.encode('ascii')).hexdigest()
    
    @staticmethod
    def md5(message):
        return hashlib.md5(message.encode('ascii')).hexdigest()
    

    def proof_of_work(self, message,i=1):
        nonce = 0
        
        while True:
            nonce += 1
            data = f'{message}{nonce}'
            if self.md5(data)[:i] == '0'*i:
                if self.sha256(data)[:i] == '0'*i:
                    return nonce

    def drawpof(self,message):
        i=1
        pof=[]
        while i<=3:
            pof.append([i,self.proof_of_work(message,i)])
            i+=1

        for r in pof:
            data = f'{message}{r[1]}'
            print(f'{r[0]}\n{r[1]}\n{seancoin.md5(data)}\n{seancoin.sha256(data)}')

            
a = seancoin()
msg = '{sean123}'
a.drawpof(msg)



""" result
1
10
06735564c666da0825ef2eb983bfe025
00777136201d684d100a574a022005b1be7d4cd4c40b8e8d6361515658ebec0f
2
51126
00602fe18610e8680a94922ef6ec248a
001b3c94adc50fc5ce484434b9f061ea198ab8b027f810a3f00e16eec1c3cad7
3
22172209
00021f964276e07fd760333f48494fc7
00019158ccbf25c2edd53da49d31bbb1230f343bf10f5f36eca311710ceca5a2
"""
