# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out#

text = "X-DSPAM-Confidence:    0.8475"
string_1=text.find(" ")
largo=len(text)
string_2=text[string_1:largo]
string_3=string_2.lstrip()
print(float(string_3))
