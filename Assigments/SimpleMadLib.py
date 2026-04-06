# Today, I saw a (adjective) (animal) wearing a (adjective) (clothingitem). It was (verbendingining) down the street while holding a (objectt).
# Suddenly, it (pasttenseverb) and shouted, “I love (food)!”
# Then it ran off to (place), never to be seen again.

adjective = input("Give adjective ")
animal = input("Give me an animal ")
clothingitem = input("Give me a clothing item ")
verbendingining = input("Give me a verb ending in -ing ")
objectt = input("Give me an object ")
pasttenseverb = input("Give me a past tense verb ")
food = input("Give me a food ")
place = input("Give me a place ")

print(f"Today, I saw a {adjective} {animal} wearing a {adjective} {clothingitem}. "
      f"It was {verbendingining} down the street while holding a {objectt}. "
      f"Suddenly, it {pasttenseverb} and shouted, 'I love {food}!' "
      f"Then it ran off to {place}, never to be seen again.")