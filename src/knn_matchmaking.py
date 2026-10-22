
from sklearn.neighbors import NearestNeighbors
import numpy as np


def encontrar_ong_mais_proxima(latitude_doador, longitude_doador, ongs):
    coordenadas_ongs = np.array([
        [ong["latitude"], ong["longitude"]]
        for ong in ongs
    ])

    coordenada_doador = np.array([
        [latitude_doador, longitude_doador]
    ])

    modelo = NearestNeighbors(n_neighbors=1)
    modelo.fit(coordenadas_ongs)

    distancia, indice = modelo.kneighbors(coordenada_doador)

    ong_escolhida = ongs[indice[0][0]]

    distancia_km = distancia[0][0] * 111

    return ong_escolhida, distancia_km


if __name__ == "__main__":
    ongs = [
        {
            "nome": "ONG Prato Quente",
            "latitude": -23.612,
            "longitude": -46.781
        },
        {
            "nome": "Abrigo Esperanca",
            "latitude": -23.625,
            "longitude": -46.795
        }
    ]

    ong, distancia = encontrar_ong_mais_proxima(
        -23.615, -46.785, ongs
    )

    print("ONG escolhida:", ong["nome"])
    print(f"Distância aproximada: {distancia:.2f} km")