Here I wrote a code where I mine three blocks and add them to a Blockchain
# Blockchain: Mining
<img src="https://github.com/Relor91/Lorenzo_Portfolio/blob/main/images/Blockchain/BlockchainMining/BlockchainMining.JPG" alt="drawing" width="350" align="left"/><p>
* Created a **BLOCK Class** and a **Mine** algorithm.
* The **BLOCKS** are encrypted with the **SHA256** hash function and each block has it's difficulty increased by 1 starting from 4 zeros.
* **Mining** will loop through all the blocks guessing their **Hash** and will stop when the guessed hash starts with the number of zeros previously set by the Mining Function, after that it will attach the Block to the **Blockchain**. The function is programmed to fail if the **Nonce** reaches 1 × 10⁹ trials.
* For each **successfully mined** Block, the Mine function will output the time needed to mine the block, the number of trials and the mined hash.
* At the very end, the Blockchain is printed.<p>
