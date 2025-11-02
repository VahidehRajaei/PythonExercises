from DAL.UniInfoModel import *
import requests
#----------------------------------------------------------------------------------------------------------------

def get_Universities(url,parameter):

    try:
        response=requests.get(url,parameter)
        content=response.json()
        uniList=[]
        for university in content:
            country=university['country']
            universityname=university['name'] 
            alpha_code=university['alpha_two_code']
            state_province=university['state-province']
            domains=university['domains']
            web_pages=university['web_pages']
            info= UniversityInfo(country,universityname,alpha_code,state_province,domains,web_pages)
            uniList.append(info)
        return uniList
    except:
         print(f'Error is:{response}')
        
def get_University_Info():
    
    result=get_Universities('http://universities.hipolabs.com/search',{'country':'IRAN'}) 
    return result



    
   
       


        