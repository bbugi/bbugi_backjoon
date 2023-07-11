import itertools

def solution(spell, dic):
    word = list(itertools.permutations(spell, len(spell)))
    
    for w in word:
        if ''.join(w) in dic:
            return 1
    
    return 2