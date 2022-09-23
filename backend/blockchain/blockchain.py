from backend.blockchain.block import Block

class BlockChain:
    """
    BlockChain: a public ledger of transactions.
    Implemented as a list of blocks - data of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self) -> str:
        return f"BlockChain : {self.chain}"


def main():
    block_chain = BlockChain()
    block_chain.add_block("one")
    block_chain.add_block("two")
    print(block_chain)


if __name__ == "__main__":
    main()
