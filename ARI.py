def ari_emptychar(s):
     if len(s)==0:
         if bool(s)==False:
          return 0
def ari_alphanumeric(s):
     if not s.isalnum():
       return False
 
def ari_emptyword(s):
     if " " not in s:
          return None
