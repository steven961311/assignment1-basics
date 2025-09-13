import os
import regex as re
import argparse

def train_bpe(
    input_path: str | os.PathLike,
    vocab_size: int,
    special_tokens: list[str],
    **kargs,
) -> tuple[dict[int, bytes], list[tuple[bytes, bytes]]]:
    
    pretokenize(input_path, special_tokens)

    return

def pretokenize(
    input_path: str | os.PathLike,
    special_tokens: list[str] 
) -> list[bytes]:
    words = []
    PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    with open(input_path, 'r') as f:
        corpus = f.read()
        corpus_nospec = corpus.split("|".join(special_token for special_token in special_tokens))
        print(re.split("|".join(map(re.escape, special_tokens)), corpus))
        print(corpus_nospec)
        for doc in corpus_nospec:
            for word in re.finditer(PAT, doc):
                print(word)
                break

def main():
    data_path = '/home/steven961311/assignment1-basics/tests/fixtures/tinystories_sample.txt'
    print(data_path)

    train_bpe(data_path, 512, ["<|endoftext|>"])
    #special_tokens = ["<|endoftext|>", "<|startoftext|>"]
    #print("|".join(special_tokens))
    #print('|'.join(map(re.escape, special_tokens)))

if __name__ == "__main__":
    main()