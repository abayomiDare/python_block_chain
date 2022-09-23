from backend.util.cryptohash import crypto_hash


def test_crypto():
    # it should create the same hash for every item even when the order is not sorted
    
    assert crypto_hash("2", [1], {"number":5}) == crypto_hash([1],"2", {"number":5})