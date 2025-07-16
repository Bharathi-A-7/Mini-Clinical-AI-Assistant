from gtts import gTTS

text = """This is a 29-year-old female here for a fertility consultation. She has been trying to conceive for 18 months without success. Reports irregular cycles, mild acne, and occasional pelvic discomfort. On examination, BMI is 31. Blood pressure is 138/88 mmHg. Transvaginal ultrasound shows mildly enlarged ovaries with multiple small follicles bilaterally. Tests advised are LH, FSH, prolactin, TSH, and total testosterone. Diagnosis is suspected polycystic ovarian syndrome (PCOS). Plan to monitor ovulation and consider letrozole if labs are consistent with anovulation. Prescribe metformin 500 mg once daily to improve insulin sensitivity and support ovulatory function."""

tts = gTTS(text)
tts.save("audio/sample_audio.wav")