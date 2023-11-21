class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
          # Create a list to store population count for each year from 1900 to 2100
        population_count = [0] * 201

        # Iterate through each person's birth and death year
        for person in logs:
            birth, death = person[0], person[1]
            for year in range(birth, death):
                # Increment the population count for each year a person is alive
                population_count[year - 1900] += 1

        max_population = max(population_count)
        earliest_year = population_count.index(max_population) + 1900
        return earliest_year


        