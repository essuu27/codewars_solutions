def howgood(results, myscore):
    if myscore > (sum(results) / len(results)):
        return (True)
    return (False)


res1 = [3, 4, 8, 3, 6, 4, 7, 2, 6, 3]
score1 = 6

print(howgood(res1, score1))
