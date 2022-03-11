def ari_emptychar(s):
     if len(s)==0:
          return 0
def ari_alphanumeric(s):
     if not s.isalnum():
       return False
 
def ari_emptyword(s):
     if " " not in s:
          return None
def ari_numword(s):
     acc=1
     for i in s:
          if i ==' ':
               acc+=1
     return acc

