# Readme

* [OpenCQRS](https://docs.opencqrs.com/)
* [Spring Boot](https://spring.io/projects/spring-boot)
* [EventSourcingDB](https://docs.eventsourcingdb.io/)

## Start EventSourcingDB

```shell
docker run --rm -it --publish 3000:3000 docker.io/thenativeweb/eventsourcingdb:1.1.0 run --api-token secret --data-directory-temporary --http-enabled=true --https-enabled=false --with-ui
```

## Start application

```shell
./mvnw spring-boot:run
```

## Create a Docker image

```shell
./mvnw spring-boot:build-image
```

### Start Container

```shell
docker run --rm -p 8080:8080 -e ESDB_SERVER_URI="http://host.docker.internal:3000" opencqrs:0.0.1-SNAPSHOT
```
