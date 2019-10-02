import Algorithmia


def fashionA(path):


    input = {
    "image": "path",
    "model": "small",
    "tags_only": True}
    client = Algorithmia.client('simBELmBzPwtLZeK/XxdN/fd9dz1')
    algo = client.algo('algorithmiahq/DeepFashion/1.3.0')
    algo.set_options(timeout=300)  # optional
    print(algo.pipe(input).result)
