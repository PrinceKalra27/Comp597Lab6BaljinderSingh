import requests
from requests import get
from sys import argv as cmd_line_prmtr

def main():
    name_pkmn = cmd_line_prmtr[1]
    dctry = get_poke_info(name_pkmn)
    if dctry:
        user_strg = get_poke_strng(dctry)
        pastbn_url = post_pastebin(user_strg[0], user_strg[1])
        print(pastbn_url)

def get_poke_info(name_pkmn):
    print("Pokemon information -", end=' ')
    url_poke = 'https://pokeapi.co/api/v2/pokemon/'
    rspnse = requests.get(url_poke + str(name_pkmn))

    if rspnse.status_code == 200:
        print('Response: Success' , 'Hooray!!!' , '\n')
        return rspnse.json()
    else:
        print('No luck, Sorry :-(')

def get_poke_strng(user_dctry):
    title = user_dctry['name'] + "Abilities of Pokemon"
    body_txt = "Abilities are :-" + user_dctry['abilities'][0]['ability']['name'] + "\n"
    body_txt = "Abilities are :-" + user_dctry['abilities'][1]['ability']['name']
    return (title, body_txt)

def post_pastebin(title, body_txt):
    print("Posting Pastbin in Process ..." , end=' ')

    requestParams = {
        'api_dev_key': 'f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X' ,
        'api_option': 'paste',
        'api_paste_code': body_txt ,
        'api_paste_name': title
        }
    URL_rspnse = 'https://pastebin.com/api/api_post.php'
    rspnse = requests.post(URL_rspnse, data=requestParams)

    if rspnse.status_code == 200:
        print('Success!!')
        return rspnse.text 
    else:
        print('Failed: Response is :', rspnse.status_code)
        return rspnse.status_code

main()
#Error pastein 422
