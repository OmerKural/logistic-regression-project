# logistic-regression-project
Coded in Python by Ömer Kural

## The Making of The Project
Before starting to coded the actual project I had to analyse the `advertising.csv` data with the `seaborn` library.

First I plotted numerical data against eachother with a pair plot. I also added a hue defined by the "Clicked on Ad" column feature. This made me see the corrolation in the data more clearly.

```py
import seaborn as sb
sb.pairplot(data=ad_data, hue="Clicked on Ad")```
![pairplot](./Images/output1.png)

