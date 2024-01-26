from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    latitude = -22.928272
    longitude = -43.346624
    timestamp = time.time()

    report = {
        'lat': latitude,
        'lon': longitude,
        'time': timestamp
    }
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2947)
