def buscar_artista(nombre):
    import requests, base64

    id_cliente = ---
    id_secreta = ---
    combi_creden = id_cliente + ":" + id_secreta
    credencial64 = base64.b64encode(combi_creden.encode()).decode()

    credencial = "Basic " + credencial64
    encabezados = {"Authorization": credencial}
    soli_token = {"grant_type": "client_credentials"}
    res_token = requests.post("https://accounts.spotify.com/api/token", headers=encabezados, data=soli_token)
    token = res_token.json()["access_token"]


    bearer = "Bearer " + token
    encabezados2 = {"Authorization": bearer}
    busqueda = {
        "q": nombre,
        "type": "artist",
        "limit": 1
    }

    res_busqueda = requests.get("https://api.spotify.com/v1/search", headers=encabezados2, params=busqueda)
    datos_artista = res_busqueda.json()["artists"]["items"][0]
    id_artista = datos_artista["id"]

    parametros = {"limit": 10}
    url = "https://api.spotify.com/v1/artists//" + id_artista + "/albums"
    respuesta = requests.get(url, headers=encabezados2, params=parametros)
    info_albumes = respuesta.json()
    albumes = []
    
    for album in info_albumes["items"]:
        
        datos_album = {
            "nombre": album['name'],
            "id":album['id'],
            "fecha": album['release_date'],
            "cant_pistas": album['total_tracks']
        }
        albumes.append(datos_album)

    parametros_dur = {"market": "MX"}
    discografia = []
    
    for alb in albumes:

        urlalb = "https://api.spotify.com/v1/albums/" + alb['id']
        res_dur = requests.get(urlalb, headers=encabezados2, params=parametros_dur)
        info_dur = res_dur.json()
        duracion = 0
        
        for pista in info_dur["tracks"]["items"]:
            
            duracion += pista["duration_ms"]
            
        alb["duracion"] = duracion
        discografia.append(alb)
        
    return discografia
