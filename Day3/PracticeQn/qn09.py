'''9. **Slicing with Step**  
   Given: nums = list(range(1, 21))  # [1, 2, 3, ..., 20]  
   Use slicing to create:
   - All even numbers
   - All multiples of 3
   - Numbers from 10 to 15 inclusive
   - The list reversed in one line'''

nums = list(range(1, 21))  # [1, 2, 3, ..., 20]

print(nums[1::2])
print(nums[2::3])
print(nums[9:15])
print(nums[::-1])
