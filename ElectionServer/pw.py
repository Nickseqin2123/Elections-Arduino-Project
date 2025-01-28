import requests


headers = {
    'Hash': "ABOBA&&12398HDQWHDQWDMITYPUPSIK123SD^^&%(&)_()*_)(*)('']'][;.;'/;[]=---1239120=4889=0``62./,.,>?<><<:PL'[DMITRYKVANTZXCPQPPWPOPIPDASTR"
}


req = requests.get('https://voteschool.ru/api/election/get_election?id=1', headers=headers)

print(req.json())
