# Sorts National Olympics Committees
nocs_table = (
    "United States",
    "China",
    "Japan",
    "Great Britain",
    "Russia",
    "Australia",
    "The Netherlands",
    "France",
    "Germany",
    "Italy",
    "Canada",
    "Brazil",
    "New Zealand",
    "Cuba",
    "Hungary",
    "South Korea",
    "Poland",
    "Czech Republic",
    "Kenya",
    "Norway",
)


print(f"Five best NOCs: {nocs_table[0:6]}")
print(f"16 to 20th NOCs: {nocs_table[-4:]}")
print(f"NOCs in alphabetical order: {sorted(nocs_table)}")
print("Brazil result: {}".format({nocs_table.index("Brazil")}))
