import requests
import csv

url = "https://dog.ceo/api/breeds/list/all"
response = requests.get(url)
data = response.json()

if data.get("status") != "success":
    raise Exception("API call failed:", data)

breeds = data["message"] 

# Write to CSV
with open("data.csv", mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # header
    writer.writerow(["breed", "sub_breed"])
    # write rows
    for breed, sub_breeds in breeds.items():
        if sub_breeds:  # if there are sub-breeds
            for sub in sub_breeds:
                writer.writerow([breed, sub])
        else:
            writer.writerow([breed, ""])
print("data.csv")
