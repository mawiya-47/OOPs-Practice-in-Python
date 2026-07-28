class fb_player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.score = 0

    def update_score(self, score):
        self.score += score

    def show_info(self):
        return f"Name: {self.name}, Position: {self.position}, Team: {self.team}, Score: {self.score}"


def compare(p1, p2):
    if p1.score > p2.score:
        print(f"{p1.name} has a higher score than {p2.name}")
    elif p1.score < p2.score: 
        print(f"{p2.name} has a higher score than {p1.name}")
    else:
        print(f"{p1.name} and {p2.name} have the same score")


# Create players
p1 = fb_player("Rodri", "CDM", "Spain")
p2 = fb_player("Neymar", "LW", "Brazil")

# Update scores
p1.update_score(10)
p2.update_score(8)

# Show player information
p1.show_info()
p2.show_info()

# Compare scores
compare(p1, p2)

print("\n----- Reference Example -----")

# New object with empty values
p1 = fb_player("", "", "")
p2 = p1

print(p1.name)
print(p2.name)

# Update score through p2
p2.score += 7

# Comparison of attributes
print(p2.name == p1.name)
print(p2.score == p1.score)
print(p2.position == p1.position)
print(p2.team == p1.team)

# Display final information
p1.show_info()
p2.show_info()




print(p2.name == p1.name)       
print(p2.score == p1.score)    
print(p2.position == p1.position) 
print(p2.team == p1.team)       

#add refference and address
print("Reference Example")
print("Address of p1:", hex(id(p1)))
print("Address of p2:", hex(id(p2)))


#if change in p1 so no change in p2 check objects
p1.name = "Updated Name"
print("After updating p1:")
p1.show_info()
p2.show_info()
print(p1.show_info())