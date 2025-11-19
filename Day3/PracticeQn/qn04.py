'''4. **Append & Extend**  
   Start with an empty list shopping_list = [].  
   Add the following items one by one using append(): "milk", "bread", "eggs".  
   Then add all these items at once using extend(): "butter", "cheese", "yogurt".  
   Print the final list.'''

shopping_list=[]
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")

print("cheacking that producted's are added to the shopping list:-  ", shopping_list)


shopping_list.extend(["butter","cheese","yogurt"])
print(shopping_list)