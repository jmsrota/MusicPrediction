import numpy as np
"""
cosine_Similarity()

Calulates the similarity between two vectors,
returns cos similiarity -> i.e: 0.766

@param user_vector, data_vector

Note: only accepted input is a 1D vector, make this 2D if needed
This is not used yet, built-in is more efficient
"""
def cosine_Similarity(user_vector, data_vector):
    similarities =[]

    user_vector = user_vector.toarray().flatten()

    for i in range(data_vector.shape[0]):
        top = np.dot(user_vector, data_vector[i].toarray().flatten())

        bot = sqrt_square_vector(user_vector) * sqrt_square_vector(data_vector[i].toarray().flatten())

        cos = top/bot

        similarities.append(cos)

    return np.array(similarities)

"""
sqrt_square_vector()

Used in the cosine_Similarity function for the bottom half of the equation
(||A|| x ||B||)

@param vector -> [0, 1, 1, 0]
"""
def sqrt_square_vector(vector):
   np.sqrt(np.sum(vector**2))