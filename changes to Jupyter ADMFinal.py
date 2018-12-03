
### Background code for running decay DDM and generating dataframes
'''
accuracy = df.choice.mean()
corRT = df[df.choice==1].rt.mean()

stdDev = np.std(df[df.choice==1].rt)


print("RT (cor) = {:.0f} ms".format(corRT/dt))
print("Accuracy = {:.0f}%".format(accuracy*100))
print('stdDev = {:.0f} ms'.format(stdDev/dt))

'''

# chi square calculation 


     
observed1 = [0.2, 0.3, 0.4, 0.5, 0.6]
expected1 = [0.12, 0.26, 0.43, 0.51, 0.62]

  
def calculateChiSquare(observed, expected): 
    #each bucket contains the counts of RTs in that interval  
    #can I calculate chiSquare from the %s?
    ChiSquare = 0
    for i in range(len(observed)):
         #calc chi square.
         ChiSquare += (observed[i] - expected[i])**2/expected[i]
    return ChiSquare

print(calculateChiSquare(observed1, expected1))
print(calculateChiSquare([4,13,7], [8, 8, 8]))

import scipy, scipy.stats

observed_values=scipy.array([18,21,16,7,15])
expected_values=scipy.array([22,19,44,8,16])


stat, pvalue = scipy.stats.chisquare(observed_values, f_exp=expected_values)
print(stat)
print(pvalue)




## bucketer 

def isInBounds(lower, upper, value):
    return lower <= value and value <= upper

def getBuckets(bounds, dataframe):
    bucketDict = dict() # dictionary mapping bucket number to counts in the bucket
    bounds.sort()
    boundsList = [] # [(lower1, upper1), (lower2, upper2) ...]
    for i,bound in enumerate(bounds):
        if i == 0:
            boundsList.append((0, bound))
            bucketDict[i] = 0
        else:
            boundsList.append((bounds[i-1], bound))
            bucketDict[i] = 0 
        #add right tail end bucket
        if i == len(bounds) - 1:
            boundsList.append((bound, 100)) #100 is a catchAll 
            bucketDict[i + 1] = 0
            
    #print(dataframe.shape)
    for i,(lower, upper) in enumerate(boundsList):
        for rt in dataframe.rt.values:
            if isInBounds(lower, upper, rt):
                bucketDict[i] += 1
    return bucketDict

obsvMean,obsvDev,obsvBuck = stats(dataAll)

simBucketCount = getBuckets(testB, df)
obsvBucketCount = getBuckets(obsvBuck, dataAll)

print("simulated buckets: \n", simBucketCount)
print("experimental buckets: \n", obsvBucketCount)






