import requests, json, random

with open('more_jokes.json') as file:
    more_jokes = json.loads(file.read())

class Jokes:

    url2 = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=religious,racist,sexist"
    url3 = "https://icanhazdadjoke.com/"

    headers2 = None
    headers3 = {
        "Accept": "text/plain",
        "User-Agent": "twitch-bot (staifresco98@gmail.com)"
    }

    def random_joke(self):
        site = round(random.random()*2)
        if site == 0:
            joke = random.choice(more_jokes)
            return f"{joke['setup']}\n{joke['punchline']}"
        url = eval(f"self.url{site+1}")
        headers = eval(f"self.headers{site + 1}")
        try:
            response = requests.request("GET", url, headers=headers)
            assert response.status_code == 200
            if site == 1:
                content = json.loads(response.text)
                text = content['joke'] if content['type'] == 'single' else f"{content['setup']}\n{content['delivery']}"
            else:
                text = response.text
        except ConnectionError:
            text = "The connection couldn't be established. Try again later."
        except AssertionError:
            text = "This resource is currently not available. Try again later."
        except Exception:
            text = "An error occurred while the content was being retrieved. Try again later."
            raise
        return text
