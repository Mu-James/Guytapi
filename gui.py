import tkinter as tk
from tkinter import messagebox
import youtube_video as yv
import youtube_channel as yc
import personal as p
import verify as v
import extract as e
from text import *
from defaults import *

def _dummy():
    pass

class YoutubeApiGUI:
    def __init__(self):
        self._root_window = tk.Tk()
        self._root_window.title(WINDOW_TITLE_ROOT)
        self._root_window.geometry(DEFAULT_RESOLUTION)
        self._root_window.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._yt_api_key = None

        self._CHANNEL_STATISTICS_TEXTBOX_HEIGHT = 5
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
        self._window_api_selection.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_input_data_api_key.withdraw()

        #Labels
        selection = self._create_label(self._window_api_selection, LABEL_TEXT_API_SELECTION, 0, 0)

        #Buttons
        select_channels = self._create_button(self._window_api_selection, BUTTON_TEXT_CHANNELS, 1, 0, self._open_channels_selection)
        select_playlists = self._create_button(self._window_api_selection, BUTTON_TEXT_PLAYLISTS, 2, 0, _dummy)
        select_videos = self._create_button(self._window_api_selection, BUTTON_TEXT_VIDEOS, 3, 0, self._open_videos_selection)
        back = self._create_button(self._window_api_selection, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._window_api_selection, self._window_input_data_api_key))

    def _open_input_data_api_key(self):
        self._window_input_data_api_key = self._create_top_level_window(self._root_window, WINDOW_TITLE_ENTER_DATA_API_KEY, DEFAULT_RESOLUTION)
        self._window_input_data_api_key.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
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
        key_entry = self._create_entry(self._window_input_data_api_key, DEFAULT_ENTRY_SIZE, 1, 0)

        #Buttons
        submit_key = self._create_button(self._window_input_data_api_key, BUTTON_TEXT_GO, 3, 0, lambda: _submit_key(self, key_entry.get()))
        back = self._create_button(self._window_input_data_api_key, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._window_input_data_api_key, self._root_window))

    def _open_channels_selection(self):
        self._window_channels_selection = self._create_top_level_window(self._window_api_selection, WINDOW_TITLE_CHANNELS_SELECTION, DEFAULT_RESOLUTION)
        self._window_channels_selection.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_api_selection.withdraw()

        #Labels
        selection = self._create_label(self._window_channels_selection, LABEL_TEXT_SELECT_OPTION_BELOW, 0, 0)

        #Buttons
        get_channel_stats = self._create_button(self._window_channels_selection, BUTTON_TEXT_GET_STATS, 1, 0, self._get_channel_stats)
        back = self._create_button(self._window_channels_selection, BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_channels_selection, self._window_api_selection))

    def _get_channel_stats(self):
        self._window_get_channel_stats = self._create_top_level_window(self._window_channels_selection, WINDOW_TITLE_GET_CHANNEL_STATS, DEFAULT_RESOLUTION)
        self._window_get_channel_stats.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_channels_selection.withdraw()

        def _submit_channel_url(channel_url, yt_api_key):
            stats_string = yc.get_parsed_channel_statistics_response(yc.get_channel_statistics_url(channel_url, yt_api_key))
            result = self._create_textbox(self._window_get_channel_stats, self._CHANNEL_STATISTICS_TEXTBOX_HEIGHT, DEFAULT_TEXTBOX_WIDTH, 1, 1, stats_string, DEFAULT_TEXTBOX_STATE)

        #Labels
        enter_channel_url = self._create_label(self._window_get_channel_stats, LABEL_TEXT_ENTER_CHANNEL_URL, 0, 0)

        #Entries
        channel_url_entry = self._create_entry(self._window_get_channel_stats, DEFAULT_ENTRY_SIZE, 0, 1)

        #Buttons
        submit_channel_url = self._create_button(self._window_get_channel_stats, BUTTON_TEXT_GO, 1, 0, lambda: _submit_channel_url(channel_url_entry.get(), self._yt_api_key))
        back = self._create_button(self._window_get_channel_stats, BUTTON_TEXT_BACK, 3, 0, lambda: self._back_to_previous_window(self._window_get_channel_stats, self._window_channels_selection))


    def _open_videos_selection(self):
        self._videos_selection = self._create_top_level_window(self._window_api_selection, WINDOW_TITLE_VIDEOS_SELECTION, DEFAULT_RESOLUTION)
        self._videos_selection.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_api_selection.withdraw()

        #Labels
        selection = self._create_label(self._videos_selection, LABEL_TEXT_VIDEOS_SELECTION, 0, 0)

        #Buttons
        get_video_num_views = self._create_button(self._videos_selection, BUTTON_TEXT_GET_NUM_VIEWS, 2, 0, self._get_video_view_count)
        get_video_thumbnail_url = self._create_button(self._videos_selection, BUTTON_TEXT_GET_THUMBNAIL_URL, 1, 0, self._get_thumbnail_url)
        back = self._create_button(self._videos_selection, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._videos_selection, self._window_api_selection))

    def _get_thumbnail_url(self):
        self._thumbnail_url = self._create_top_level_window(self._videos_selection, WINDOW_TITLE_GET_THUMBNAIL_URL, DEFAULT_RESOLUTION)
        self._thumbnail_url.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._videos_selection.withdraw()

        tb_url = None

        def _submit_inputs(video_url, size, yt_api_key):
            nonlocal tb_url
            tb_url = yv.get_video_thumbnail_url_url(video_url, size, yt_api_key)
            result = self._create_textbox(self._thumbnail_url, 1, 50, 2, 1, tb_url, 'disabled')

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
        submit_inputs = self._create_button(self._thumbnail_url, BUTTON_TEXT_GO, 2, 0, lambda: _submit_inputs(url_entry.get(), size_var.get().lower(), self._yt_api_key))
        back = self._create_button(self._thumbnail_url, BUTTON_TEXT_BACK, 3, 0, lambda: self._back_to_previous_window(self._thumbnail_url, self._videos_selection))

    def _get_video_view_count(self):
        self._window_video_get_num_views = self._create_top_level_window(self._videos_selection, WINDOW_TITLE_VIDEO_GET_NUM_VIEWS, DEFAULT_RESOLUTION)
        self._window_video_get_num_views.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._videos_selection.withdraw()

        def _submit_video_url(video_url, yt_api_key):
            view_count = yv.get_video_view_count_url(video_url, yt_api_key)
            result = self._create_textbox(self._window_video_get_num_views, DEFAULT_TEXTBOX_HEIGHT, DEFAULT_TEXTBOX_WIDTH, 1, 1, view_count, DEFAULT_TEXTBOX_STATE)

        #Labels
        enter_video_url = self._create_label(self._window_video_get_num_views, LABEL_TEXT_ENTER_VIDEO_URL, 0, 0)

        #Entries
        channel_url_entry = self._create_entry(self._window_video_get_num_views, DEFAULT_ENTRY_SIZE, 0, 1)

        #Buttons
        submit_video_url = self._create_button(self._window_video_get_num_views, BUTTON_TEXT_GO, 1, 0, lambda: _submit_video_url(channel_url_entry.get(), self._yt_api_key))
        back = self._create_button(self._window_video_get_num_views, BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_video_get_num_views, self._videos_selection))

    def _open_non_api_selection(self):
        self._window_non_api_selection = self._create_top_level_window(self._root_window, WINDOW_TITLE_NON_API_SELECTION, DEFAULT_RESOLUTION)
        self._window_non_api_selection.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI )
        self._root_window.withdraw()

        #Labels
        selection = self._create_label(self._window_non_api_selection, LABEL_TEXT_NON_API_SELECTION, 0, 0)

        #Buttons
        select_extract_ids = self._create_button(self._window_non_api_selection, BUTTON_TEXT_EXTRACT_IDS, 1, 0, lambda: self._extract_ids())
        back = self._create_button(self._window_non_api_selection, BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_non_api_selection, self._root_window))
        
    def _extract_ids(self):
        self._window_extract_id_selection = self._create_top_level_window(self._window_non_api_selection, WINDOW_TITLE_EXTRACT_IDS_SELECTION, DEFAULT_RESOLUTION)
        self._window_extract_id_selection.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_non_api_selection.withdraw()

        #Labels
        selection = self._create_label(self._window_extract_id_selection, LABEL_TEXT_SELECT_EXTRACT_ID, 0, 0)

        #Buttons
        playlist_id =  self._create_button(self._window_extract_id_selection, BUTTON_TEXT_PLAYLISTS, 1, 0, lambda: self._extract_playlist_id())
        channel_id = self._create_button(self._window_extract_id_selection, BUTTON_TEXT_CHANNELS, 2, 0, lambda: self._extract_channel_id())
        video_id = self._create_button(self._window_extract_id_selection, BUTTON_TEXT_VIDEOS, 3, 0, lambda: self._extract_video_id())
        back = self._create_button(self._window_extract_id_selection, BUTTON_TEXT_BACK, 4, 0, lambda: self._back_to_previous_window(self._window_extract_id_selection, self._window_non_api_selection))

    def _extract_playlist_id(self):
        self._window_extract_playlist_id = self._create_top_level_window(self._window_extract_id_selection, WINDOW_TITLE_EXTRACT_PLAYLIST_ID, DEFAULT_RESOLUTION)
        self._window_extract_playlist_id.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_extract_id_selection.withdraw()

        def _submit_playlist_url(playlist_url): 
            playlist_id = e.extract_youtube_playlist_id_from_url(playlist_url)
            result = self._create_textbox(self._window_extract_playlist_id, DEFAULT_TEXTBOX_HEIGHT, DEFAULT_TEXTBOX_WIDTH, 1, 1, playlist_id, DEFAULT_TEXTBOX_STATE)

        #Labels
        enter_playlist_url = self._create_label(self._window_extract_playlist_id, LABEL_TEXT_ENTER_PLAYLIST_URL, 0, 0)

        #Entries
        playlist_url_entry = self._create_entry(self._window_extract_playlist_id, DEFAULT_ENTRY_SIZE, 0, 1)

        #Buttons
        submit_playlist_url = self._create_button(self._window_extract_playlist_id, BUTTON_TEXT_GO, 1, 0, lambda: _submit_playlist_url(playlist_url_entry.get()))
        back = self._create_button(self._window_extract_playlist_id, BUTTON_TEXT_BACK, 3, 0, lambda: self._back_to_previous_window(self._window_extract_playlist_id, self._window_extract_id_selection))

    def _extract_channel_id(self):
        self._window_extract_channel_id = self._create_top_level_window(self._window_extract_id_selection, WINDOW_TITLE_EXTRACT_CHANNEL_ID, DEFAULT_RESOLUTION)
        self._window_extract_channel_id.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_extract_id_selection.withdraw()

        def _submit_channel_url(channel_url):
            channel_id = e.extract_youtube_channel_id_from_url(channel_url)
            result = self._create_textbox(self._window_extract_channel_id, DEFAULT_TEXTBOX_HEIGHT, DEFAULT_TEXTBOX_WIDTH, 1, 1, channel_id, DEFAULT_TEXTBOX_STATE)

        #Labels
        enter_channel_url = self._create_label(self._window_extract_channel_id, LABEL_TEXT_ENTER_CHANNEL_URL, 0, 0)

        #Entries
        channel_url_entry = self._create_entry(self._window_extract_channel_id, DEFAULT_ENTRY_SIZE, 0, 1)

        #Buttons
        submit_channel_url = self._create_button(self._window_extract_channel_id, BUTTON_TEXT_GO, 1, 0, lambda: _submit_channel_url(channel_url_entry.get()))
        back = self._create_button(self._window_extract_channel_id, BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_extract_channel_id, self._window_extract_id_selection))

    def _extract_video_id(self):
        self._window_extract_video_id = self._create_top_level_window(self._window_extract_id_selection, WINDOW_TITLE_EXTRACT_VIDEO_ID, DEFAULT_RESOLUTION)
        self._window_extract_video_id.protocol(DEFAULT_DELETE_WINDOW_PROTOCOL, self._confirm_close_GUI)
        self._window_extract_id_selection.withdraw()

        def _submit_video_url(video_url):
            video_id = e.extract_youtube_video_id_from_url(video_url)
            result = self._create_textbox(self._window_extract_video_id, DEFAULT_TEXTBOX_HEIGHT, DEFAULT_TEXTBOX_WIDTH, 1, 1, video_id, DEFAULT_TEXTBOX_STATE)

        #Labels
        enter_video_url = self._create_label(self._window_extract_video_id, LABEL_TEXT_ENTER_VIDEO_URL, 0, 0)

        #Entries
        video_url_entry = self._create_entry(self._window_extract_video_id, DEFAULT_ENTRY_SIZE, 0, 1)

        #Buttons
        submit_video_url = self._create_button(self._window_extract_video_id, BUTTON_TEXT_GO, 1, 0, lambda: _submit_video_url(video_url_entry.get()))
        back = self._create_button(self._window_extract_video_id, BUTTON_TEXT_BACK, 2, 0, lambda: self._back_to_previous_window(self._window_extract_video_id, self._window_extract_id_selection))

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