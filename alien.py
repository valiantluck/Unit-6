
alien_0 = {1: "green", "points": 5}
print(alien_0[1])
print(alien_0["points"])

modifier = .2

new_points = alien_0["points"]
new_points = new_points * (1 + modifier)
print(f"You just earned {new_points} points!")
print(alien_0)