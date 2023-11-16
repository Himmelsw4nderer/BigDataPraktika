import csv

# Function to read CSV file and return a dictionary
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

# Function to perform the join on 'movieid'^
def join_data(movies, ratings):
    joined_data = []
    for rating_row in ratings:
        for movie_row in movies:
            if rating_row['movieId'] == movie_row['movieId']:
                joined_row = {**rating_row, **movie_row}
                joined_data.append(joined_row)
    return joined_data

# Read CSV files
movies_data = read_csv('/home/nbax/Proj/BigDataPraktika/CassandraPraktika/ml-latest-small/movies.csv')
ratings_data = read_csv('/home/nbax/Proj/BigDataPraktika/CassandraPraktika/ml-latest-small/ratings.csv')

# Perform the join
result_data = join_data(movies_data, ratings_data)

# Write the result to a new CSV file
fieldnames = result_data[0].keys() if result_data else []
with open('/home/nbax/Proj/BigDataPraktika/CassandraPraktika/ml-latest-small/joined_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header
    csvwriter.writeheader()
    
    # Write data
    csvwriter.writerows(result_data)

print("Join operation completed. Result saved to 'joined_data.csv'.")
