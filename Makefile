.PHONY: help all build validate

MD_FILES= $(wildcard pages/*.md)
HTML_FILES= $(patsubst pages/%.md, pages/%.html, $(MD_FILES))

help: ## Short description of the commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

all: validate build index.html

validate:
	@echo 'Validating datapackages...'
	@python main.py

build: $(HTML_FILES) ## Run livemark build inside pages folder

$(HTML_FILES): pages/%.html : pages/%.md index.html
	@echo 'Building pages/$*.html file from pages/$*.md...'
	@livemark build $< --target $@

index.html: index.md
	@echo 'Building index.html file from index.md...'
	@livemark build $< --target $@

start:
	@echo 'Starting livemark server...'
	@livemark start
