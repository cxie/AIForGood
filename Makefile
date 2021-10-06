default:
	pdflatex main
	bibtex main

run:
	go main.pdf

clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.pdf main.toc
