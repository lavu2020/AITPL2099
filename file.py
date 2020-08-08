import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.bar([1,2,3],[3,4,5])
ax2.bar([1,2,3],[3,4,5])
plt.show()
