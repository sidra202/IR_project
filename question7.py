from sklearn.metrics.pairwise import cosine_similarity


def cos_sim(X,Y):

    cosine_sim = cosine_similarity(X,Y)
    sim_scores = list(enumerate(cosine_sim))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:10]
    return sim_scores




