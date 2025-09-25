import gtts
import playsound
from googletrans import Translator, LANGUAGES

# Function to get the language code from user input
def get_language_code():
    print("Select the language for text-to-speech conversion:")
    print("1. Hindi")
    print("2. Bengali")
    print("3. Tamil")
    print("4. Telugu")
    print("5. Kannada")
    print("6. Gujarati")
    print("7. Marathi")
    print("8. Malayalam")
    print("9. Punjabi")

    while True:
        choice = input("Enter the number corresponding to the language: ")
        if choice == '1':
            return 'hi'
        elif choice == '2':
            return 'bn'
        elif choice == '3':
            return 'ta'
        elif choice == '4':
            return 'te'
        elif choice == '5':
            return 'kn'
        elif choice == '6':
            return 'gu'
        elif choice == '7':
            return 'mr'
        elif choice == '8':
            return 'ml'
        elif choice == '9':
            return 'pa'
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

def detect_language(text):
    try:
        translator = Translator()
        lang = translator.detect(text).lang
        return lang
    except ValueError as e:
        print(f"Error during language detection: {e}")
        return None
    except ConnectionError as e:
        print(f"Error during language detection: {e}")
        return None
    except Exception as e:
        print(f"Error during language detection: {e}")
        return None

def main():
    text = input("Enter the text you want to convert to speech: ")
    desired_lang_code = get_language_code()

    # Detect the language of the input text
    input_lang = detect_language(text)

    if input_lang:
        # Translate the text to the desired language if it's not already in that language 
        if input_lang != desired_lang_code:
            try:
                translator = Translator()
                translated_text = translator.translate(text, dest=desired_lang_code).text
            except Exception as e:
                print(f"Translation error: {e}")
                translated_text = text
        else:
            translated_text = text

        try:
            sound = gtts.gTTS(translated_text, lang=desired_lang_code)
            sound.save("output.mp3")
            playsound.playsound("output.mp3")
        except ValueError:
            print("Error: Language code not recognized or supported.")

if __name__ == "__main__":
  main()
