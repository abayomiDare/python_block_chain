
import time
from backend.util.cryptohash import crypto_hash
from backend.config import MINE_RATE

GENESIS_DATA = {
    "timestamp":1,
    "last_hash":"genesis_last_hash",
    "hash":"genesis_hash",
    "data":[],
    "difficulty":3,
    "nonce":"genesis_nonce"
}

class Block:
    """
    Block: A unit of storage
    Stores transactions in a unit that supports a cryptocurrency
    """

    def __init__(self, data, timestamp, hash, last_hash , difficulty, nonce) -> None:
        self.data = data
        self.timestamp = timestamp
        self.hash = hash
        self.last_hash = last_hash
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self) -> str:
        return f"Block( timestamp: {self.timestamp}, last_hash: {self.last_hash}, hash: {self.hash}, difficulty: {self.difficulty}, nonce: {self.nonce}"

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last block and data, until a block
        hash is found that meets the leadinf 0's proof of work requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hash[0:difficulty] != "0" * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(data=data, timestamp=timestamp, last_hash=last_hash, hash=hash, difficulty=difficulty, nonce=nonce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        return Block(**GENESIS_DATA)
        # return Block(timestamp=1, last_hash="genesis_last_hash", hash="genesis_hash", data=[])

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        calaculate the adjusted difficulty according to the Mine_rate.
        increase the difficulty for quickly mine blocks
        decrease the difficulty for slowly mine blocks
        """
        if (new_timestamp -last_block.timestamp) < MINE_RATE:
            return last_block.difficulty -1
        if last_block.difficulty > 0:
            return last_block.difficulty -1
        return 1
        
        # return Block(timestamp=1, last_hash="genesis_last_hash", hash="genesis_hash", data=[])


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "foo")
    print(block)


if __name__ == "__main__":
    main()
