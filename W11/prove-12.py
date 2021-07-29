class CountryData:
    def __init__(self, entity: str, code: str, year: str, life_expectancy: int):
        self.entity = entity
        self.code = code
        self.year = year
        self.life_expectancy = life_expectancy


max_life_country = None
min_life_country = None

max_life_country_by_year = None
min_life_country_by_year = None
total_life_expectancy_by_year = 0
countries_by_year_count = 0

def get_highest_life_expectancy(current_country: CountryData, next_country: CountryData) -> CountryData:
    if current_country == None or next_country.life_expectancy > current_country.life_expectancy:
        return next_country
    else:
        return current_country

def get_lowest_life_expectancy(current_country: CountryData, next_country: CountryData) -> CountryData:
    if current_country == None or next_country.life_expectancy < current_country.life_expectancy:
        return next_country
    else:
        return current_country

year_of_interest = input("Enter the year of interest: ")

with open('./life-expectancy.csv') as data:
    # skip the header line
    next(data)
    for line in data:
        entity, code, year, life_expectancy = line.strip().split(',')
        country = CountryData(entity, code, year, float(life_expectancy))

        max_life_country = get_highest_life_expectancy(max_life_country, country)
        min_life_country = get_lowest_life_expectancy(min_life_country, country)

        if year_of_interest == country.year:
            max_life_country_by_year = get_highest_life_expectancy(max_life_country_by_year, country)
            min_life_country_by_year = get_lowest_life_expectancy(min_life_country_by_year, country)
            total_life_expectancy_by_year += country.life_expectancy
            countries_by_year_count += 1


print(f"\nThe overall max life expectancy is: {max_life_country.life_expectancy} from {max_life_country.entity} in {max_life_country.year}")
print(f"The overall min life expectancy is: {min_life_country.life_expectancy} from {min_life_country.entity} in {min_life_country.year}\n")

print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {(total_life_expectancy_by_year / countries_by_year_count):.2f}")
print(f"The max life expectancy was in {max_life_country_by_year.entity} with {max_life_country_by_year.life_expectancy}")
print(f"The min life expectancy was in {min_life_country_by_year.entity} with {min_life_country_by_year.life_expectancy}")
