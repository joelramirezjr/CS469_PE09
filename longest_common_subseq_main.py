"""longest_common_subseq_main.py

This assignment is to learn about Dynamic Programming.
Given two string sequences from the longest_common_subseq_main.py, complete the functions
in the separate "LCSClass" class within longest_common_subseq.py. 
The main object of the "LCSClass" is to find the length of the longest common subsequence.
(There are many solutions out there, but please try on your own along with the textbook read.)

Examples:
-abca is a subsequence of abccefa with a length of 4
-adf is a subsequence of abcdef with a length of 3
-ebcf is a subsequence of aeebbefc with a length of 3
-vc is not a subsequence of asdf

"""
from longest_common_subseq import LCSClass


def main():
    lcs = LCSClass()
    x = "aaebbecc"
    y = "abc"
    result = lcs.find(x, y)
    print("LCS length: %s" % result)

    lcs = LCSClass()
    x = "aeebbefc"
    y = "ebcf"
    result = lcs.find(x, y)
    print("LCS length: %s" % result)

    lcs = LCSClass()
    x = "asdf"
    y = "vc"
    result = lcs.find(x, y)
    print("LCS length: %s" % result)

if __name__ == "__main__":
        main()
