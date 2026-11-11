fail = open("nimed.txt", "w", encoding="utf-8")
fail.write("Mari\n")
fail.write("Jüri\n")
fail.write("Anna\n")
fail.close()

fail = open("nimed.txt", "r", encoding="utf-8")
read = fail.readlines()
fail.close()

print(f"Failis on {len(read)} nime.")