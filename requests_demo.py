import requests

# 屏蔽warning信息
requests.packages.urllib3.disable_warnings()

def get_name():
    print('Separate each name with Space')
    names = input()
    return names.split()

def check_repos(names):
    repo_api = 'https://api.github.com/search/repositories?q='
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
    for name in names:
        #  verify=False 屏蔽ssh验证 https
        repo_info = requests.get(repo_api+name, verify=False).json()['items'][0]

        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']
        ecosys_info = requests.get(ecosys_api+name).json()['total_count']

        print(name)
        print('Start:', str(stars))
        print('Farks:', str(forks))
        print('Ecosys:', str(ecosys_info))
        print('-------------------')


names = get_name()
check_repos(names)