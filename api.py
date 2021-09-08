from fastapi import FastAPI
from geolocation import Address, GeoLoc, distance, polyzone, df2


app = FastAPI()

'''http://127.0.0.1:8000/API?area=shampura&zone=east%20zone&city=bangalore&country=india&
area1=govindapura&zone1=east%20zone&city1=bangalore&country1=india'''


@app.get("/API")
def read(area,zone,city,country,area1,zone1,city1,country1):
    loc1 = Address(area=area,zone=zone,city=city,country=country)
    loc2 = Address(area=area1,zone=zone1,city=city1,country=country1)
    geo = GeoLoc(loc1.coord().latitude, loc1.coord().longitude)
    geo2 = GeoLoc(loc2.coord().latitude, loc2.coord().longitude)
    points = [(geo.lat, geo.long), (geo2.lat, geo2.long)]
    polyzones = polyzone()
    print(polyzones)
    return {"points": points, "weather1": geo.weather(), "weather2": geo2.weather(),
            "distance": distance((geo.lat, geo.long), (geo2.lat, geo2.long)).kilometers,
            "Polygonal orange zones": polyzones[0], "Polygonal red zones": polyzones[1]}
