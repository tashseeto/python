groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Facon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

print(groceries)

# print(groceries["Facon"])

groceries["Avos"] = 1.00
groceries["Avos"] = 2.00

for item in groceries:
    print(item, groceries[item])

for key, value in groceries.items():
    print(key, value)

print(groceries.items())

cohorts = {
    "perth": ["Anna", "Viv", "Nic", "Teagen"],
    "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
}

print(cohorts["perth"])

for cohort, peeps in cohorts.items():
    print(cohort, peeps)
    for peep in peeps:
        print(f"     {peep}")

print()

all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

for year, cohorts in all_cohorts.items():
    print(year)
    for city, cohort in cohorts.items():
        print(f"   {city}")
        for peep in cohort:
            print(f"    {peep}")
