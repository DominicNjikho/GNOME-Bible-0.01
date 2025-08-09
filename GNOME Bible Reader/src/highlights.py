from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/BibleReader/ui/highlights_view.blp')
class HighlightsView(Gtk.Box):
    __gtype_name__ = 'HighlightsView'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)