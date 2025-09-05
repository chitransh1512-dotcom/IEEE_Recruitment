cutoffs = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "MSc Eco", 271),
    ("Pilani", "MSc Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "MSc Eco", 263),
    ("Goa", "MSc Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "MSc Eco", 261),
    ("Hyderabad", "MSc Bio", 234),
]
cutoff_dict = {}
for campus, program, score in cutoffs:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][program] = score
print(cutoff_dict)
