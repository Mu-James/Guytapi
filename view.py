import tkinter as tk
from tkinter import messagebox
import youtube_video as yv
import personal as p

_DELETE_WINDOW_PROTCOL = "WM_DELETE_WINDOW",

_LABEL_TEXT_WELCOME = "Welcome, please choose an option below:"
_LABEL_TEXT_API_SELECTION = "Please select an API category below:"
_LABEL_TEXT_NON_API_SELECTION = "Please select an option below:"
_LABEL_TEXT_VIDEOS_SELECTION = "Please select an action below:"
_LABEL_TEXT_ENTER_VIDEO_URL = "Enter a Youtube Video URL"
_LABEL_TEXT_SELECT_THUMBNAIL_SIZE = "Select a thumbnail size"

_BUTTON_TEXT_API_RELATED = "API Related"
_BUTTON_TEXT_NON_API_RELATED = "Non-API Related"
_BUTTON_TEXT_CLOSE = "Close"
_BUTTON_TEXT_VIDEOS = "Videos"
_BUTTON_TEXT_CHANNELS = "Channels"
_BUTTON_TEXT_PLAYLISTS = "Playlists"
_BUTTON_TEXT_EXTRACT_IDS = "Extract IDs"
_BUTTON_TEXT_BACK = "Back"
_BUTTON_TEXT_GET_THUMBNAIL_URL = "Get Thumbnail URL"
_BUTTON_TEXT_GO = "Go"

_DROPDOWN_TEXT_DEFAULT = "Default"
_DROPDOWN_TEXT_MEDIUM = "Medium"
_DROPDOWN_TEXT_HIGH = "High"
_DROPDOWN_TEXT_STANDARD = "Standard"


_MESSAGEBOX_TITLE_CONFIRM_CLOSE = "Close Youtube API GUI?"
_MESSAGEBOX_MESSAGE_CONFIRM_CLOSE = "Are you sure you want to close Youtube API GUI?"

_WINDOW_TITLE_API_SELECTION = "Youtube API GUI: API Selection"
_WINDOW_TITLE_NON_API_SELECTION = "Youtube API GUI: Non-API Selection"
_WINDOW_TITLE_VIDEOS_SELECTION = "Youtube API GUI: Videos"
_WINDOW_TITLE_GET_THUMBNAIL_URL = "Youtube API GUI: Video Thumbnail URL"

_WINDOW_TITLE_ROOT = "Youtube API GUI"
_DEFAULT_RESOLUTION = "512x512"
_DEFAULT_FONT = "Arial"

def _dummy():
    pass

class YoutubeApiGUI:
    def __init__(self):
        self._root_window = tk.Tk()
        self._root_window.title(_WINDOW_TITLE_ROOT)
        self._root_window.geometry(_DEFAULT_RESOLUTION)

        #Labels
        welcome = self._create_label(self._root_window, _LABEL_TEXT_WELCOME, 0, 0)

        #Buttons
        api_related = self._create_button(self._root_window, _BUTTON_TEXT_API_RELATED, 1, 0, self._open_api_selection)
        non_api_realted = self._create_button(self._root_window, _BUTTON_TEXT_NON_API_RELATED, 2, 0, self._open_non_api_selection)
        close = self._create_button(self._root_window, _BUTTON_TEXT_CLOSE, 3, 0, self._confirm_close_GUI)
        
    def run(self):
        self._root_window.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._root_window.mainloop()

    def _open_api_selection(self):
        self._window_api_selection = self._create_top_level_window(self._root_window, _WINDOW_TITLE_API_SELECTION, _DEFAULT_RESOLUTION)
        self._window_api_selection.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._root_window.withdraw()

        #Labels
        selection = self._create_label(self._window_api_selection, _LABEL_TEXT_API_SELECTION, 0, 0)

        #Buttons
        select_channels = self._create_button(self._window_api_selection, _BUTTON_TEXT_CHANNELS, 1, 0, _dummy)
        select_playlists = self._create_button(self._window_api_selection, _BUTTON_TEXT_PLAYLISTS, 2, 0, _dummy)
        select_videos = self._create_button(self._window_api_selection, _BUTTON_TEXT_VIDEOS, 3, 0, self._open_videos_selection)
        back = self._create_button(self._window_api_selection, _BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._window_api_selection, self._root_window))

    def _open_non_api_selection(self):
        self._window_non_api_selection = self._create_top_level_window(self._root_window, _WINDOW_TITLE_NON_API_SELECTION, _DEFAULT_RESOLUTION)
        self._window_non_api_selection.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI )
        self._root_window.withdraw()

        #Labels
        selection = self._create_label(self._window_non_api_selection, _LABEL_TEXT_NON_API_SELECTION, 0, 0)

        #Buttons
        select_extract_ids = self._create_button(self._window_non_api_selection, _BUTTON_TEXT_EXTRACT_IDS, 1, 0, _dummy)
        back = self._create_button(self._window_non_api_selection, _BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_non_api_selection, self._root_window))

    def _open_videos_selection(self):
        self._videos_selection = self._create_top_level_window(self._window_api_selection, _WINDOW_TITLE_VIDEOS_SELECTION, _DEFAULT_RESOLUTION)
        self._videos_selection.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._window_api_selection.withdraw()

        #Labels
        selection = self._create_label(self._videos_selection, _LABEL_TEXT_VIDEOS_SELECTION, 0, 0)

        #Buttons
        get_video_thumbnail_url = self._create_button(self._videos_selection, _BUTTON_TEXT_GET_THUMBNAIL_URL, 1, 0, self._get_thumbnail_url)

    def _get_thumbnail_url(self):
        self._thumbnail_url = self._create_top_level_window(self._videos_selection, _WINDOW_TITLE_GET_THUMBNAIL_URL, _DEFAULT_RESOLUTION)
        self._thumbnail_url.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._videos_selection.withdraw()

        tb_url = None

        def _submit_inputs(video_url, size, yt_api_key):
            nonlocal tb_url
            tb_url = yv.get_video_thumbnail_url_url(video_url, size, yt_api_key)
            result = self._create_textbox(self._thumbnail_url, 1, 50, 3, 1, tb_url, 'disabled')

        #Labels
        url_entry_label = self._create_label(self._thumbnail_url, _LABEL_TEXT_ENTER_VIDEO_URL, 0, 0)
        select_size_label = self._create_label(self._thumbnail_url, _LABEL_TEXT_SELECT_THUMBNAIL_SIZE, 1, 0)

        #Entries
        url_entry = self._create_entry(self._thumbnail_url, 50, 0, 1)

        #Dropdown
        size_var = tk.StringVar()
        sizes = [
            _DROPDOWN_TEXT_DEFAULT,
            _DROPDOWN_TEXT_MEDIUM,
            _DROPDOWN_TEXT_HIGH,
            _DROPDOWN_TEXT_STANDARD
        ]
        size_var.set(sizes[0])
        size_drop = tk.OptionMenu(self._thumbnail_url, size_var, *sizes)
        size_drop.grid(row = 1, column = 1)

        #Buttons
        submit_inputs = self._create_button(self._thumbnail_url, _BUTTON_TEXT_GO, 2, 1, lambda: _submit_inputs(url_entry.get(), size_var.get().lower(), p.yt_api_key))

    def _back_to_previous_window(self, current, previous):
        current.withdraw()
        previous.deiconify()

    def _confirm_close_GUI(self):
        #response = tk.messagebox.askyesno(_MESSAGEBOX_TITLE_CONFIRM_CLOSE, _MESSAGEBOX_MESSAGE_CONFIRM_CLOSE)
        response = self._create_messagebox("askyesno", _MESSAGEBOX_TITLE_CONFIRM_CLOSE, _MESSAGEBOX_MESSAGE_CONFIRM_CLOSE)
        if response == True:
            self._root_window.destroy()
        elif response == False:
            pass

    def _create_button(self, master, text, row, column, command):
        button = tk.Button(
            master = master,
            text = text, font = _DEFAULT_FONT,
            command = command
        )
        button.grid(
            row = row,
            column = column,
        )
        return button
    
    def _create_label(self, master, text, row, column):
        label = tk.Label(
            master = master,
            text = text,
        )
        label.grid(
            row = row,
            column = column
        )
        return label
    
    def _create_messagebox(self, style, title, message):
        data = {"tk":tk}
        exec(f'messagebox = tk.messagebox.{style}(title = "{title}", message = "{message}")', data)
        return data['messagebox']
    
    def _create_top_level_window(self, root, title, resolution):
        top_window = tk.Toplevel(root)
        top_window.title(title)
        top_window.geometry(resolution)
        return top_window
    
    def _create_entry(self, master, width, row, column):
        entry = tk.Entry(
            master = master,
            width = width
        )
        entry.grid(row = row, column = column)
        return entry
    
    def _create_textbox(self, master, height, width, row, column, text, state):
        textbox = tk.Text(
            master = master,
            height = height,
            width = width
        )
        textbox.grid(
            row = row,
            column = column
        )
        textbox.insert('end', text)
        textbox.config(state = state)
        return textbox

if __name__ == "__main__":
    ytapigui = YoutubeApiGUI()
    ytapigui.run()