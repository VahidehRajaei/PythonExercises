import string
import operator

str1 = """
Today, Richard Rael and Tony Riggs tell the story of American astronomer edwin hubble .
He changed our ideas about the universe and how it developed.

Edwin hubble made his most important discoveries in the nineteen twenties. Today, other
astronomers continue the work he began. Many of them are using the Hubble space
telescope that is named after him.

Edwin Hubble was born in eighteen eighty-nine in Marshfield, Missouri. He spent his early
years in the state of Kentucky. Then he moved with his family to Chicago, Illinois. He
attended the University of Chicago. He studied mathematics and astronomy.
"""
#-----------------------------------------------Highlight-----------------------------------------------------------
def markWord(func):
    def inner(*args):
        return "<mark>"+func(args)+"</mark>"
    return inner

@markWord
def highlightWord(*args):
    for item in args:
        str = ' '.join(item)
    return str

def scan(str):
    target = ['Edwin','edwin']
    words = str.split()
    itWords=iter(words)
    tupleResult=( highlightWord(word,next(itWords)) if  word in target else word for word in itWords)
    listResult=list(tupleResult)
    temp=[]
    for t in listResult:
        if(type(t)==tuple):
            temp.append(t[0])
            temp.append(t[1]) 
        else:
             temp.append(t)

    finalStr=' '.join(temp)
    return finalStr
#-----------------------------------------------Sample-----------------------------------------------------------
#Show Result In Webpage:

f1=open("Highlightpage.html","w")
f1.write(scan(str1))
f1.close()
#-----------------------------------------------CapWord-----------------------------------------------------------

def mainFun1(func):
    def changWord(str):
            if operator.contains(str,'edwin hubble'):
                newWord=string.capwords('edwin hubble')
                newStr=str.replace('edwin hubble',newWord)
            func(newStr)    
    return changWord

def mainFun2(func):
    def changWord(str):
            if operator.contains(str,'Edwin hubble'):
                newWord=string.capwords('Edwin hubble')
                newStr=str.replace('Edwin hubble',newWord)
            func(newStr)    
    return changWord

@mainFun2
@mainFun1
def capWord(str):
    print(str) 
#------------------------------------------------Sample----------------------------------------------------------------    
capWord(str1)
