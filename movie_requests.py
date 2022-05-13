import requests
import csv

from my_key import api_key

basic_url = 'https://www.omdbapi.com/?i=' 

# read csv and get data
def get_csv():
    with open('oscar_winners.csv') as csvfile:
        data = csv.reader(csvfile)
        call_api(data)

# run over data and format it
def call_api(input):
    
    data = []
    for row in input:
        if row[0] != 'Movie':
            url = basic_url + row[1] + '&apikey=' + api_key
            res = requests.get(url).json()

            title = res.get("Title")
            runtime = int( res.get("Runtime").split()[0])
            genre = res.get("Genre")
            all_awards = res.get("Awards").split()
            wins = int(all_awards[3])
            noms = int(all_awards[6])
            box = int(res.get("BoxOffice").replace(",","")[1:])

            new_row = [title , runtime, genre, wins,noms,box]
            data.append(new_row)
    write_csv(data)

# write to output csv file
def write_csv(data):
    header = ['Movie Title', 'Runtime', 'Genre', 'Award Wins','Award Nominations','Box Office']
    with open('movies.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)


        
if __name__ == "__main__":
    get_csv()