# TCC_Dummy_GPS_API

```
docker build -t dummy_gps_image .
docker run --name dummy_gps_api -d -p 2947:2947 --network host dummy_gps_image
```
