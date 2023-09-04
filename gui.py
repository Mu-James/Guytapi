import tkinter as tk
from tkinter import messagebox
import youtube_video as yv
import personal as p
import verify as v
from text import *

def _dummy():
    pass

class YoutubeApiGUI:
    def __init__(self):
        self._root_window = tk.Tk()
        self._root_window.title(WINDOW_TITLE_ROOT)
        self._root_window.geometry(DEFAULT_RESOLUTION)
        self._root_window.protocol(DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._yt_api_key = None

        #Labels
        welcome = self._create_label(self._root_window, LABEL_TEXT_WELCOME, 0, 0)

        #Buttons
        api_related = self._create_button(self._root_window, BUTTON_TEXT_API_RELATED, 1, 0, self._open_input_data_api_key)
        non_api_realted = self._create_button(self._root_window, BUTTON_TEXT_NON_API_RELATED, 2, 0, self._open_non_api_selection)
        close = self._create_button(self._root_window, BUTTON_TEXT_CLOSE, 3, 0, self._confirm_close_GUI)
        
    def run(self):
        self._root_window.mainloop()

    def _open_api_selection(self):
        self._window_api_selection = self._create_top_level_window(self._window_input_data_api_key, WINDOW_TITLE_API_SELECTION, DEFAULT_RESOLUTION)
        self._window_api_selection.protocol(DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._window_input_data_api_key.withdraw()

        #Labels
        selection = self._create_label(self._window_api_selection, LABEL_TEXT_API_SELECTION, 0, 0)

        #Buttons
        select_channels = self._create_button(self._window_api_selection, BUTTON_TEXT_CHANNELS, 1, 0, _dummy)
        select_playlists = self._create_button(self._window_api_selection, BUTTON_TEXT_PLAYLISTS, 2, 0, _dummy)
        select_videos = self._create_button(self._window_api_selection, BUTTON_TEXT_VIDEOS, 3, 0, self._open_videos_selection)
        back = self._create_button(self._window_api_selection, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._window_api_selection, self._window_input_data_api_key))

    def _open_input_data_api_key(self):
        self._window_input_data_api_key = self._create_top_level_window(self._root_window, WINDOW_TITLE_ENTER_DATA_API_KEY, DEFAULT_RESOLUTION)
        self._window_input_data_api_key.protocol(DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._root_window.withdraw()

        invalid_key = None

        def _submit_key(self, key):
            nonlocal invalid_key
            if invalid_key != None:
                invalid_key.destroy()

            verify = v.verify_api_key(key)
            if verify == True:
                self._yt_api_key = key
                self._open_api_selection()
            else:
                #Label
                invalid_key = self._create_label(self._window_input_data_api_key, verify, 2, 0)

        #Labels
        enter_label = self._create_label(self._window_input_data_api_key, LABEL_TEXT_ENTER_DATA_API_KEY, 0, 0)

        #Entries
        key_entry = self._create_entry(self._window_input_data_api_key, 50, 1, 0)

        #Buttons
        submit_key = self._create_button(self._window_input_data_api_key, BUTTON_TEXT_GO, 3, 0, lambda: _submit_key(self, key_entry.get()))
        back = self._create_button(self._window_input_data_api_key, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._window_input_data_api_key, self._root_window))

    def _open_videos_selection(self):
        self._videos_selection = self._create_top_level_window(self._window_api_selection, WINDOW_TITLE_VIDEOS_SELECTION, DEFAULT_RESOLUTION)
        self._videos_selection.protocol(DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._window_api_selection.withdraw()

        #Labels
        selection = self._create_label(self._videos_selection, LABEL_TEXT_VIDEOS_SELECTION, 0, 0)

        #Buttons
        get_video_thumbnail_url = self._create_button(self._videos_selection, BUTTON_TEXT_GET_THUMBNAIL_URL, 1, 0, self._get_thumbnail_url)
        back = self._create_button(self._videos_selection, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._videos_selection, self._window_api_selection))

    def _get_thumbnail_url(self):
        self._thumbnail_url = self._create_top_level_window(self._videos_selection, WINDOW_TITLE_GET_THUMBNAIL_URL, DEFAULT_RESOLUTION)
        self._thumbnail_url.protocol(DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._videos_selection.withdraw()

        tb_url = None

        def _submit_inputs(video_url, size, yt_api_key):
            nonlocal tb_url
            tb_url = yv.get_video_thumbnail_url_url(video_url, size, yt_api_key)
            result = self._create_textbox(self._thumbnail_url, 1, 50, 3, 1, tb_url, 'disabled')

        #Labels
        url_entry_label = self._create_label(self._thumbnail_url, LABEL_TEXT_ENTER_VIDEO_URL, 0, 0)
        select_size_label = self._create_label(self._thumbnail_url, LABEL_TEXT_SELECT_THUMBNAIL_SIZE, 1, 0)

        #Entries
        url_entry = self._create_entry(self._thumbnail_url, 50, 0, 1)

        #Dropdown
        size_var = tk.StringVar()
        sizes = [
            DROPDOWN_TEXT_DEFAULT,
            DROPDOWN_TEXT_MEDIUM,
            DROPDOWN_TEXT_HIGH,
            DROPDOWN_TEXT_STANDARD
        ]
        size_var.set(sizes[0])
        size_drop = tk.OptionMenu(self._thumbnail_url, size_var, *sizes)
        size_drop.grid(row = 1, column = 1)

        #Buttons
        submit_inputs = self._create_button(self._thumbnail_url, BUTTON_TEXT_GO, 2, 1, lambda: _submit_inputs(url_entry.get(), size_var.get().lower(), self._yt_api_key))

    def _open_non_api_selection(self):
        self._window_non_api_selection = self._create_top_level_window(self._root_window, WINDOW_TITLE_NON_API_SELECTION, DEFAULT_RESOLUTION)
        self._window_non_api_selection.protocol(DELETE_WINDOW_PROTCOL, self._confirm_close_GUI )
        self._root_window.withdraw()

        #Labels
        selection = self._create_label(self._window_non_api_selection, LABEL_TEXT_NON_API_SELECTION, 0, 0)

        #Buttons
        select_extract_ids = self._create_button(self._window_non_api_selection, BUTTON_TEXT_EXTRACT_IDS, 1, 0, _dummy)
        back = self._create_button(self._window_non_api_selection, BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_non_api_selection, self._root_window))
        
    def _extract_ids(self):
        self._window_extract_id_selection = self._create_top_level_window(self._window_non_api_selection, )

    def _back_to_previous_window(self, current, previous):
        current.withdraw()
        previous.deiconify()

    def _confirm_close_GUI(self):
        #response = tk.messagebox.askyesno(_MESSAGEBOX_TITLE_CONFIRM_CLOSE, _MESSAGEBOX_MESSAGE_CONFIRM_CLOSE)
        response = self._create_messagebox("askyesno", MESSAGEBOX_TITLE_CONFIRM_CLOSE, MESSAGEBOX_MESSAGE_CONFIRM_CLOSE)
        if response == True:
            self._root_window.destroy()
        elif response == False:
            pass

    def _create_button(self, master, text, row, column, command):
        button = tk.Button(
            master = master,
            text = text, font = DEFAULT_FONT,
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