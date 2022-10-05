from hashlib import sha256
import time

class Block:
    def __init__(self, block_number,previous_hash, transactions,nonce):
        self.block_number = block_number
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = nonce
        string_to_hash = "".join(transactions) + previous_hash + str(block_number) + str(nonce)
        self.block_hash = SHA256(string_to_hash)

def SHA256(text):
    hashcode = sha256(text.encode()).hexdigest()
    return hashcode
    #return ''.join(format(ord(n),'b') for n in hashcode) #if you want to see then hash in binary

def mine(block,prefix_zeros):
    NONCE_MAX = 1000000000
    start_time = time.time()
    prefix_zeros_str = '0'*prefix_zeros
    for nonce in range(NONCE_MAX):
        block.nonce = nonce
        string_to_hash = "".join(block.transactions) + block.previous_hash + str(block.block_number) + str(nonce)
        new_hash = SHA256(string_to_hash)
        if new_hash.startswith(prefix_zeros_str):
            total_time = str(round(time.time() - start_time, 1))
            blockchain.append(block)
            print(f"The following hash has been mined in {total_time} seconds after {nonce} trials:\n {new_hash}")
            return new_hash
    raise BaseException(f"Mining Failed after reaching {NONCE_MAX} trials")

blockchain = []

genesys_block = Block(1,"Vires In Numeris",["Transaction1","Transaction2","Transaction3"],1)
second_block = Block(2,genesys_block.block_hash,["Transaction4","Transaction5","Transaction6"],1)
third_block = Block(3,second_block.block_hash,["Transaction7","Transaction8","Transaction9"],1)


new_hash = mine(genesys_block,4)
new_hash = mine(second_block,5)
new_hash = mine(second_block,6)

print(f"The following Blockchain has been mined: \n"
      f"{blockchain}")




