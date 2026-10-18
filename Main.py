from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json 
# print("Program Started")
load_dotenv()
# print("load_dotenv")
api_key= os.getenv("GEMINI_API_KEY")
print(api_key)

client= genai.Client(api_key=api_key)
print(client)
# for model in client.models.list():
#           print(model.name)
saved_conversation=[]
conversation=[]
with open("Conversation","r") as file: 
     saved_conversation= json.load(file)
for content in saved_conversation:
     conversation.append(
          types.Content(
               role= content["role"],
               parts=[types.Part(text=content["text"])]
          )
     )


   
while True:
     message= input("you:")
     if message.lower().strip()=='quit':
          break
     elif message.strip()=="":
          print("please ask your question")
     else:
          
          conversation.append(
          types.Content(
          role="user",
          parts=[
          types.Part(text=message)
          ]))
          response= client.models.generate_content(
          model="gemini-3.1-flash-lite",
          contents=conversation)
          conversation.append(types.Content(role="model",parts=[
          types.Part(text=response.text)]
          ))
       
     print(response.text)     
          
for content in conversation:
     saved_conversation.append({
      "role": content.role,
      "text": content.parts[0].text
     })

with open("Conversation","w") as file:   # for saving the conversation into the computer here W means write and first string is name of the folder  
     json.dump(saved_conversation,file,indent=4)    # json.dumb is a attribute for dumbing the saved conversation data into file name are conversation 
                                                    # indent =4 for giving indentation    


print(conversation)

     
    

#print(response)   # give all the package or all the inforamtion like metadata , token left , other inforamtion which is not usefull the user      
   # give only Ai answer 
print(response.usage_metadata)
