# Return the "survivor" of a Josephus permutation with 'n' participants,
# skipping 'k' participants between each 'victim'

def josephus_survivor(n,k):
    joes = [*range(1,n+1)]
    n1 = n
    indx = 0
    
    while(n1!=1):
        indx = (indx+k-1)%n1
        joes.pop(indx)
        n1-=1
        
    indx = indx%n1
    return(joes[indx])
