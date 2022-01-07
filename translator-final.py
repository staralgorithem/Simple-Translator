import translators
import os
os.system ('cls')
print('hey there! please write your source text:')
#fLanguage= From which language?
#tLanguage= to which language?
#sourceText= the text which you want to translate it!
fLanguage,tLanguage,sourceText =input("whats your text's language? : "
), input("What language do you want to translate into?"), input("please write your text: ")
bing=translators.bing(sourceText,from_language=fLanguage,to_language=tLanguage)
print(bing)