import tkinter as tk

_LABLE_TEXT_WELCOME = "Welcome, please choose an option below:"

_BUTTON_TEXT_API_RELATED = "API Related"
_BUTTON_TEXT_NON_API_RELATED = "Non-API Related"
_BUTTON_TEXT_CLOSE = "Close"

_WINDOW_TITLE = "Youtube API GUI"
_START_RESOLUTION = "512x512"
_DEFAULT_FONT = "Arial"

def _dummy():
    pass

class YoutubeApiGUI:
    def __init__(self):
        self._root_window = tk.Tk()
        self._root_window.title(_WINDOW_TITLE)
        self._root_window.geometry(_START_RESOLUTION)

        #Labels
        welcome = self._create_label(self._root_window, _LABLE_TEXT_WELCOME, 0, 0)

        #Buttons
        api_related = self._create_button(self._root_window, _BUTTON_TEXT_API_RELATED, 1, 0, _dummy)
        non_api_realted = self._create_button(self._root_window, _BUTTON_TEXT_NON_API_RELATED, 2, 0, _dummy)
        close = self._create_button(self._root_window, _BUTTON_TEXT_CLOSE, 3, 0, self._root_window.quit)

    def run(self):
        self._root_window.mainloop()

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
    
    def _create_messagebox(self, master, style, title, message):
        exec(
            f"""messagebox = tk.messagebox.{style}(
                master = {master},
                title = {title},
                message = {message}
            )
            return messagebox"""
        ) 

if __name__ == "__main__":
    ytapigui = YoutubeApiGUI()
    ytapigui.run()