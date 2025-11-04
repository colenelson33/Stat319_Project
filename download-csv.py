import urllib.request

url = "https://vincentarelbundock.github.io/Rdatasets/csv/carData/UN.csv"
filename = "UN.csv"

urllib.request.urlretrieve(url, filename)
print("✅ File downloaded successfully as", filename)
