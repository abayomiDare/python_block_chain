import hashlib
import json

# def stringify(data):
#     return json.dumps(data)

def crypto_hash(*args):
    """
    Return a sha-256 of the given argument.
    """
    # stringifies any sort of data eg list dict int float, etc
    
    # stringify_data = map(stringify, args)
    # use the sorted function so long the data type may be rearrenged but they are the same

    stringify_data = sorted(map(lambda data: json.dumps(data), args))
    joined_data = "".join(stringify_data)

    return hashlib.sha256(joined_data.encode("utf-8")).hexdigest()


def main():
    print(crypto_hash(4, {"3":7}, "5"))


if __name__ == "__main__":
    main()
