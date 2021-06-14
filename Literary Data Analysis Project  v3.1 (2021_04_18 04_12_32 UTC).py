import classics
import matplotlib.pyplot as plt

birth_year = classics.get('bibliography.author.birth','(None)','')

ancient_lit = []
medieval_lit = []
modern_lit = []

#Literary Period Grouping

#Ancient Literature
for i in (birth_year):
    if i < 1100:
        ancient_lit.append(i)

#Medieval Literature
for i in (birth_year):
    if i > 1100 and i < 1500:
        medieval_lit.append(i)

#Modern Lit
for i in (birth_year):
    if i > 1900:
        modern_lit.append(i)

#Flesch Kincaid Readability
readability = classics.get('metrics.difficulty.flesch reading ease','(None)','')

#Literary Period Scatterplots
#Ancient Literature Readability Scatter Plot
plt.scatter(ancient_lit, readability)
plt.title('Ancient Literature Readability Scores')
plt.xlabel('Years')
plt.ylabel('Readability Score')
plt.show()

#Medival Literature Readbility Scatter Plot
plt.scatter(medieval_lit, readability)
plt.title('Medieval Literature Readability Scores')
plt.xlabel('Years')
plt.ylabel('Readability Score')
plt.show()

#Modern Literature Readability Plot
plt.scatter(modern_lit, readability)
plt.title('Modern Literature Readability Scores')
plt.xlabel('Years')
plt.ylabel('Readability Score')
plt.show()


#Average Readability All Literary Periods
def mean(readability): 
    return sum(readability)/ len(readability)
mean_readability = mean(readability)
print(mean_readability)