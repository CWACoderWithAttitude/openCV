# OpenCV Stuff

* [tesseract finetuning](https://www.statworx.com/content-hub/blog/finetuning-von-tesseract-ocr-fuer-deutsche-rechnungen)
* [non english languages](https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/)
Additional [Training data](https://github.com/tesseract-ocr/tessdata) had to be moved to `/opt/homebrew/share/tessdata` (on OS X). Your path may vary if you use a different OS.

> Hint: Just specify the language to recognize like this `pytesseract.image_to_string(image, lang='deu')` and check the path in the error message. Tesseract will tell you where it expects to find the training data for your language.



