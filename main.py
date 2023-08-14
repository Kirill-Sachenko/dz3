import requests

def find_smartest_superhero(superheroes):
    max_intelligence = -1
    smartest_superhero = None

    response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    if response.status_code == 200:
        data = response.json()

        for superhero in data:
            if superhero['name'] in superheroes:
                intelligence = int(superhero['powerstats']['intelligence'])
                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    smartest_superhero = superhero['name']
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    return smartest_superhero

if __name__ == '__main__':
    superheroes = ['Hulk', 'Captain America', 'Thanos']
    smartest = find_smartest_superhero(superheroes)
    if smartest:
        print(f"The smartest superhero is: {smartest}")
    else:
        print("No data available.")