import os
import requests
import pandas as pd

def get_data(url='http://ddragon.leagueoflegends.com/cdn/14.8.1/data/pt_BR/champion.json'):
    response = requests.get(url)

    return response.json()['data']

def transform_to_df(data):
    ids = []
    for _ in data:
        ids.append(_)

    champions_all = []
    for _ in ids:
        champions_all.append(data.get(_))

    champions = []
    for champ in champions_all:
        champions.append({
            'name': champ.get('name'),
            'image': champ.get('image')['full'],
            'tags': champ.get('tags'),
            'hp': champ.get('stats')['hp'],
            'hpperlevel': champ.get('stats')['hpperlevel'],
            'mp': champ.get('stats')['mp'],
            'mpperlevel': champ.get('stats')['mpperlevel'],
            'movespeed': champ.get('stats')['movespeed'],
            'armor': champ.get('stats')['armor'],
            'armorperlevel': champ.get('stats')['armorperlevel'],
            'spellblock': champ.get('stats')['spellblock'],
            'spellblockperlevel': champ.get('stats')['spellblockperlevel'],
            'attackrange': champ.get('stats')['attackrange'],
            'hpregen': champ.get('stats')['hpregen'],
            'hpregenperlevel': champ.get('stats')['hpregenperlevel'],
            'mpregen': champ.get('stats')['mpregen'],
            'mpregenperlevel': champ.get('stats')['mpregenperlevel'],
            'crit': champ.get('stats')['crit'],
            'critperlevel': champ.get('stats')['critperlevel'],
            'attackdamage': champ.get('stats')['attackdamage'],
            'attackdamageperlevel': champ.get('stats')['attackdamageperlevel'],
            'attackspeed': champ.get('stats')['attackspeed'],
            'attackspeedperlevel': champ.get('stats')['attackspeedperlevel'],
        })

    return pd.DataFrame(champions)

def save_images(df):
    folder = "assets/LoL"
    os.makedirs(folder, exist_ok=True)

    df['image_path'] = folder+'/'+df['image'].astype(str)
    df['image_url'] = 'http://ddragon.leagueoflegends.com/cdn/14.8.1/img/champion/'+df['image'].astype(str)

    for _, row in df.iterrows():
        url = row["image_url"]
        
        filename = os.path.join(folder, url.split("/")[-1])
        
        if os.path.exists(filename):
            print(f"Já existe: {filename}")
            continue
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"Salvo: {filename}")
            else:
                print(f"Erro {response.status_code}: {url}")
        
        except Exception as e:
            print(f"Falha ao baixar {url}: {e}")

if __name__ == '__main__':
    data = get_data()
    df = transform_to_df(data)
    save_images(df)
    
    df.to_csv('champions_db.csv', index=False)
