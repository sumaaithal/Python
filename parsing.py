text = "X-DSPAM-Confidence:    0.8475"

start_of_number = text.find('0')
print(float(text[start_of_number:]))