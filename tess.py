import cv2, os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract
import argparse
import gtts
from playsound import playsound
import pyttsx3
# import module
from pdf2image import convert_from_path
import sys, traceback

class Tess:

    def __init__(self):
        self.a='a'
        self.jpg_file="/Users/volker/Pictures/misc/cost_of_retaining_employees.jpg"
        self.pdf_file="/Users/volker/dev/volker/openCV/input/faktencheck-vom-2-november-2021-100.pdf"
        self.file = self.pdf_file
        self.file = self.jpg_file
        self.temp_filename= "{}_tmp.png".format(os.getpid())

# https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-linux/
# https://theailearner.com/2018/10/23/understanding-images-with-opencv-python/



    #print(f"Image: ${img.item}")
    # https://pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/
    def do_tesseract(self):
        img=cv2.imread(self.file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cv2.imwrite(self.temp_filename, img_gray)
        
        text = pytesseract.image_to_string(Image.open(self.temp_filename))
        os.remove(self.temp_filename)
        print(text)
        # show the output images
        #cv2.imshow("Image", img)
        #cv2.imshow("Output", img_gray)
        #cv2.waitKey(0)
        #text="volker"
        self.speak(text)
    
    def do_tesseract_image(self, image_file):
        print(f"do_tesseract_image: ${image_file}")
        img=cv2.imread(image_file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cv2.imwrite(self.temp_filename, img_gray)
        print(pytesseract.get_languages())
        text = pytesseract.image_to_string(Image.open(self.temp_filename), lang='deu')
        os.remove(self.temp_filename)
        #print(text)
        # show the output images
        #cv2.imshow("Image", img)
        #cv2.imshow("Output", img_gray)
        #cv2.waitKey(0)
        #text="volker"
        print(f"do_tesseract_image: speaking...")
        #self.speak(text)
        return text
        print(f"do_tesseract_image: said enough...")


    # https://www.thepythoncode.com/article/convert-text-to-speech-in-python
    def speak_gtts(self, text):
        print(f"---\nsspeak_gtts: ${text}")

        for lang in gtts.lang.tts_langs():
            print(f"---\ni speak:  ${lang}")

        print(f"---\nspeaking: {text}")
        tts = gtts.gTTS(text)

    # https://stackoverflow.com/questions/65977155/change-pyttsx3-language
    def list_ttsx3_voices(self, engine):
        pass
        # for get property to work we needed to apply
        # https://github.com/nateshmbhat/pyttsx3/issues/248
        voices = engine.getProperty('voices')
        for voice in voices:
            if "german" in voice.name.lower():
                #print(f"list_ttsx3_voices: voice ${voice}")
                print(voice.id)

    def speak_pyttsx3(self, text):
        print(f"---\nspeak_pyttsx3: ...")
        engine = pyttsx3.init()
        print(f"---\nspeak_pyttsx3: engine: ${engine}...")
        try:
            self.list_ttsx3_voices(engine)
        except Exception:
            print(">"*60)
            traceback.print_exc(file=sys.stderr)
            print("<"*60)
        engine.setProperty("rate", 90)
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Eddy")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Grandma")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Flo")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Flo")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Flo")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Flo")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Flo")
        engine.setProperty("voice", "com.apple.eloquence.de-DE.Grandpa")
        
        try:
            engine.say(text)
            engine.runAndWait()
        except KeyboardInterrupt:
            print('bail out..')

        #print(f"---\nspeaking: ${text}")
        #tts = gtts.gTTS(text)
    def speak(self, text):
        print(f"---\nspeaking: {text}")
        #self.speak_gtts(text)
        self.speak_pyttsx3(text)

    # https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/
    def read_pdf(self):
        # Store Pdf with convert_from_path function
        images = convert_from_path(self.pdf_file)
        number_of_images=len(images)
        number_of_images=1
        for i in range(number_of_images):
            images[i].save('page'+ str(i) +'.jpg', 'JPEG')
            text = self.do_tesseract_image('page'+ str(i) +'.jpg')
            self.speak(text)
            break

if __name__ == "__main__":
    tess = Tess()
    #tess.do_tesseract()
    tess.read_pdf()
    