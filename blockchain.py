class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions= []

        #genisis block
        self.new_block(previous_hash=1, proof=100)



    def new_block(self, proof, previous_hash=None):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions=[]
        self.chain.append(block)
        return block


    def new_transaction(self, sender, recepient, amount):

        self.transactions.append({
            'sender': sender,
            'recepient': recepient,
            'amount': amount,
        })

        return self.last_block['index'] + 1 #returns the next block to be mined

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass

