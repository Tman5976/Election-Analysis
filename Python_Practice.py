counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#What is the score?
score = int(input("What is your test score?"))

#Determine the grade
if score >= 90:
    print("Your grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >= 70:
    print("Your grade is a C.")
elif score >= 60:
    print("Your grade is a D.")
else:
    print("Your grade is a F.")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county, registered_voters in voting_data_dict.items():
    print(county,registered_voters)
    