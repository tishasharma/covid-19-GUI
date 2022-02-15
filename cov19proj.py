import covid
import matplotlib.pyplot as plt
cov=covid.Covid() #get data
name=input("enter country name")
virdat=cov.get_status_by_country_name(name)
print(virdat)
l=['id','country','confirmed','latitude','longitude','last_update']
for i in l:
    virdat.pop(i)
lab=virdat.keys()
slices=virdat.values()
plt.pie(slices,labels=lab,colors=['b','g','y'],explode=(0,0.1,0),autopct='%1.1f%%')
plt.title(name)
plt.legend()
plt.show()
