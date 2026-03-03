#The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.
wrongmean=38
numbers=40
wrongnumber=36
correctnumber=56
totalwrsum=wrongmean*numbers
totalrsum=totalwrsum-wrongnumber+correctnumber
correctmean=totalrsum/numbers
print("The correct total sum is ",totalrsum)
print("The correcte mean is ",correctmean)