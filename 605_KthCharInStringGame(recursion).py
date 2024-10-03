'''Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the 
English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation
 on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for 
word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.'''

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word='a'
        while len(word)<k:
            new_word=''
            for char in word:
                next_char= chr((ord(char)-ord('a')+1)%26+ord('a'))
                new_word+= next_char

            word+=new_word
        return word[k-1]
k=7
sol=Solution()
print(sol.kthCharacter(k))