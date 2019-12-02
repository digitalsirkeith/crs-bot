import requests


crs_url = 'https://www.crs.upd.edu.ph/'

def main():
    response = requests.get(crs_url)
    print(response)

if __name__ == '__main__':
    main()