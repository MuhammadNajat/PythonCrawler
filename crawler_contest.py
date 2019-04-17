import re, requests
from html import  unescape

if __name__ == "__main__":

    teams = []
    basicUrl = 'https://algo.codemarshal.org/contests/icpc-dhaka-18/standings?page='
    #basicUrl = 'https://algo.codemarshal.org/contests/icpc-dhaka-18-mock/standings?page='

    pageId = 1
    while True:
        url = basicUrl + str(pageId)
        content = requests.get(url)
        text = unescape(content.text)
        if not content.ok:
            break
        #matcher = re.compile(r'<td>(\d*)</td><td><a href="/users/icpc_dhaka_18_\d*?">(BUET.*?) \[ Bangladesh University of Engineering and Technology \]</a></td><td><a href="/contests/icpc-dhaka-18/submissions/for\?user=icpc_dhaka_18_.*?"><div class="label label-info">(.*?)</div><div class="label label-default">(.*?)</div></a><td style="width: 24px;"></td></td><td><a href="/contests/icpc-dhaka-18/submissions/')
        matcher = re.compile(r'<td>(\d*)</td><td><a href="/users/icpc_dhaka_18_\d*?">(SUST.*?)\[ .*? \]</a></td><td><a href="/contests/icpc-dhaka-18/submissions/for\?user=icpc_dhaka_18_\d*?"><div class="label label-info">(\d*?)</div><div class="label label-default">(\d*?)</div></a><td style="width: 24px;"></td></td><td><a href="/contests/icpc-dhaka-18/submissions/', re.IGNORECASE)

        items = matcher.findall(text)

        teams += items

        pageId += 1
        if pageId > 2:
            break

    for team in teams:
        print("RANK {}: {} solved {} problems with {} time penalty".format(team[0], team[1], team[2], team[3]))

    try:
        with open('icpc_teams.txt', 'w') as handle:
            handle.write(content.text)
    except:
        print("Error in writing to file")