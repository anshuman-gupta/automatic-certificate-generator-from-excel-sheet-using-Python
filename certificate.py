from docxtpl import DocxTemplate
import pandas as pd
j=0
ans=pd.read_csv('data.csv')
n=(len(ans))
def mkw(n):
    tpl=DocxTemplate("temp.docx")
    context={i+1:{"name":ans['name'][i],"designation":ans['designation'][i],"start_date":ans['start_date'][i],"end_date":ans['end_date'][i]}for i in range (n)}
    tpl.render(context[n])
    tpl.save("%s - "%str(n)+ans['name'][j]+".docx")
for i in range(1,n+1):
    mkw(i)
    j+=1