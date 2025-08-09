from gi.repository import Gtk, Adw, Gio

@Gtk.Template(resource_path='/org/gnome/BibleReader/ui/settings_window.blp')
class SettingsWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'SettingsWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = Gio.Settings.new('org.gnome.BibleReader')

        # Setup theme switch
        self.theme_switch = self.ThemeRow.get_row().get_last_child()
        current_theme = self.settings.get_string('theme')
        self.theme_switch.set_active(current_theme == 'dark')
        self.theme_switch.connect('state-set', self._on_theme_changed)

    def _on_theme_changed(self, switch, state):
        theme = 'dark' if state else 'light'
        self.settings.set_string('theme', theme)