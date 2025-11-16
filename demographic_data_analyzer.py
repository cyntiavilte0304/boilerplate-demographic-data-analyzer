import pandas as pd

def calculate_demographic_data(print_data=True):
    # 1. Cargar dataset
    df = pd.read_csv("adult.data.csv")

    # 2. Conteo de razas
    race_count = df["race"].value_counts()

    # 3. Edad promedio de los hombres
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 4. Porcentaje de personas con Bachelor’s
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 5. Educación avanzada
    advanced = ["Bachelors", "Masters", "Doctorate"]

    # Personas con educación avanzada
    higher_education = df[df["education"].isin(advanced)]
    # Personas sin educación avanzada
    lower_education = df[~df["education"].isin(advanced)]

    # 6. % high-education con >50K
    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    # 7. % low-education con >50K
    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    # 8. Mínimo de horas semanales
    min_work_hours = df["hours-per-week"].min()

    # 9. % de ricos que trabajan el mínimo
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 10. País con mayor % de >50K
    country_stats = (
        df[df["salary"] == ">50K"]["native-country"]
        .value_counts() / df["native-country"].value_counts() * 100
    )

    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(
        country_stats.max(), 1
    )

    # 11. Ocupación más común en India para >50K
    india_rich = df[(df["native-country"] == "India")
                    & (df["salary"] == ">50K")]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # Diccionario final que requieren los tests
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupation for >50K in India:", top_IN_occupation)

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


