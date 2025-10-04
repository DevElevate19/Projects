from google import genai
from openai import OpenAI

#gemini_api_key=AIzaSyB1n3DYMAdpH7SHEiKAtgP9J3LJIlE_5Bo
#openrouter=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

#Dint find feasible because we need to handle 2 models with different kind of errors
'''#Creating a decorator to handle api key error instead of using the try-except again for each model
def apierror_tokenerror(fx):
    def wrapper(args):
        try:
            f_x=fx(args)
            return f_x
        except:
            print("Error")
    return wrapper'''



#Writing all models to send request and access them
class Ai_models:
    def __init__(self,api_kee,query):
        #Using kee for now getting confused with pointers set for api models
        self.api_kee=api_kee

        self.query=query
    #@apierror_tokenerror
    def gemini(self):
        try:
            #Making request to access gemini and decoding the api key stored at ascii char to keep it protected
            client = genai.Client(api_key=self.api_kee)
    
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=self.query,

            )


            #Returning instead of printing so that when no query is passed we could check auth credentials atleast
            print(f'Gemini:{response.text}\n')
        except Exception as e:

            try:
                if 401 in e:
                    print("Invalid Api Key")

                #This model isnt free so we need to take care of tokens as well
                elif 429 in e:
                    print("Tokens Exhausted")
            
            
            #Since the error raised when not connected to is not iterable so we can use try-except again to classify all possible errors
            except:
                print("Connect to Intenet")

            

    #@apierror_tokenerror
    def openrouter(self,i):
        try:
            models=[["x-ai/grok-4-fast:free",'Grok'],['deepseek/deepseek-chat-v3.1:free','Deepseek'],['qwen/qwen3-235b-a22b:free','Qwen']]
            client = OpenAI(
              base_url="https://openrouter.ai/api/v1",
              api_key=self.api_kee,
            )

            completion = client.chat.completions.create(
              model=models[i][0],
              messages=[
                {
                    'role':'user',
                    "content": self.query
                }
              ]
            )

            response_content = completion.choices[0].message.content
            
            # Filter out thinking content for Qwen model
            if i==2:  # Qwen model
                
                #Checking if qwen thought or not else would raise an error
                if '<think>' in response_content and '</think>' in response_content:
                    
                    
                    # Extract content after </think>
                    response_content = response_content.split('</think>')[-1].strip()
            
            
            
            print(f'{models[i][1]}:{response_content}\n')

        except Exception as e:

            try:
            #Since these models are opensource hence we dont need to tackle token exhaustion
                if 401 in e:
                    print("Invalid Api Key")

            except:
                print('Connect to Internet')
            

#-------------------------------------------------------------------------------------------------



print("="*60)
print("            TERMIBOT - AI CHAT INTERFACE ")
print("="*60)
print("Commands: /help | /list | /quit | /change <model>")
print("-"*60)



#Outer loop to ensure the input match with existing model present in the program
while True:

    #Selection of AI model to be used to get answers
    model=input("Choose AI model: ")

    print('\n'+'-'*60)

    #Using match-case because we dont need want access model.lower() again and again
    match model.lower():
        case 'gemini':
            val=None
            break
        case 'grok':
            val=0
            break
        case 'deepseek':
            val=1
            break
        case 'qwen':
            val=2
            break
        case '/list':
            print('\n1. Gemini, 2. Grok, 3. Deepseek, 4. Qwen')
        case _:
            print("\nEnter model from available model list accessible from /list")


answer=input("Enable model switching (yes/no): ")



if answer.lower()=='yes':

    #Taking Api key from user to access AI model online and encoding it to ascii to make it secured
    api_kee1=input("Gemini API key: ")
    api_kee2=input("Other Bots API key: ")
    k=1

else:
    api_kee=input(f"{model.title()} API key: ")
    k=2





#print(api_kee)



print("\n\nEnter the text from now:")



while True:


    query=input()
    


    
    
    #Printing users query separately for better CLI
    print(f"You:{query}")
    
    

    if k==2:
    
        #Calling AI_models class with all args to access specific models based on users input
        ai_model=Ai_models(api_kee,query)
    

    else:
        
        #Assigning access as per the model chose by user
        if val==None:
            ai_model=Ai_models(api_kee1,query)
        else:
            ai_model=Ai_models(api_kee2,query)



    #Breaking loop if users want to quit
    if query=='/quit':
        print("User left the chat")
        break
    
    
    #Based on user's input putting all commands available during live chat
    elif query=='/help':
        if k==1:
            print('1. /list - print all available ai models\n2. /change <AI_Model_Name> - change the model at any time\n3. /quit - exit the chat')
        else:
            print('1. /list - print all available ai models\n2. /quit - exit the chat')


    #Matching query to know if users want to change model or not
    elif query.lower().startswith('/change') and k==1:
        match query.lower():
            case '/change gemini':
                val=None
                print("Switched to Gemini")
            case '/change grok':
                val=0
                print("Switched to Grok")
            case '/change deepseek':
                val=1
                print("Switched to Deepseek")
            case '/change qwen':
                val=2
                print("Switched to Qwen")
            case _:
                print("Write Available Ai model to which u want to change to")
    

    #Not allowing user to change model if the user havent enabled multi model mode at beginning
    elif query.lower().startswith('/change') and k==2:
        print("Model switching is only available in multi-model mode")

    
    
    
    #Making sure users want to start chatting or want to start from accessing available commands
    #So added if just before accessing ai models
    elif query=='/list':
        print('\n1. Gemini\n2. Grok\n3. Deepseek\n4. Qwen')
    
    
    #Using Earlier values assigned to val to use model based on the input
    elif val==None:
        ai_model.gemini()
    elif val is not None:
        ai_model.openrouter(val)


    


