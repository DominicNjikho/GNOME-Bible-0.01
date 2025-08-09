from gi.repository import Gtk, GObject, Pango

@Gtk.Template(resource_path='/org/gnome/BibleReader/ui/bible_view.blp')
class BibleView(Gtk.Box):
    __gtype_name__ = 'BibleView'

    text_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buffer = self.text_view.get_buffer()
        self.settings = Gio.Settings.new('org.gnome.BibleReader')
        self._setup_style()

    def _setup_style(self):
        # Update font
        self.settings.connect('changed::font-family', self._update_font)
        self.settings.connect('changed::font-size', self._update_font)
        self._update_font()

    def _update_font(self, *args):
        font_family = self.settings.get_string('font-family')
        font_size = self.settings.get_int('font-size')
        font_desc = Pango.FontDescription.new()
        font_desc.set_family(font_family)
        font_desc.set_size(font_size * Pango.SCALE)
        self.text_view.override_font(font_desc)

    def load_chapter(self, book_id, chapter):
        # TODO: Implement actual chapter loading
        self.buffer.set_text(f"Loading {book_id} {chapter}...")