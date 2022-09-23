from backend.blockchain.blockchain import BlockChain
from backend.blockchain.block import GENESIS_DATA


def test_blockchain_instance():
    block_chain = BlockChain()

    assert block_chain.chain[0].hash == GENESIS_DATA["hash"]

def test_add_block():
    block_chain = BlockChain()
    block_chain.add_block("test-data") 
    assert block_chain.chain[-1].data == "test-data"