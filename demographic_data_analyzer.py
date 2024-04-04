import pandas as pd

def calculate_demographic_data(print_data=True):
    database = pd.read_csv('adult.data.csv')

    #How many people of each race are represented in this dataset?
    race_count = database.race.value_counts()

    #What is the average age of men?
    #podminene filtry
    avg_male_age = round(database[database.sex =='Male'].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = round(database[database.education == 'Bachelors'].size/(database.size/100), 1)

    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    educated = database[database.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    over_fifty = educated[educated.salary == '>50K']
    educated_perc = round(over_fifty.size/educated.size*100, 1)

    #What percentage of people without advanced education make more than 50K?
    not_educated = database[~database.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    over_fifty_not = not_educated[not_educated.salary == '>50K']
    not_educated_perc = round(over_fifty_not.size/not_educated.size*100, 1)

    #What is the minimum number of hours a person works per week?
    min_hours = database['hours-per-week'].min()

    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    people_min_hours = database[database['hours-per-week'] == min_hours]
    min_hours_over_perc = round((people_min_hours[people_min_hours.salary == '>50K']).size/people_min_hours.size*100, 1)

    #What country has the highest percentage of people that earn >50K and what is that percentage?
    over_country_perc = 100*database[database.salary == '>50K']['native-country'].value_counts()/database['native-country'].value_counts()
    best_country = over_country_perc.idxmax()
    best_country_perc =  round(over_country_perc/best_country*100, 1)
    # Identify the most popular occupation for those who earn >50K in India.
    india = database[database['native-country'] == 'India']
    india_over = india[india.salary == '>50K']
    occup = india_over.occupation.value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", avg_male_age)
        print(f"Percentage with Bachelors degrees: {bachelors}%")
        print(f"Percentage with higher education that earn >50K: {educated_perc}%")
        print(f"Percentage without higher education that earn >50K: {not_educated_perc}%")
        print(f"Min work time: {min_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {min_hours_over_perc}%")
        print("Country with highest percentage of rich:", best_country)
        print(f"Highest percentage of rich people in country: {best_country_perc}%")
        print("Top occupations in India:", occup)

    return {
        'race_count': race_count,
        'avg_male_age': avg_male_age,
        'bachelors': bachelors,
        'educated_perc': educated_perc,
        'not_educated_perc': not_educated_perc,
        'min_hours': min_hours,
        'min_hours_over_perc': min_hours_over_perc,
        'best_country': best_country,
        'best_country_perc':
            best_country_perc,
        'occup': occup
    }
    
