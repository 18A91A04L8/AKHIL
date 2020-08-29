import matplotlib.pyplot as plt
product ='Mobile','Laptop','Desktop','ipad'
quantity =[45,30,20,5]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
plt.pie(quantity,labels = product,colors = colors,
        autopct = '%1.if %%',shadow = True,startangle = 140)
plt.show()
