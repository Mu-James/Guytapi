import tkinter as tk

_BUTTON_API_RELATED = "API Related"
_BUTTON_NON_API_RELATED = "Non-API Related"
_WINDOW_TITLE = "Youtube API Application"
_START_RESOLUTION = "640x640"

class YoutubeApiGUI:
    def __init__(self):
        self._root_window = tk.Tk()
        self._root_window.title(_WINDOW_TITLE)
    
    def run(self):
        self._root_window.mainloop()

if __name__ == "__main__":
    ytapigui = YoutubeApiGUI()
    ytapigui.run()