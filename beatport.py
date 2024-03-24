import wx
import subprocess

class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)

        # Create GUI components here
        self.url_text_ctrl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.load_file_button = wx.Button(self, -1, "Load URLs from File")
        self.start_button = wx.Button(self, -1, "Start")

        # Layout components
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.url_text_ctrl, 1, wx.EXPAND)
        sizer.Add(self.load_file_button, 0, wx.EXPAND)
        sizer.Add(self.start_button, 0, wx.EXPAND)
        self.SetSizer(sizer)

        # Bind events
        self.load_file_button.Bind(wx.EVT_BUTTON, self.on_load_file)
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start)

    def on_load_file(self, event):
        with wx.FileDialog(self, "Open text file", wildcard="Text files (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = file_dialog.GetPath()
            with open(path, 'r') as file:
                urls = file.read().splitlines()
                self.url_text_ctrl.SetValue("\n".join(urls))

    def on_start(self, event):
        urls = self.url_text_ctrl.GetValue().splitlines()
        for url in urls:
            # Call orpheus.py with the URL
            subprocess.run(["python", "orpheus.py", url], check=True)

def main():
    app = wx.App(False)
    frame = MainWindow(None, title="OrpheusDL - Beatport", size=(800, 600))
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
