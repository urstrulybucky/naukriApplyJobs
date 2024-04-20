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
    'authorization': 'ACCESSTOKEN = eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTIwOTE0MjEzLCJzdWIiOiIxMjk1NjEzOTUiLCJ1ZF91c2VybmFtZSI6ImhpbWFuc2h1Lm5pbmphN0BnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlwQWRyZXNzIjoiMTAzLjYuMTU5Ljg3IiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjEyOTU2MTM5NSwic3ViVXNlclR5cGUiOiJqb2JzZWVrZXIiLCJ1c2VyU3RhdGUiOiJBVVRIRU5USUNBVEVEIiwidWRfZW1haWxWZXJpZmllZCI6dHJ1ZSwidWRfaXNQYWlkQ2xpZW50IjpmYWxzZSwidXNlclR5cGUiOiJqb2JzZWVrZXIiLCJzZXNzaW9uU3RhdFRpbWUiOiIyMDI0LTA0LTIwVDEwOjM4OjM1IiwidWRfZW1haWwiOiJoaW1hbnNodS5uaW5qYTdAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzEzNjE0OTEzLCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlhdCI6MTcxMzYxMTMxMywianRpIjoiYTQyMGU3MWQwZDhhNGZmMWI4ZmY5YzY4MDQ3OTg5ZTcifQ.hRu6ka2gxwMI-kpjnazVr2KTaR2TfwWfML8YXAmPDzeGZM3JeN0H-K4RSsO7vJ66bOuI1a0xLGEnFMb2bbwUrNZntxBbzrg_KID82fJIlptCV5RyIM0z8M1wM8VL4MGV0pbD20CndDbie_qpQiUsAejt3dGCsPyZOH5GT_1JRbTqQTZbzSwbBrwnnrWF3XUQzxJlwS3JSoqDeaxFVekWbs9QJFTYXAhhgC7CC-hiwvD2YJNA712XMQOYLSDrhwCstVSPx7mAmgMtTjME2At8YA5V5O-3vyCuUzXSxCz_d1jeKBDvx7zL2TMqdCQ7cLKCCQBIWKrtniNnZDYw0MBKeA',
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


    url = "https://www.naukri.com/jobapi/v3/search?noOfResults=100&urlType=search_by_key_loc&searchType=adv&location=bangalore&keyword=python%20software%20developer&sort=p&pageNo=1&experience=7&k=python%20software%20developer&l=bangalore&experience=7&nignbevent_src=jobsearchDeskGNB&seoKey=python-software-developer-jobs-in-bangalore&src=jobsearchDesk&latLong=&sid=17136121678974678"

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


get_job_list()
