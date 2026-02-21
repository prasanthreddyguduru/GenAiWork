import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
#initializing the model //model could be diffrent
#like gemini flash,gemini pro ..etc 
#Temparature value is accurate result to display or enhancement

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature=0.7) 
 
#print(google_api_key = os.getenv("GOOGLE_API_KEY"))
#buildinhg message content
messages=[{"role" : "system", "content":"hey ur a supportive assistant"},
         {"role" : "user" ,"content":"Give me where ai evoultion started and how ..?"} ]
response=llm.invoke(messages)

print(response.content)