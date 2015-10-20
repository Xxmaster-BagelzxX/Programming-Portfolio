# Secret Decoder


def main():
	message = raw_input("Enter a message: ")
	plain_message = open("plain_message.txt", "w")
	plain_message.write(message)
	plain_message.close()




main()
	