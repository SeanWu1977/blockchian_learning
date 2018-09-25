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


