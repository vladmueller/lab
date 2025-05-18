# Golang

Projects = Modules in Golang

**NOTE**: The identifier of the `module` has to be unique (globally).

```shell
go mod init github.com/vladmueller/golang-demo
```

This will generate a Go "project file": `go.mod`

---

Per default, everything is private in a package.
**Capitalization** is used to determine whether something is _private_ or _public_.

---

Packages ~ Directories

TIP: Use **short** and unique names for packages ;)

---

External dependencies have to be listed in the `go.mod` file.
We can do this automatically with:

```shell
go mod tidy
```

---

An HTTP Router in Go is called "Muxer" in reference to a multiplexer.
