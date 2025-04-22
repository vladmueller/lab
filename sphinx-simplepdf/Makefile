# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docker-build:
	docker build -t ghcr.io/vladmueller/sphinx-simplepdf:latest .

docker-push:
	docker push ghcr.io/vladmueller/sphinx-simplepdf:latest

docker-make-html:
	docker run -p 50006:50006 --rm -v $(shell echo $${PWD}):/workdir ghcr.io/vladmueller/sphinx-simplepdf:latest html

docker-make-pdf:
	docker run -p 50006:50006 --rm -v $(shell echo $${PWD}):/workdir ghcr.io/vladmueller/sphinx-simplepdf:latest simplepdf
