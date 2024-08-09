import requests
import csv

def authenticate():
    base_url = 'https://www.reddit.com/'
    data = {
        'grant_type': 'password', 
        'username': 'user_name', 
        'password': 'pswd'
    }
    auth = requests.auth.HTTPBasicAuth('user_id', 'access_token')
    headers = {'User-Agent': 'Scrap'}
    
    response = requests.post(base_url + 'api/v1/access_token', data=data, headers=headers, auth=auth)

    if response.status_code == 200:
        print("Successfully received response.")
        response_json = response.json()
        print("Response JSON:", response_json) 
        return response_json.get('access_token')  
    else:
        print(f"Failed to get response: {response.status_code}")
        return None 


def fetch_comments(post_id, token):
    base_url = 'https://oauth.reddit.com'
    headers = {
        'Authorization': f'bearer {token}',
        'User-Agent': 'Scrap'
    }

    url = f'{base_url}/comments/{post_id}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        comments_data = response.json()
        comments_list = []

      
        for comment in comments_data[1]['data']['children']:  
            if 'body' in comment['data']: 
                comments_list.append(comment['data'])




# fetch
    
def fetch_data(token, subreddits, keywords):
    base_url = 'https://oauth.reddit.com'
    headers = {
        'Authorization': f'bearer {token}',
        'User-Agent': 'Scrap'
    }

    data = []

    for subreddit in subreddits:
        search_keywords = keywords + [keyword.lower() for keyword in keywords]
        search_query = f'subreddit:{subreddit} ({ " OR ".join(search_keywords) })'
        url = f'{base_url}/search?q={search_query}&limit=10'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(f"Successfully retrieved data for subreddit: {subreddit}")
            response_json = response.json()
            posts = response_json['data']['children']

            for post in posts:
                post_data = post['data']
                title = post_data['title']
                post_id = post_data['id']
                post_url = f"https://www.reddit.com{post_data}"

                
                comments = fetch_comments(post_id, token)

                data.append({
                    'subreddit': subreddit,
                    'url': post_url,
                    'title': title,
                    'comments': comments,
                    'keywords': keywords
                })
        else:
            print(f"Failed to retrieve data for subreddit: {subreddit}. Status code: {response.status_code}")

    return data

# dump 

def write_to_csv(data, filename='reddit_data.csv'):
    keys = ['subreddit', 'url', 'title', 'comments', 'keywords']
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        
        for entry in data:
            

            comments_str = ' | '.join(entry['comments']) if entry['comments'] else ''
            
            
            writer.writerow({
                'subreddit': entry['subreddit'],
                'url': entry['url'],
                'title': entry['title'],
                'comments': comments_str,
                'keywords': ', '.join(entry['keywords'])
            })


def main():
    token = authenticate()
    
    if token:
        subreddits = ['bespoke', 'fashion', 'B2B', 'design', '3D', 'Visualization', 'Shopify', 'PageBuilder', 'Product', 'Visualstore', 'Threejs']
        keywords = [
            'Personalization',
            'Fashion',
            'Visulisation',
            'Bespoke',
            'Business',
            'Studio',
            'Customization',
            '3D customization',
            '3Dcustomization',
            'B2b'
        ]

        data = fetch_data(token, subreddits, keywords)
        
        
        write_to_csv(data, filename='reddit_data.csv')
    

if __name__ == "__main__":
    main()
