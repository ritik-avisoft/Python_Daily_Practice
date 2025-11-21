'''8. **Basic Slicing**  
   Given: letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
   Write slices to get:
   - First 5 letters
   - Last 4 letters
   - Elements from index 2 to 7 (inclusive)
   - Every second letter starting from the beginning
   - The list in reverse using slicing'''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[:5])
print(letters[-4:])
print(letters[2:8])
print(letters[::2])
print(letters[::-1])
