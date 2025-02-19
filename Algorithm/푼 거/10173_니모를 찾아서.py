while True:
    text = input()
    if text == "EOI":
        break
    print("Found" if "nemo" in text.lower() else "Missing")
