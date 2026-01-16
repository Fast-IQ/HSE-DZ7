from requests import get

def get_post_ver1():
    response = get(
        f'https://jsonplaceholder.typicode.com/posts'
        f'?_limit=10'
    )

    for i in range(5)  :
        print(i+1, ' Title: ', response.json()[i]['title'])
        print('Body: ', response.json()[i]['body'])

def get_post_ver2():
    response = get(
        f'https://jsonplaceholder.typicode.com/posts'
        f'?_limit=5'
    )

    for post in response.json()  :
        print('Title: ', post['title'])
        print('Body: ', post['body'])
        print(' ')

if __name__ == "__main__":
    get_post_ver1()
    get_post_ver2()