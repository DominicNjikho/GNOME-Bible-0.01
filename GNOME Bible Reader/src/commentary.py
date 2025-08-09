from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/BibleReader/ui/commentary_view.blp')
class CommentaryView(Gtk.Box):
    __gtype_name__ = 'CommentaryView'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)