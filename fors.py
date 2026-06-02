import copy
def process(a:int):
    print(a)
def fors(procs,frommm,intos,steeps):

    
    
    while frommm < intos:
        procs(frommm)
        frommm=frommm+steeps
_restarts={'frommm':0 ,'intos':10 , 'steeps':1 }

fors(process,**_restarts)