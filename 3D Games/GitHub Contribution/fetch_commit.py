
def commit_history(username, year):
    import requests
    from bs4 import BeautifulSoup as bs

    if year == None:
        link = f'https://github.com/{username}'
    else:
        link = f'https://github.com/{username}?tab=overview&from={year}-12-01&to={year}-12-31'

    req = requests.get(link)
    soup = bs(req.content, 'html5lib')

    box = soup.findAll('div', 
            attrs = {'class':'border py-2 graph-before-activity-overview'})

    con = box[0].findAll('rect', 
            attrs = {'class':'ContributionCalendar-day'})

    # print(len(box)) # 1
    # print(len(con)) # 376
    du = {}

    for i,j in enumerate(con):
        try:
            k = j.text.split(', ')
            m = k[0].split()
            n = k[1].split()

            du.update({ i+1: (int(m[0]), m[-1], n[0], n[1], k[2]) })
            # print(f'{i+1}). "{m[0]}", "{m[-1]}", "{n[0]}", "{n[1]}", "{k[2]}"')

            # if not (i+1)%7:
            #     print()
        except:
            pass
    return du

# username = input('Enter Username : ')
# if username == '':
#     username = 'Sen-Takatsuki'
# plain = commit_history(username)
# print(plain)
