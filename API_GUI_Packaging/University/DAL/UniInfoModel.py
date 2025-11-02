import sys
sys.path.insert(0,'D:/PythonClass/University')

#------------------------------------------------------------------------------------------------------------
class UniversityInfo:

    def __init__(self,country,universityname,alpha_code,state_province,domains,web_pages):
        self.country=country
        self.universityname=universityname
        self.alpha_code=alpha_code
        self.state_province=state_province
        self.domains=domains
        self.web_pages=web_pages

    def __str__(self):
        return (f'Country:{self.country}\tUniversityname:{self.universityname}\tAlphaCode:{self.alpha_code}\tStateProvince:{self.state_province}\tDomains:{self.domains}\tWeb_pages:{self.web_pages}')
        