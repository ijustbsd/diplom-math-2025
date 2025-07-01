THEME = О математическом моделировании процесса погружения сваи с дополнительными параметрами
STUDENT = С.Д. Бабошин
DEGREE = д. ф.-м. н., доцент
DIRECTOR = Д.В. Костин

SED = "s/{{theme}}/${THEME}/; s/{{student}}/${STUDENT}/; s/{{degree}}/${DEGREE}/; s/{{director}}/${DIRECTOR}/"

all:
	# титульный лист
	sed -e ${SED} titlepage.fodt > tp-output.fodt
	# libreoffice --headless --convert-to pdf tp-output.fodt
	/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf tp-output.fodt

	# .tex
	pdflatex diplom.tex
	biber diplom
	pdflatex diplom.tex
	pdflatex diplom.tex
	mv diplom.pdf Бабошин.pdf
	open Бабошин.pdf &

referat:
	# титульный лист
	sed -e ${SED} referat-titlepage.fodt > referat-tp-output.fodt
	# libreoffice --headless --convert-to pdf referat-tp-output.fodt
	/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf referat-tp-output.fodt

	# .tex
	pdflatex referat.tex
	biber referat
	pdflatex referat.tex
	pdflatex referat.tex
	mv referat.pdf Бабошин_реферат.pdf
	open Бабошин_реферат.pdf &

presentation:
	pdflatex presentation.tex
	pdflatex presentation.tex
	open presentation.pdf &

clean:
	rm -f *.aux *.log *.out *.toc *.pdf *.bbl *.bcf *.blg *.xml *.nav *.snm
	rm -f images/*.pdf
	rm -f tp-output.*
	rm -f referat-tp-output.*
