# Band name generator
import random


titles = ["huge", "pot bellied", "rotten", "grumpy", "salty", "crazy",
          "disfunctional", "rustic", "futuristic", "fabulous", "groovy",
          "royal", "dynamic", "hollow", "ignorant", "illegal", "brawny"
          "blue", "pickled", "prickly", "small", "spherical"]
          
adjs = ["tine", "fat", "shiny", "wreched", "master", "bright", 
        "corrupt", "aggressive", "alarming", "amazing", "magical",
        "masterful", "fierce", "colorless", "fergalicious", "fabulous",
        "measly", "wacky", "tame", "earsplitting", "deez", "lethal"]

plural_nouns = ["rockets", "nuts", "frogs", "unicorns", "bros", "bears",
                "bagelz", "oats", "men", "women", "children", "mamoths",
                "rocks", "days", "dreams", "ropes", "sandwiches",
                "cakes", "wives", "pens", "nuclei", "fungi", "witches"]

def title():
	'''This function chooses a random title for the name'''
	return random.choice(titles)

def adj():
	'''This function chooses a random adj for the band'''
	return random.choice(adjs)

def plural_noun():
	return random.choice(plural_nouns)
	
def main():
	while True:
		name = raw_input("Enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()

main()