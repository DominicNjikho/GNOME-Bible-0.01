from gi.repository import Gtk, Gio, Adw

from .window import BibleWindow

class BibleApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='org.gnome.BibleReader',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.set_resource_base_path('/org/gnome/BibleReader/')

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = BibleWindow(application=self)
        win.present()