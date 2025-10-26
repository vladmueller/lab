# Readme

* [OpenCQRS](https://docs.opencqrs.com/)
* [Spring Boot](https://spring.io/projects/spring-boot)
* [EventSourcingDB](https://docs.eventsourcingdb.io/)

## Start EventSourcingDB

```shell
docker run --rm -it \
    --publish 3000:3000 \
    docker.io/thenativeweb/eventsourcingdb:1.1.0 run \
    --api-token secret \
    --data-directory-temporary \
    --http-enabled=true \
    --https-enabled=false
```

## Start application

```shell
./mvnw spring-boot:run
```
