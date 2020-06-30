import time as dt
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_excel(r'Path to the File')
print("The DataSet To be Sorted using SELECTION SORT")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df)
print("---------------------------------------------")
n=input("Enter the Attribute Name that needs to be Sorted :")
s = list(df.loc[:,n])
print("----------------------------------------------")
def sel_sort(s):
	s2=s.copy()
	s1=s.copy()
	l=len(s)
	for i in range(0,int(l/2)):
		mi=s.index(min(s[i:l]))
		s[i],s[mi]=swap(s[i],s[mi])
	return(s2,s)

def swap(a,b):
	temp=a
	a=b
	b=temp
	return(a,b)
def multiple_sort(s1,s,q,l):
	l3=[]
	l2=[]
	flag=False
	if (len(s)==0 or len(s1)==0):
		flag=True
		return(s1,len(l3),len(l2),flag)
	else:
		mi=s.index(min(s1))
		for i in range(len(s)):
			if (s[i]==s[mi]):
				l3.append(i)
		j=q
		for i in range(len(l3)):
			s[l3[i]],s[j]=swap(s[l3[i]],s[j])
			j=j+1
		k=0
		ma=s.index(max(s1))
		for i in range(len(s)-1,-1,-1):
			if (s[i]==s[ma]):
				l2.append(i)		
		for i in range(len(l2)):
			s[l2[i]],s[l-k-1]=swap(s[l2[i]],s[l-k-1])
			k=k+1
		return(s,len(l3),len(l2),flag)
def sort(s):
	s2=s.copy()
	s1=s.copy()
	x=len(set(s))
	l=len(s)
	if((l-x)==0):
		l1=[]
		l5=[]
		for i in range(0,int(l/2)):
			mi=s.index(min(s[i:l]))
			ma=s.index(max(s[i:l]))
			s[i],s[mi]=swap(s[i],s[mi])
			s[l-1],s[ma]=swap(s[l-1],s[ma])
			l=l-1
		return(s2,s)
	else:
		q=0
		while(len(s1)!=0):
			s1=s[q:l]
			s,l33,l22,flag=multiple_sort(s1,s,q,l)
			if(flag==False):
				q=q+l33
				l=l-l22
				s3=s
			else:
				break
		return(s2,s3)
# Main Program
s1,s=sort(s)
l=[]
d={}
for i in range(len(s1)):
	d[i]=0
for i in range(0,len(s1)):
	for j in range(0,len(s1)):
		if (s[i]==s1[j]):
			if (d[j]=='visited'):
				continue
			else:
				d[j]='visited'
				l.append(list(df.iloc[j,:]))
sam=pd.DataFrame(l)
print("The DataSet After Sorting using SELECTION SORT")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(sam)
# Time Comparision
ele_sort = [] 
time_sort = [] 
time_sel_sort = [] 
l=[[1,2,3,4],[1,1,1,2,45,6,8],[1,23,456,1,2,2,2,3,4,7]]
for i in l: 
    start =  dt.clock()
    s1,s=sort(i) 
    end =  dt.clock()
    print("the strat and the stop",start,end)
    start1 = dt.clock()
    s1,s=sel_sort(i)
    end1 = dt.clock()
    ele_sort.append(len(i)) 
    time_sort.append(end-start)
    time_sel_sort.append(end1-start1) 
print("The number of elements in every iter",ele_sort)
print("The times for our sort",time_sort)
print("The times for sel sort",time_sel_sort)
plt.xlabel('Execution Time For the Reformed Approach') 
plt.ylabel('Execution Time For the Existing Selection Sort') 
plt.plot(time_sort, time_sel_sort) 
plt.grid() 
plt.show() 


