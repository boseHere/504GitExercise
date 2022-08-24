#!/usr/bin/env python3

"""Here is some documentation lmao"""

def nuc_count_dict(seq):
    nuc_dict = dict()
    for nuc in seq:
        if nuc not in nuc_dict:
            nuc_dict[nuc] = 1
        else:
            nuc_dict[nuc] += 1
    return nuc_dict

def print_nuc_freqs(nuc_dict):
    print('freqs')
    total = float(sum([nuc_dict[nuc] for nuc in nuc_dict.keys()]))
    for nuc in nuc_dict.keys():
        print(nuc + ':' + str(nuc_dict[nuc]/total))


if __name__ == "__main__":
    nuc_dict = nuc_count_dict('ATCTGACGCGCGCCGC') 
    print_nuc_freqs(nuc_dict)

