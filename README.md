NEETCODE 150: SUMMER 2025 CHALLENGE!


Arrays:

Contains Duplicates:

  Initial approach (time complexity is O(n2)) : Using  two pointers i and j we iterate the array with i starting at one and j starting at      the next position. We use a while loop ‘while i < len(nums)’  we iterate j though the array ‘while j < len(nums)’ and check if the value     of element at position j is equal to i or not if it is equal we return true if not we return we move j to next element. If we reach the      end of the array and no matches are found we move it to the next element and run the loop again. If at the end no matches are found we       return   false. This approach has one problem that the time complexity is O(n2), as we use two nested while loops.

  Second approach (time complexity is O(n2)): If nums if empty return False. Initialise a list temp and iterate through nums if i is not in    temp then append it to temp else return True. If all elements are added to temp then return False.

  Correct approach (time complexity is O(n)): Initialise a set temp and iterate nums if element is not in temp add it to set else return       True. If all elements are added to temp then return False.

Valid Anagrams:

  Initial Approach (accepted on Leetcode) : Initialize two lists temp1 and temp2 iterate the strings s and t and append there elements to      temp1 and temp 2 respectively. Then check if sorted(temp1) == sorted(temp2)

Two Sum: 

  Initial Approach (accepted on Leetcode): Initialise two pointers i and j and a list temp position i at the first element and j at the next element then iterate j through the array if the element at position j and i add up to give the target integer, append i and j to temp and return temp. If not the move j to the next element if j goes to the end and doesn't add up to the target then we move i to the next element.

Group Anagram:


  Initial Approach: Initialise two pointers i and j and a list temp. For each string i in strs j is the next string iterated through the list and if sorted(i) == sorted(j). Initialize a list store append strs{i} and strs{j} and then append strs to temp. And send j to the next position and return temp, else send j to the next string. 


  Correct Approach: Initialise a dictionary anagram and for each string s in strs. Sort each character in s and join them in sorted_s. Then sorted_s acts as the key to all other anagrams. it appends the original string s to the existing list. inally, it returns the list of all grouped anagrams


Top K Frequent Elements:


  Initial Approach (accepted on Leetcode): Initialise a variable count which is equal to Counter. Creates a dictionary-like object where keys are elements from nums and values are their frequencies. Then we return [x for x, _ in count.most_common(k)]. count.most_common(k)returns a list of the k most frequent elements in descending order of frequency. [x for x, _ in ...] Iterates over the top k (element, frequency) pairs and extracts just the element x, ignoring the frequency _.

Remove Duplicates from Sorted Array:


  Initial Approach (accepted on leetcode): initialise a variable i=0 and j=0 and iterate through the array while i< len(nums) j+=1and then we iterate j though the array and check each element if element at i and j are equal then we remove element at j from the array and move to the next one.

Concatenation of Array:


  Initial Approach (accepted on leetcode): Initialise a list ans and variable i=0 then iterate through the list whale i< lens(nums) and append nums[i] to ans and move i to next position. Then if i==len(nums) set i to 0 then iterate while i<len(nums) append nums[i] to ans and move i to next position then at the end return ans.

Remove Element:


  Initial Approach (accepted on leetcode): initialise a variable i and iterate it through the list while i< len(nums). If the element at position i is equal to the value of the given int then we remove it from the list nums.remove(nums[i]) else we move i to the next position, then at the end we return nums.


Product of Array Except Self:


  Correct Approach: initialize a list temp of length len(nums) with all elements initially set as 1, then initialise a variable mul1=1 and iterate the list for i in range(len(nums)) and let value of temp[i] be equal to mul1 and let value of mul1 be the multiplication of the elements to the left of it, the initialise a variable mul2 and iterate through the list starting for the right this time and keep going back let value of elements temp[i] be equal to the value right now multiplied by mul2 and let mul2 be the multiplication of all elements right of it.








