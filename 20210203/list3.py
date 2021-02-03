import pprint
H=10
W=10
data=[[0]*W]*H
#newは1回しか行われておらず、shallowコピーとなってしまう
pprint.pprint(data)
