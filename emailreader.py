import imaplib2
import email
import email.header


class Email:

    def __init__(self, username, password, last_uid):
        self.username = username
        self.password = password
        self.last_uid = last_uid

    def unread(self):
        conn = imaplib2.IMAP4_SSL('imap.gmail.com', 993)
        conn.login(self.username, self.password)
        conn.list()
        conn.select('inbox')
        statuscode, uids = conn.search(None, '(UNSEEN)')
        emails = []
        unread = False

        for uid in sorted(uids[0].split()):
            unread = True
            if int(uid) <= self.last_uid:
                continue
            statuscode, data = conn.fetch(uid, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
            conn.store(uid, '-FLAGS','\\Seen') 
            header = data[0][1]
            msg = email.message_from_string(header)
            msg_from = msg.get("From")
            msg_subject = msg.get("Subject")
            data, encoding = email.header.decode_header(msg_subject)[0]
            if encoding != None:
                msg_subject = data.decode(encoding)
            data, encoding = email.header.decode_header(msg_from)[0]
            if encoding != None:
                msg_from = data.decode(encoding)

            emails.append((msg_from, msg_subject))
            self.last_uid = max(int(uid), self.last_uid)

        conn.close()
        conn.logout()
        return unread, emails
