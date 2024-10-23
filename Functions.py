import numpy as np
"""
cosine_Similarity()

Calulates the similarity between two vectors,
returns cos similiarity -> i.e: 0.766

@param user_vector, data_vector

Note: only accepted input is a 1D vector, make this 2D if needed
"""
def cosine_Similarity(user_vector, data_vector):
    top = np.dot(user_vector, data_vector)
    bot = sqrt_square_vector(user_vector) * sqrt_square_vector(data_vector)
    cos = top/bot
    return cos

"""
sqrt_square_vector()

Used in the cosine_Similarity function for the bottom half of the equation
(||A|| x ||B||)

@param vector -> [0, 1, 1, 0]
"""
def sqrt_square_vector(vector):
    added_vector = 0
    for i in range(len(vector)):
        added_vector += vector[i]**2

    new_vector = np.sqrt(added_vector)
    return new_vector