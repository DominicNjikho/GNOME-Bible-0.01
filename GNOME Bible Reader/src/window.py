from gi.repository import Gtk, Adw, Gio

from .bible_view import BibleView
from .commentary import CommentaryView
from .highlights import HighlightsView
from .settings import SettingsWindow
from .books import BIBLE_BOOKS

@Gtk.Template(resource_path='/org/gnome/BibleReader/ui/main_window.blp')
class BibleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'BibleWindow'

    book_dropdown = Gtk.Template.Child()
    chapter_dropdown = Gtk.Template.Child()
    translation_dropdown = Gtk.Template.Child()
    main_paned = Gtk.Template.Child()
    commentary_view = Gtk.Template.Child()
    bible_view = Gtk.Template.Child()
    highlights_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = Gio.Settings.new('org.gnome.BibleReader')

        # Setup book list
        book_list = Gtk.StringList()
        for book in BIBLE_BOOKS:
            book_list.append(book['name'])
        self.book_dropdown.set_model(book_list)

        # Set last book and chapter
        last_book = self.settings.get_string('last-book')
        last_chapter = self.settings.get_int('last-chapter')
        self._set_book(last_book)
        self._set_chapter(last_chapter)

        # Connect signals
        self.book_dropdown.connect('notify::selected', self._on_book_selected)
        self.chapter_dropdown.connect('notify::selected', self._on_chapter_selected)
        self.translation_dropdown.connect('notify::selected', self._on_translation_selected)

    def _set_book(self, book_id):
        for i, book in enumerate(BIBLE_BOOKS):
            if book['id'] == book_id:
                self.book_dropdown.set_selected(i)
                # Update chapter dropdown
                chapter_list = Gtk.StringList()
                for chapter in range(1, book['chapters'] + 1):
                    chapter_list.append(str(chapter))
                self.chapter_dropdown.set_model(chapter_list)
                break

    def _set_chapter(self, chapter):
        self.chapter_dropdown.set_selected(chapter - 1)

    def _on_book_selected(self, dropdown, _):
        index = dropdown.get_selected()
        if index == Gtk.INVALID_LIST_POSITION:
            return
        book = BIBLE_BOOKS[index]
        self.settings.set_string('last-book', book['id'])

        # Update chapter dropdown
        chapter_list = Gtk.StringList()
        for chapter in range(1, book['chapters'] + 1):
            chapter_list.append(str(chapter))
        self.chapter_dropdown.set_model(chapter_list)
        self.chapter_dropdown.set_selected(0)

        # Load new book and chapter
        self.bible_view.load_chapter(book['id'], 1)

    def _on_chapter_selected(self, dropdown, _):
        chapter = dropdown.get_selected() + 1
        if chapter < 1:
            return
        book_index = self.book_dropdown.get_selected()
        if book_index == Gtk.INVALID_LIST_POSITION:
            return
        book = BIBLE_BOOKS[book_index]
        self.settings.set_int('last-chapter', chapter)
        self.bible_view.load_chapter(book['id'], chapter)

    def _on_translation_selected(self, dropdown, _):
        # TODO: Implement translation change
        pass

    @Gtk.Template.Callback()
    def on_settings_clicked(self, button):
        settings_window = SettingsWindow(transient_for=self)
        settings_window.present()