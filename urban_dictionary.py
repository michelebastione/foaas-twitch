import requests, json, random, re
from bs4 import BeautifulSoup

class Urban_Dict:
    random_url = "https://www.urbandictionary.com/random.php"
    main_url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    headers = {
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
        "X-RapidAPI-Key": "065858bb67mshaa55aeb6e9ad5aap1e15d7jsn295d8b27ecee"
    }

    def random_def(self):
        try:
            response = requests.request("GET", self.random_url)
            assert response.status_code == 200
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find(attrs={"class": "p-5 md:p-8"})
            attrs = data.find_all('div')
            title = attrs[0]
            name = title.h1.text
            return self.search(name)
        except ConnectionError:
            text = "The connection couldn't be established. Try again later."
        except AssertionError:
            text = "This resource is currently not available. Try again later."
        except Exception as e:
            text = "An error occurred while the connection was being established. Try again later."
        return text

    def search(self, term):
        try:
            term = term.capitalize()
            response = requests.request("GET", self.main_url, headers=self.headers, params={"term": term})
            assert response.status_code == 200
            content = json.loads(response.text)
            if not content['list']:
                return "There seem to be no definitions for this expression. Please try again."
            definition = content['list'][0]['definition']
            clean_def = re.sub(r'[\[\]]', '', definition)
            text = f"{term}:\n{clean_def}"
        except ConnectionError:
            text = "The connection couldn't be established. Try again later."
        except AssertionError:
            text = "This resource is currently not available. Try again later."
        except Exception as e:
            text = "An error occurred while the connection was being established. Try again later."
        return text
