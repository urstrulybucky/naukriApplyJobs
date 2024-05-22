import requests
import json


def apply_jobs(job_list):
    url = "https://www.naukri.com/cloudgateway-workflow/workflow-services/apply-workflow/v1/apply"

    payload = json.dumps({
    "strJobsarr": [
        job_list
    ],
    "logstr": "--jobsearchDesk-3-F-0-1--17136118180512495-",
    "flowtype": "show",
    "crossdomain": True,
    "jquery": 1,
    "rdxMsgId": "",
    "chatBotSDK": True,
    "mandatory_skills": [],
    "optional_skills": [
        "Cloud",
        "Data analytics",
        "Developer Trainee",
        "AWS",
        "Python",
        "SQL"
    ],
    "applyTypeId": "107",
    "closebtn": "y",
    "applySrc": "jobsearchDesk",
    "sid": "17136118180512495",
    "mid": ""
    })
    headers = {
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'ACCESSTOKEN = eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJkZXZpY2VUeXBlIjoiZDNza3QwcCIsInVkX3Jlc0lkIjoxMjA5MTQyMTMsInN1YiI6IjEyOTU2MTM5NSIsInVkX3VzZXJuYW1lIjoiaGltYW5zaHUubmluamE3QGdtYWlsLmNvbSIsInVkX2lzRW1haWwiOnRydWUsImlzcyI6IkluZm9FZGdlIEluZGlhIFB2dC4gTHRkLiIsInVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiaXBBZHJlc3MiOiIxMDMuNi4xNTkuNzYiLCJ1ZF9pc1RlY2hPcHNMb2dpbiI6ZmFsc2UsInVzZXJJZCI6MTI5NTYxMzk1LCJzdWJVc2VyVHlwZSI6ImpvYnNlZWtlciIsInVzZXJTdGF0ZSI6IkFVVEhFTlRJQ0FURUQiLCJ1ZF9pc1BhaWRDbGllbnQiOmZhbHNlLCJ1ZF9lbWFpbFZlcmlmaWVkIjp0cnVlLCJ1c2VyVHlwZSI6ImpvYnNlZWtlciIsInNlc3Npb25TdGF0VGltZSI6IjIwMjQtMDUtMjJUMTQ6MDQ6NDUiLCJ1ZF9lbWFpbCI6ImhpbWFuc2h1Lm5pbmphN0BnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MTYzNzA0ODUsInRva2VuVHlwZSI6ImFjY2Vzc1Rva2VuIiwiaWF0IjoxNzE2MzY2ODg1LCJqdGkiOiI3MDI2ODMzMzNjZmI0MjhiYTQ1Zjg0NzEyNTllMTc5ZiJ9.sdp-XH3lJ3TRd5e_vFmkv6tTHqstO7Oe7T-DabjfVSDdO0ZxeTwtMcfySox4wFnvDb1CfGd1H8oUDFp56gBlBS8-tBOrhK8THkGFVFtJMS2x2fs3QocfaEybQO-XBPo_0mlSAU41vEJcR5eG9yKJgNV6zRm2QhIu6lUhYAKGFK9eg4MTV2dkrEAQZZ7636keyTeOvJeD54ede2mzQCJdGaymiEiQZv5KBp7uzWl0yycRtHSu-cDb3vvXZBLG8Ro8GOH06zejwW-3IUxjm9NDOZFyDS3CC2wG-QMimFpCZ8QVmGujRApUP-clwOzjUYLWrgEaPV_VSuMpqDSd6aL-Og',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'systemid': 'jobseeker',
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'clientId': 'd3skt0p',
    'Referer': 'https://www.naukri.com/job-listings-python-developer-trainee-everforce-llc-bengaluru-0-to-1-years-120820500090?src=jobsearchDesk&sid=17136118180512495&xp=3&px=1&nignbevent_src=jobsearchDeskGNB',
    'appId': '121',
    'sec-ch-ua-platform': '"Linux"',
    'Cookie': 'J=0; _t_ds=f37d9f01713611223-21f37d9f0-0f37d9f0; ak_bmsc=A71B6FB09DF0881D47CFF02B7A1CA7FD~000000000000000000000000000000~YAAQxP7UFzqZcs+OAQAAmPo6+xfBghd1CzbMDuYKcv1skx6yaAha3jA/8XmqVJWf4rWdVlpCfgo7xQ814chfXKr34rBiYdoh0zbmqcJbHKezNPmVbBoeaa8SgKX51592E+FdSjIEXG4PwMhQBax23B5EEY1egqe38Ahltz4Pq5Lvd4iQRhS0ez6ZkU8kniCTQ+h/CvqSkL9NPVqJNHAYj9RX5vFkhkP6gwsUOpRqqTZxyMKhrFiomNdmzSMoGvNrRPdpkjMJnQ6NtBxS0+rgKp1w8gDNouVVolzHXir/Gwz8uDkaH8hMZWVXh5skPA56SiFVsFvxumnl1UxBDiyBsufaaNuMfIi+XsAJCh5QqOAJxneKgQeb2ax+gA==; bm_sv=93AEE9395D5C49D3CA50EB5381B287C8~YAAQxP7UFwi8cs+OAQAA4xI8+xcqhKcmH5g1UmUu9m4b/hSC1AEKgIYl0FXr1KkWnv8p12cyfZpjmcQY8Uudq9cbqC4ILR0gG9/wF+dZwvPAKDdopT4hl95E51/MU5q/uZg4V9k07msBLrXIQLrN8QoQM9fu3EXz+hPpg8+9Y9RUK+NyyQjDfp6SdCQ3OQaKiYySWjdnWagJ+s33BhBgTRxBFyj+d8VxJYgvL7a5LIHhdsTu425e48H63zPi1MJ+~1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_job_list():


    url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=python%20software%20developer&sort=p&pageNo=1&cityTypeGid=97&jobAge=1&k=python%20software%20developer&nignbevent_src=jobsearchDeskGNB&cityTypeGid=97&jobAge=1&seoKey=python-software-developer-jobs&src=cluster&latLong=12.9129842_77.6421466&sid=17163702205602858_1"

    payload = {}
    headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'appid': '109',
    'authorization': 'Bearer eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTIwOTE0MjEzLCJzdWIiOiIxMjk1NjEzOTUiLCJ1ZF91c2VybmFtZSI6ImhpbWFuc2h1Lm5pbmphN0BnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlwQWRyZXNzIjoiMTAzLjYuMTU5Ljg3IiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjEyOTU2MTM5NSwic3ViVXNlclR5cGUiOiJqb2JzZWVrZXIiLCJ1c2VyU3RhdGUiOiJBVVRIRU5USUNBVEVEIiwidWRfZW1haWxWZXJpZmllZCI6dHJ1ZSwidWRfaXNQYWlkQ2xpZW50IjpmYWxzZSwidXNlclR5cGUiOiJqb2JzZWVrZXIiLCJzZXNzaW9uU3RhdFRpbWUiOiIyMDI0LTA0LTIwVDEwOjM4OjM1IiwidWRfZW1haWwiOiJoaW1hbnNodS5uaW5qYTdAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzEzNjE0OTEzLCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlhdCI6MTcxMzYxMTMxMywianRpIjoiYTQyMGU3MWQwZDhhNGZmMWI4ZmY5YzY4MDQ3OTg5ZTcifQ.hRu6ka2gxwMI-kpjnazVr2KTaR2TfwWfML8YXAmPDzeGZM3JeN0H-K4RSsO7vJ66bOuI1a0xLGEnFMb2bbwUrNZntxBbzrg_KID82fJIlptCV5RyIM0z8M1wM8VL4MGV0pbD20CndDbie_qpQiUsAejt3dGCsPyZOH5GT_1JRbTqQTZbzSwbBrwnnrWF3XUQzxJlwS3JSoqDeaxFVekWbs9QJFTYXAhhgC7CC-hiwvD2YJNA712XMQOYLSDrhwCstVSPx7mAmgMtTjME2At8YA5V5O-3vyCuUzXSxCz_d1jeKBDvx7zL2TMqdCQ7cLKCCQBIWKrtniNnZDYw0MBKeA',
    'clientid': 'd3skt0p',
    'content-type': 'application/json',
    'cookie': '_t_ds=1efad1c51713588832-31efad1c5-01efad1c5; J=0; PHPSESSID=c50kkk777nlb19ndnvnjm7j55f; _ga=GA1.1.647748750.1713588833; test=naukri.com; _t_s=direct; _t_r=1030%2F%2F; persona=default; _gcl_au=1.1.1522089923.1713588840; jd=170424009788; nauk_rt=eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTIwOTE0MjEzLCJzdWIiOiIxMjk1NjEzOTUiLCJ1ZF91c2VybmFtZSI6ImhpbWFuc2h1Lm5pbmphN0BnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlwQWRyZXNzIjoiMTAzLjYuMTU5Ljg3IiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjEyOTU2MTM5NSwic3ViVXNlclR5cGUiOiJqb2JzZWVrZXIiLCJ1c2VyU3RhdGUiOiJBVVRIRU5USUNBVEVEIiwidWRfaXNQYWlkQ2xpZW50IjpmYWxzZSwidWRfZW1haWxWZXJpZmllZCI6dHJ1ZSwidXNlclR5cGUiOiJqb2JzZWVrZXIiLCJzZXNzaW9uU3RhdFRpbWUiOiIyMDI0LTA0LTIwVDEwOjM4OjM1IiwidWRfZW1haWwiOiJoaW1hbnNodS5uaW5qYTdAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzQ1MTI1NzE1LCJ0b2tlblR5cGUiOiJyZWZyZXNoVG9rZW4iLCJpYXQiOjE3MTM1ODk3MTUsImp0aSI6ImE0MjBlNzFkMGQ4YTRmZjFiOGZmOWM2ODA0Nzk4OWU3In0.oU6IZHcWMgrvi8YUBECLRbrgYufpGIftMV20MTYP1AFHxEzyRKbk15kE1TLG3Ku8Z_hXYEplkknRzt0pfRqdtnjIOt0AFDFcp_0JXJs7OpdKIgK1y6slSr2O0WcfiECQXFDrQKdrvwXtuBoJYfVt9Y3RcKfBvQ7rAmdXbKt9ql_xmKU4HDHTk3XOL9wxQdWP6Ighly2lg6uPegrYz7SdeZY6f809bhWH3bbokyvEZbnqakZF88jKqUbgPeyApL1l0zci9g7E_z8zkdL2nIPHX3zUaHjjoi_Chy-o9GGrjdRNZud3MCqwZXHG3B-X7ne-LkaKoshEjszrBBoqFW_B7A; nauk_sid=a420e71d0d8a4ff1b8ff9c68047989e7; nauk_otl=a420e71d0d8a4ff1b8ff9c68047989e7; NKWAP=2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255~2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255~1~0; MYNAUKRI[UNID]=102fd0404742cdbc73; nauk_ps=default; nauk_at=eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTIwOTE0MjEzLCJzdWIiOiIxMjk1NjEzOTUiLCJ1ZF91c2VybmFtZSI6ImhpbWFuc2h1Lm5pbmphN0BnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlwQWRyZXNzIjoiMTAzLjYuMTU5Ljg3IiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjEyOTU2MTM5NSwic3ViVXNlclR5cGUiOiJqb2JzZWVrZXIiLCJ1c2VyU3RhdGUiOiJBVVRIRU5USUNBVEVEIiwidWRfZW1haWxWZXJpZmllZCI6dHJ1ZSwidWRfaXNQYWlkQ2xpZW50IjpmYWxzZSwidXNlclR5cGUiOiJqb2JzZWVrZXIiLCJzZXNzaW9uU3RhdFRpbWUiOiIyMDI0LTA0LTIwVDEwOjM4OjM1IiwidWRfZW1haWwiOiJoaW1hbnNodS5uaW5qYTdAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzEzNjE0OTEzLCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlhdCI6MTcxMzYxMTMxMywianRpIjoiYTQyMGU3MWQwZDhhNGZmMWI4ZmY5YzY4MDQ3OTg5ZTcifQ.hRu6ka2gxwMI-kpjnazVr2KTaR2TfwWfML8YXAmPDzeGZM3JeN0H-K4RSsO7vJ66bOuI1a0xLGEnFMb2bbwUrNZntxBbzrg_KID82fJIlptCV5RyIM0z8M1wM8VL4MGV0pbD20CndDbie_qpQiUsAejt3dGCsPyZOH5GT_1JRbTqQTZbzSwbBrwnnrWF3XUQzxJlwS3JSoqDeaxFVekWbs9QJFTYXAhhgC7CC-hiwvD2YJNA712XMQOYLSDrhwCstVSPx7mAmgMtTjME2At8YA5V5O-3vyCuUzXSxCz_d1jeKBDvx7zL2TMqdCQ7cLKCCQBIWKrtniNnZDYw0MBKeA; is_login=1; failLoginCount=0; ak_bmsc=A32064E22893E988E66A708487B66092~000000000000000000000000000000~YAAQfP7UFyxVMc2OAQAATpYx+xdwizgv2kNrMKcsjBJEFys3sxGy35iXPUa4irUuaw+pstw8ff6M+B3M1+KXw8AzRqSGMlxxh/Jnzekxi5s/kVTTcmtC++M20VSkjHwdazNlKCIkEa00m01EKiJcEZjIGhk4mBjRtPyOzoyVR5vAGDcjSvTqh9nG5Zr40sK14vHaPrwfm2Wyw9ibB3FlMM5rYU4elTRD4672gGJXtxknp4s3R7eR9uouEqw5n7mad3PiLKV27r9uQQtBSY2M8jZICyUOmxevaXk7RfPKhXsHtZ/sndrUTddMtAK4CKkWvgvKkNVsTpR5wmEJvqAytK69uUNbLKkCVZ9aCePD3LPiqZtFeMIZcjT8pY3KVWFxY1Mzjk6U8k8F9jufdl1FBrCmfjwEJw/lHydPYCgWmuJM7tunsJG9E2pnz1Q0H/+Fdvmh4TpGCps00dg=; PS=2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255; ACTIVE=1713611430; HOWTORT=ul=1713612167505&r=https%3A%2F%2Fwww.naukri.com%2Fpython-software-developer-jobs%3Fk%3Dpython%2520software%2520developer&hd=1713612167658; _ga_K2YBNZVRLL=GS1.1.1713611313.2.1.1713612167.38.0.0; __gads=ID=00f6162d85112d65:T=1713588897:RT=1713612169:S=ALNI_MbE5MXF9Wlwih0sl06_b-n-OilHwA; __gpi=UID=00000df36d7a04c7:T=1713588897:RT=1713612169:S=ALNI_MZK9srJneWdarsjUUAkHNy_SqsYPQ; __eoi=ID=76da1689c817e157:T=1713588897:RT=1713612169:S=AA-AfjaHpFQjHMC3I7LbCQkIOuaZ; bm_sv=04A3EA0B09B0E178882C03BE2EF39C49~YAAQxP7UF9oLc8+OAQAAwKE++xfb8fm5hbG1lVdZ+wrg2qeeFFNo3gQXXxmRwU7euHy3uc1Hzud8XOvN5ehSp3W/3E5ZoAUGeWVohrfT4Ewmn1ls0xYSJjxuIC9VIT77Tw4tGJfojOwViO4VAYaOhz5ey4Ddoahe502FXica3krsPUWbaPHbp77i+eUvVcDXtVXLR9D3fdubbNjGWERs9BWtRpGk0C/gsrlEA4Z0A8/0me3tjW2b484n31nuEm4FOQ==~1; J=0; PS=2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255; _t_ds=f37d9f01713611223-21f37d9f0-0f37d9f0; ak_bmsc=A71B6FB09DF0881D47CFF02B7A1CA7FD~000000000000000000000000000000~YAAQxP7UFzqZcs+OAQAAmPo6+xfBghd1CzbMDuYKcv1skx6yaAha3jA/8XmqVJWf4rWdVlpCfgo7xQ814chfXKr34rBiYdoh0zbmqcJbHKezNPmVbBoeaa8SgKX51592E+FdSjIEXG4PwMhQBax23B5EEY1egqe38Ahltz4Pq5Lvd4iQRhS0ez6ZkU8kniCTQ+h/CvqSkL9NPVqJNHAYj9RX5vFkhkP6gwsUOpRqqTZxyMKhrFiomNdmzSMoGvNrRPdpkjMJnQ6NtBxS0+rgKp1w8gDNouVVolzHXir/Gwz8uDkaH8hMZWVXh5skPA56SiFVsFvxumnl1UxBDiyBsufaaNuMfIi+XsAJCh5QqOAJxneKgQeb2ax+gA==; bm_sv=04A3EA0B09B0E178882C03BE2EF39C49~YAAQxP7UFzCJc8+OAQAAxpFC+xcJhardqJKI2AfMSbYfjhTdFix/Cyxn7zki0svsyWlaGU6QacP/aDB5aaG88BQ0tY7StxtknOw3YafsSBZ8QO7Iy+GE3mnroi19kEsWroY7MoFlsTVEZwumzCRwdMIWiHo8GG1A6HQKtPbfM3icfl6POEjxcpjins2MOYBy+G/N0VUwGgRQR4Jo1IsdT/3n+ZfRAoHS/SWCo3mKTqDUhFwnM63EsTxLAI9xdrdbAg==~1',
    'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
    'priority': 'u=1, i',
    'referer': 'https://www.naukri.com/python-software-developer-jobs-in-bangalore?k=python%20software%20developer&l=bangalore&experience=7&nignbevent_src=jobsearchDeskGNB',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'systemid': 'Naukri',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    response_data=json.loads(response.text)
    job_id_list=[]
    for data in response_data["jobDetails"]:
        job_id=data["jobId"]
        apply_jobs(job_id)
        job_id_list.append(job_id)
    
    return job_id_list


def recom_jobs():

    url = "https://www.naukri.com/jobapi/v2/search/recom-jobs"

    payload = json.dumps({
    "clusterId": None,
    "src": "recommClusterApi",
    "clusterSplitDate": {
        "apply": "2024-08-05 11:46:44",
        "preference": "1980-01-01 05:30:00",
        "profile": "1980-01-01 05:30:00",
        "similar_jobs": "2024-08-05 11:46:48"
    },
    "searches": [
        {
        "keywords": "tech support",
        "location": ""
        },
        {
        "keywords": "python software developer",
        "location": ""
        }
    ]
    })
    headers = {
    'authority': 'www.naukri.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'appid': '105',
    'cache-control': 'no-cache, no-store, must-revalidate',
    'content-type': 'application/json',
    'cookie': '_t_s=direct; _t_ds=3904aa11693479034-303904aa1-03904aa1; _t_us=18A655EFCD5; test=naukri.com; nauk_rt=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJkZXZpY2VUeXBlIjoiZDNza3QwcCIsInVkX3Jlc0lkIjoxMjA5MTQyMTMsInN1YiI6IjEyOTU2MTM5NSIsInVkX3VzZXJuYW1lIjoiaGltYW5zaHUubmluamE3QGdtYWlsLmNvbSIsInVkX2lzRW1haWwiOnRydWUsImlzcyI6IkluZm9FZGdlIEluZGlhIFB2dC4gTHRkLiIsInVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTYuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlwQWRyZXNzIjoiMTAuMjQzLjE3Ni42NCIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxMjk1NjEzOTUsInVzZXJTdGF0ZSI6IkFVVEhFTlRJQ0FURUQiLCJ1ZF9pc1BhaWRDbGllbnQiOmZhbHNlLCJ1ZF9lbWFpbFZlcmlmaWVkIjp0cnVlLCJ1c2VyVHlwZSI6ImpvYnNlZWtlciIsInNlc3Npb25TdGF0VGltZSI6IjIwMjMtMDgtMzFUMTY6MjA6NTciLCJ1ZF9lbWFpbCI6ImhpbWFuc2h1Lm5pbmphN0BnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MjUwMTUwNTcsInRva2VuVHlwZSI6InJlZnJlc2hUb2tlbiIsImlhdCI6MTY5MzQ3OTA1NywianRpIjoiMzAzYzJjZjU2NDEyNDc1M2E0NmQxNWEwYmZhYzEzY2MifQ.bXeC5CPyTm8FsqPo4dqSZsArtEgukQ1SKsjfSQ4wDHVbQuUPA0WK9DYOekKpjtRlE-HQRtGa6xkqQla10s7KC4m69PoAYQna1lB4xtvKpBqk9pgMQkegmAIBG8y_v4g7V5S1P1GzGFANJZtDfToTVFgcuTluHO_DBv2uPsHXiIWNEj0eU9sGD4yRRssKdDTfIrI0PQPa6fiRsf9lO86TvutOEcswsxF7xYX_2VLkaWcjBDxSW3r6NZ6-rAj0Kr21Zp4c6XG26FkwN8801b4Ef_PwhbJH6cYhhEpj3l4tJEYkgY_BKlH3qtvRDa_qBG1r4nVnwtxulGQV8RppBiSzvA; nauk_sid=303c2cf564124753a46d15a0bfac13cc; nauk_otl=303c2cf564124753a46d15a0bfac13cc; NKWAP=2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255~2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255~1~0; MYNAUKRI[UNID]=102fd0404742cdbc73; _cc_id=fd2492d71e451fae1ed43565ae1d63dd; PS=2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255; G_ENABLED_IDPS=google; __utmc=266160400; _t_ds=1eb666681695196895-251eb66668-01eb66668; PHPSESSID=g075ep83a4ht5f5d9qou24vgj2; cto_bundle=IYE-R181cU1kM29zcVZyZEExcUtrdXVYclJINWV1RHpmallaQXNCTVdsYTBPRlglMkJXa3NvWTFMN0hxdnRmSEdPbVg0SEY3SUwyNmFEcFZKeHpmUkNYUk5ONVRIdDEyWVVESW5qT0ZTMGtqNHM4b2lmTDd1UE1naEJKQkltVDIlMkZZQyUyQnlCbGhUdiUyQkV4dTNGbkszSEJ3byUyQmN4Qmh3JTNEJTNE; _abck=AACDCB01DDFE1EFCCCC46A0E479BDB35~0~YAAQXEYDF05bzLaKAQAAK7t4uwoPFOD+EbwAb2Ajcs4NIOkCNnMf1ZtaoB/0tjv90B2JT0EbwUNhW9qhem8bZA1HJ4HMZzEMFNoXp8nsD5454RUjG8qNt+cYf4lrEKggRTdJ/M2y82lxScRd7U3eOQK46RLH+2Qapcbr6cRId70RJSTLkJwoTbx3NRLnXet1iVqbriL1qukR74jmlY6vLUg/GT7Ptsx9Y5TpoTxbvTMJfZCG6xykpAmLpXI/r1yA3Gi2sngUy3gCmv5UVCq2HRSL1+Br5tQuu3MwGlgzkLWScD07fVJXcG6XNC+jpCBDrnJYL994NoZkDpj8rnzHfuLf8klicF62860IeUJL/MEZFvJQfjIrHhXR8Op3hbXUUcN6tipjJdG6EV02CzIM3A5QtHjq+J3D~-1~-1~-1; failLoginCount=0; _ga=GA1.1.1792950486.1693479038; __utmz=266160400.1715142163.32.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); J=0; nauk_ps=default; _gcl_au=1.1.1016949448.1715142169; bm_mi=D3ECB4A2E8E427211F83305755A33428~YAAQnf7UF/pDGUmPAQAAoHp6VhfBunmIKp91P9J8Z5pqzgVxPS+n2hdy9PXVlkPusl7nWiVaFt/6Q0PFRQS61J0unGEgEuFLaCYr2FBaHUI8MO3s0WbM4dkVBNPO2zBTo2q0mUoAqr6O0P/K01w43UCJmwYpmu4OSh8LYnDD1HoAGg8cmp4j11t6gniBY7GMngNa2SzR9sk0w51cn3wNmUU5GAYit9M3lKh/YIqTkbvFqg+2yXhbz63LtAWSGNyWcW6OBG3dKpWjnv6PrpiIEAye3fDwnHboNg5rhzLbe3xjD41MF5X3AuYpsPsBH9LjVWE1GtOBL2R2yVzhzg==~1; ak_bmsc=D53587D6F971E072EE4BE20D158F08AF~000000000000000000000000000000~YAAQnf7UFwtEGUmPAQAAl4J6VhcwlkN1SvmUr+Mgx1T4mSXmwMOHYRkvT1rTtZv7yWziHnC2VARRNxDY26Q8BxxxLheQvoQQod0tA2g5bjfsv5n2+mXeuNv7EUptpDM2SusGs7lbtV5GASvIiHmlp3mh1bvDmVL6mS+SbJQWt1JaYdRPYAf9djodxcWafxJW9mL7l2400o1QAbep3ATeFAkMEPLkj3/QX91q+oQfGWW/Oz2iSBqLAuU3syIXqeYV+oX/vyrnPVjrt/B1nwD6kWxx+eFH88dO4jevc+QZlj1LfmlR54ViMLEpJVMMCVDIclo4fp8vhKu1mKppfMrd07d5o1KA/V7ceoMBs5GynBoqRl0BxKdsK3+aM2hn0BHO4DzyEwQjtdshsH3Vl7zSg7UEg4Gz82SexMMhQJ8s60lY76DNCg/cJY/95R5KQrosj9nOzlpqqbFZgVcmLFakmRkx705tYgJPHDBvS1JSNHw2a2AEYh4g5/EtxEy1; PS=2b44fc7cc22605c8e28990168a4b59ba5ee641aa56500b2fc3f44683ac4836269a86cc384cde9c370d99ad6a3af22255; __gads=ID=7681b693da145931:T=1693917786:RT=1715144565:S=ALNI_MYGUFIytHRJu6efKGhQRm6Xjc4_BQ; __gpi=UID=00000c3c2c1c6eaa:T=1693917786:RT=1715144565:S=ALNI_Mb2aDiQYcwXRwrTGyPsqo3q_ltYxA; __eoi=ID=6833cab4d1039621:T=1715144565:RT=1715144565:S=AA-AfjZocepljJ1hqt4x681nCLKk; nauk_at=eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJkZXZpY2VUeXBlIjoiZDNza3QwcCIsInVkX3Jlc0lkIjoxMjA5MTQyMTMsInN1YiI6IjEyOTU2MTM5NSIsInVkX3VzZXJuYW1lIjoiaGltYW5zaHUubmluamE3QGdtYWlsLmNvbSIsInVkX2lzRW1haWwiOnRydWUsImlzcyI6IkluZm9FZGdlIEluZGlhIFB2dC4gTHRkLiIsInVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTYuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlwQWRyZXNzIjoiMTAuMjQzLjE3Ni42NCIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxMjk1NjEzOTUsInN1YlVzZXJUeXBlIjoiam9ic2Vla2VyIiwidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2VtYWlsVmVyaWZpZWQiOnRydWUsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVzZXJUeXBlIjoiam9ic2Vla2VyIiwic2Vzc2lvblN0YXRUaW1lIjoiMjAyMy0wOC0zMVQxNjoyMDo1NyIsInVkX2VtYWlsIjoiaGltYW5zaHUubmluamE3QGdtYWlsLmNvbSIsInVzZXJSb2xlIjoidXNlciIsImV4cCI6MTcxNTE1MDI1OSwidG9rZW5UeXBlIjoiYWNjZXNzVG9rZW4iLCJpYXQiOjE3MTUxNDY2NTksImp0aSI6IjMwM2MyY2Y1NjQxMjQ3NTNhNDZkMTVhMGJmYWMxM2NjIn0.Z1V_wvWx2w7zP7Jn85OGo9MPBnYXIaXyFQSbwI4C1Gy35bKox1t-_Mw8cUVEo8JIDa9D3c3OwBZNXbwJszXsffutazxj_1vIz8rvNEi_s2XdbV91FntmaRrVmxWwUnkL1oh7MsL9tEp60YIs96VnU9S1o0mr2sOtxoBhlN70nulnudp4HSA20aI2k5MX3vqgLzhkFTKjE3XhFFgs-IF7cnFizZQAOnOKTcjbajCxCaEIQYHJ34fM5w8KyvVj1fl3DDNwHQ8SLY61MK7sLUzl06OavmSruZOAXxEi6N67BYZcPscijsWHARnOiWKBGmdGmv0JdAgqyvD-wAASpFUmmg; is_login=1; __utma=266160400.1792950486.1693479038.1715142163.1715146660.33; __utmb=266160400.3.10.1715146660; ACTIVE=1715147596; HOWTORT=ul=1715149025311&r=https%3A%2F%2Fwww.naukri.com%2Fmnjuser%2Frecommendedjobs&hd=1715149025566; bm_sv=8E61FFA58EED28392C889E28A771779D~YAAQl/7UF5XmsDSPAQAAoznZVhd+1y7oNmk5Zk2EKYYbccKqeHTaG/JmDALH34Kw1m+xFhNZTWNPyUnb+a1GPXHRO5bW1wK6ZNxK3sgjd34X/sCOlbFruXfj47T4fNF1JUSCc6JX8PQA/2acNFQOhyP7nyreaVsXUZBlrx8qf5PuplcfieqBEjhd7LawkRHJUgPHASmPtdJcCvgHQ5HWrOUv5SUHEIxNDVKMNqDv3r3wyZn5LIZhW+7znMuEj34h0A==~1; _ga_K2YBNZVRLL=GS1.1.1715146663.38.1.1715149027.32.0.0; J=0; bm_sv=8E61FFA58EED28392C889E28A771779D~YAAQ3/7UFxCxqFCPAQAA6zPbVhct67OugFlZgNnZI5RUvs3bMffKNc500aIf8eQpimYrps4lfr9S57ktx//MEoHY+Qxb1IO/jgVnb4v/AalNDsz7EYpr3cCnk5nezeuM5HiM2QnWGwt0cgBWiLCk3q4StYVUByy+Krqu1uk8mu1v7qzog4QwA6ZX7iXz+NN60ZxG1eHo8xCSdV9mKT6rXZY/V30RU5Mee0Knnxtrabiw0XABLk1YbNYW4Qs1iFPhfw==~1',
    'expires': '0',
    'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
    'origin': 'https://www.naukri.com',
    'pragma': 'no-cache',
    'referer': 'https://www.naukri.com/mnjuser/recommendedjobs',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'systemid': 'Naukri',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_data=json.loads(response.text)
    job_id_list=[]
    for data in response_data["jobDetails"]:
        job_id=data["jobId"]
        apply_jobs(job_id)
        job_id_list.append(job_id)
    
    return job_id_list


while(True):
    # recom_jobs()
    get_job_list()
