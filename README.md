NEETCODE 150: SUMMER 2025 CHALLENGE!


Arrays:

Contains Duplicates:

  Initial approach (time complexity is O(n2)) : Using  two pointers i and j we iterate the array with i starting at one and j starting at      the next position. We use a while loop ‘while i < len(nums)’  we iterate j though the array ‘while j < len(nums)’ and check if the value     of element at position j is equal to i or not if it is equal we return true if not we return we move j to next element. If we reach the      end of the array and no matches are found we move it to the next element and run the loop again. If at the end no matches are found we       return   false. This approach has one problem that the time complexity is O(n2), as we use two nested while loops.

  Second approach (time complexity is O(n2)): If nums if empty return False. Initialise a list temp and iterate through nums if i is not in    temp then append it to temp else return True. If all elements are added to temp then return False.

  Correct approach (time complexity is O(n)): Initialise a set temp and iterate nums if element is not in temp add it to set else return       True. If all elements are added to temp then return False.

Valid Anagrams:

  Initial Approach (accepted on Leetcode) : Initialize two lists temp1 and temp2 iterate the strings s and t and append there elements to      temp1 and temp 2 respectively. Then check if sorted(temp1) == sorted(temp2)



