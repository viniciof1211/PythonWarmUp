# Implementation of anagram.py - assumes 2 strings since it's dynamically typed

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)