import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1
    )

    # Higher education: Bachelors, Masters, Doctorate
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Lower education: everything else
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage of high-education people earning >50K
    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] /
         higher_education.shape[0]) * 100, 1
    )

    # Percentage of low-education people earning >50K
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] /
         lower_education.shape[0]) * 100, 1
    )

    # Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # How many people work that amount?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Percentage of those people earning >50K
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] /
         num_min_workers.shape[0]) * 100, 1
    )

    # Country with highest percentage of >50K earners
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total_counts = df['native-country'].value_counts()

    country_percentage = (country_rich_counts / country_total_counts) * 100

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # Most popular occupation for >50K earners in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

