'''5. **Insert Practice**  
   Given: planets = ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]  
   Insert "Venus" between "Mars" and "Jupiter", and insert "Earth" right after "Mars".  
   Expected result: ["Mars", "Earth", "Venus", "Jupiter", "Saturn", "Uranus", "Neptune"]
'''

planets = ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]  
planets.insert(1,"Venue")
planets.insert(1,"Earth")

print(planets)