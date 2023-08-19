#import the library used to query a website
import urllib.request

# The following link has a gmail adress in the summary
# https://www.linkedin.com/recruiter/profile/45450475,u25o,CAP?searchController=smartSearch&searchId=2099076884&pos=421&total=3197&searchCacheKey=cacf26f6-4a06-463f-9243-286c9e09d36b%2CQMNw&searchRequestId=26d7a7a7-3afe-4993-b4c9-0b7c9a396e21%2C0jez&searchSessionId=2099076884&memberAuth=45450475%2Cu25o%2CCAP

# https://www.linkedin.com/recruiter/profile/116075591,BRaX,CAP?searchController=smartSearch&searchId=2099076884&pos=121&searchCacheKey=cacf26f6-4a06-463f-9243-286c9e09d36b%2CQMNw&searchRequestId=8d6b869c-78a7-4357-ba03-4f21db3979ec%2CT-j-&searchSessionId=2099076884&memberAuth=116075591%2CBRaX%2CCAP
# url = "https://www.linkedin.com/recruiter/profile/45450475,u25o,CAP?searchController=smartSearch&searchId=2099076884&pos=421&total=3197&searchCacheKey=cacf26f6-4a06-463f-9243-286c9e09d36b%2CQMNw&searchRequestId=26d7a7a7-3afe-4993-b4c9-0b7c9a396e21%2C0jez&searchSessionId=2099076884&memberAuth=45450475%2Cu25o%2CCAP"

url = "https://www.linkedin.com/recruiter/profile/17509918,aqyX,CAP?searchController=smartSearch&searchId=5778905923&pos=43&total=442&searchCacheKey=cec848df-14e8-47e3-bb2f-dd64d804d784%2CDC7_&searchRequestId=059d77a5-1b37-486b-a013-827c4256e24b%2CXsQs&searchSessionId=5778905923&memberAuth=17509918%2CaqyX%2CCAP"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(response, "lxml") 

print(soup.prettify())
#soup.find_all("code")
#print(soup.find_all)

#myA = soup.findAll('div')

#print(myA)

