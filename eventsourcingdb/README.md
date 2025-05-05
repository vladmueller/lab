# Readme


- [EventSourcingDB – because it's more than just data](https://www.thenativeweb.io/products/eventsourcingdb)
- [EventSourcingDB](https://docs.eventsourcingdb.io/)

```bash
docker run -it -p 3000:3000 thenativeweb/eventsourcingdb run --api-token=secret --data-directory-temporary --http-enabled --https-enabled=false --with-ui
```

NOTE: EventSourcingDB does not support configuration via environment variables.
All settings must be passed as command-line flags.
If you want to use environment variables (e.g., for secrets), inject them into the container and reference them explicitly in the args section.
