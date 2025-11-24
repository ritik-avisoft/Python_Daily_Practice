'''7. **Sort and Reverse**  
   Given: scores = [88, 92, 75, 95, 81, 90, 78]  
   a) Make a copy of the list and sort it in ascending order  
   b) Sort it in descending order  
   c) Reverse the original list (without sorting)  
   Print all three versions.'''

scores = [5, 95, 81, 90, 78]

scores_copy= scores.copy()
scores_copy.sort()
print(scores_copy)

scores_copy.sort(reverse=True)
print(scores_copy)

scores.reverse()
print(scores)



