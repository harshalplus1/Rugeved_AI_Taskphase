#%%
from matplotlib.ticker import FixedLocator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
bwood=pd.read_csv(r'/home/harshal/Downloads/bollywood-1.csv')
print(bwood)
print()
print()
print()
#1
print(bwood.shape[0])
print()
print()
print()
#2
print(bwood['ReleaseTime'].value_counts().sort_values())
print()
print()
print()
#3
print(bwood['Genre'].value_counts())
print()
print()
print()
#4
print(pd.crosstab(bwood.Genre,bwood.ReleaseTime))
print()
print()
print()
#5
bwood['Year']=pd.DatetimeIndex(bwood['Release Date']).year
print(bwood['Year'].value_counts().idxmax())
print()
print()
print()
#6
bwood['Month']=pd.DatetimeIndex(bwood['Release Date']).month
print(bwood[bwood.Budget>=30].Month.value_counts().idxmax())
print()
print()
print()
#7
bwood['ROI']=bwood['BoxOfficeCollection']-bwood['Budget']
print(bwood['MovieName'].iloc[bwood['ROI'].argmax()])
print()
print()
print()
#8
print(bwood.groupby("ReleaseTime").ROI.mean())
print()
print()
print()
#9
sns.regplot(x=bwood['BoxOfficeCollection'], y=bwood['YoutubeLikes'], data=bwood)
print(bwood['BoxOfficeCollection'].corr(bwood['YoutubeLikes']))
#10
sns.boxplot(x=bwood['Genre'], y=bwood['YoutubeViews'],data=bwood)
#11
sns.heatmap(bwood[['Budget','BoxOfficeCollection','YoutubeLikes','YoutubeDislikes','YoutubeViews']].corr(),annot=True)
#12
sns.boxplot(x=bwood['Genre'], y=bwood['BoxOfficeCollection'],data=bwood)
#13
plt.plot(bwood["Year"].value_counts())
print()
print()
print()
#14
bwood.plot.hist(column=["Budget"], by="Genre", figsize=(10, 25))
#15
plt.plot(bwood.groupby('Year').YoutubeLikes.sum())
plt.plot(bwood.groupby('Year').YoutubeDisLikes.sum())
# %%
