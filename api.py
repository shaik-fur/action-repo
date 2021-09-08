from fastapi import FastAPI
from geolocation import Address, GeoLoc, distance, polyzones, df2


app = FastAPI()

'''http://127.0.0.1:8000/API?area=shampura&zone=east%20zone&city=bangalore&country=india&
area1=govindapura&zone1=east%20zone&city1=bangalore&country1=india'''


@app.post("/API")
def read(dest1, dest2):
    d1 = dest1.split(",")
    d2 = dest2.split(",")
    print(d1)
    print(d2)
    loc1 = Address(area=d1[0], city=d1[1], country=d1[2])
    loc2 = Address(area=d2[0], city=d2[1], country=d2[2])
    geo = GeoLoc(loc1.coord().latitude, loc1.coord().longitude)
    geo2 = GeoLoc(loc2.coord().latitude, loc2.coord().longitude)
    points = [(geo.lat, geo.long), (geo2.lat, geo2.long)]
    polyzone = polyzones()
    return {"points": points, "weather1": geo.weather(), "weather2": geo2.weather(),
            "distance": distance((geo.lat, geo.long), (geo2.lat, geo2.long)).kilometers,
            "Polygonal orange zones": polyzone[0], "Polygonal red zones": polyzone[1]}
