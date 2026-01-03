# When we write hindi, japanese or chinese characters:
label_text = "Chai spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non-encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
