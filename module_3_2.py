def send_email(message,recipient,sender = "univerity.help@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or (
            "@" or (".com" or "ru" or ".net")) not in (recipient or sender):
        print(f"Unable to send email from address {sender}to the address {recipient}")
    elif recipient == sender:
        print("You can't send a letter to yourself!")
    elif sender == "university.help@gmail.com":
        print(f"The letter was successfully sent from the address{sender} to the address {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"NON-STANDARD SENDER!The letter was successfully sent from the address {sender} to the address {recipient}.")
send_email('messagje', 'university.help@mail.com', '@.com')
send_email('messagje', 'university.help@mail.com')
send_email('messagje', 'universi@.com')
send_email('messagje', 'universi@.co')
send_email('messagje', 'universi@.com')