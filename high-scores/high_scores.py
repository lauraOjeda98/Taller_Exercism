def latest(scores):
    mini = min(scores)
    scores.remove(mini)

    return min(scores)


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    aux = scores
    maxi = []
    if len(scores) > 2:
        for i in range(3):
            maxi.append(max(aux))
            aux.remove(max(aux))
        return maxi
    else:
        return sorted(scores, reverse=True)
