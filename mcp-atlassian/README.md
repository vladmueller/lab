# README

Port publishen und auf alle Interfaces binden:

```text
mcp-atlassian:
...
command: ["--transport","streamable-http","--port","9000","--host","0.0.0.0","-vv"]
ports:
- "9000:9000"
```

n8n-Endpoint, wenn nicht im selben Netzwerk bzw. derselben docker-compose-Datei:

Docker Desktop (Mac/Windows):
http://host.docker.internal:9000/mcp

Linux (Standard-Bridge):
http://172.17.0.1:9000/mcp (oder deine Host-IP)
