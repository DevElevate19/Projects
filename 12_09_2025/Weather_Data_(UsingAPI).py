import requests
while True:
    try:
        api_key=input("Enter your api-key: ")
        Co_ordniates=input("Enter your Co-ordinates: (Put 'exit' to stop program)")
        if Co_ordniates.lower()=="exit":
            break
        rom_date=input("Enter the date from which u want to view weather date (YYYY-MM-DD): ")
        to_date=input("Enter the date till which u want to view weather date (YYYY-MM-DD): ")   
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{Co_ordniates}/{rom_date}/{to_date}?key={api_key.upper()}"
        weather=requests.get(url)
        data=weather.json()
        print('alerts',data['alerts'])
    except:
        print("Put valid credentials")
# print(type(data['days']),(data['days'])[0])
    while True:
        thing_u_wanna_know=input("Enter thing you want to know (If you dont know anything put 'tell'(will tell all things) and for exit put 'exit'):")
        if thing_u_wanna_know.lower()=="exit":
            break
        elif thing_u_wanna_know.lower()=="tell":
            for j,k in (data).items():
                print(j,'=',k)
        elif thing_u_wanna_know.lower() in data['days'][0]:
            print(thing_u_wanna_know.lower(),'=',((data['days'])[0])[thing_u_wanna_know.lower()])
        else:
            print("thing u asked doesnt exits in database")
