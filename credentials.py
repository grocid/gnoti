import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class Credentials(Gtk.Dialog):

    def __init__(self, username, password):
        # This is sort of un-used as of now,
        # as the email and password is not
        # updated in keychain
        Gtk.Dialog.__init__(self, "Credentials", None, 0,
            (Gtk.STOCK_OK, Gtk.ResponseType.OK,
             Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        self.set_default_size(400, 200)
        box = self.get_content_area()

        box.add(Gtk.Label("Gmail"))
        self.gmail = Gtk.Entry()
        self.gmail.set_text(username)
        box.add(self.gmail)
        
        box.add(Gtk.Label("Password"))
        self.pwinput = Gtk.Entry()
        self.pwinput.set_invisible_char("*")
        self.pwinput.set_visibility(False)
        self.pwinput.set_text(password)
        box.add(self.pwinput)
        
        self.show_all()
