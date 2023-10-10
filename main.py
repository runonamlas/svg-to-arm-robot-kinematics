import tkinter as tk

from src.svg import extract_d_attribute, parse_coordinates, split_by_letter
from src.d import linear_interpolation, calculate_coordinates_with_h, calculate_coordinates_with_v, calculate_bezier_curve_points, calculate_q_and_curve_points
from src.coordinates import calculate_coordinates_with_d
from src import inside

dlist = []
svg_file_path = 'data/e.svg'
coordinatLists = []
t= 100
infill =10

# d niteliklerini al
dlist = extract_d_attribute.main(svg_file_path)
coordinatLists = calculate_coordinates_with_d.main(dlist, t)

#a = inside.scale_polygon(coordinatLists,2)


#inside.insidePoints(a,infill)


class CustomCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        print("here")
        if event.delta > 0:
            self.zoom_in(event.x, event.y)
        else:
            self.zoom_out(event.x, event.y)

    def zoom_in(self, x, y):
        self.scale("all", x, y, 1.2, 1.2)

    def zoom_out(self, x, y):
        self.scale("all", x, y, 0.8, 0.8)



class FullscreenApp:
    def __init__(self, master, polygon):
        self.master = master
        self.polygon = polygon
        master.title("SALMAN 2 DOF")
        #master.attributes('-fullscreen', False)  # Pencereyi tam ekrana getir

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Pencereyi ekran boyutunda boyutlandır
        master.geometry(f"{screen_width}x{screen_height}")

        # Tam ekranda bir etiket
        #self.label = tk.Label(master, text="Tam Ekran Uygulama", font=("Helvetica", 24))
        #self.label.pack(expand=True)

        self.canvas = CustomCanvas(master, width=400, height=400)
        self.canvas.pack()


        # Grafik çiz

        # Tam ekranda bir düğme
       # self.quit_button = tk.Button(master, text="Çıkış", command=master.quit)
        #self.quit_button.pack()


        # Poligonu çiz
        self.graph_id = self.canvas.create_polygon(self.polygon, fill='', outline='blue', width=2)
        self.canvas.bind('<Motion>', self.on_mouse_move)
        self.canvas.bind('<Button-1>', self.on_mouse_click)  # Sol tuşa tıklama

    def on_mouse_move(self, event):
        x, y = event.x, event.y
        widget_id = event.widget.find_closest(x, y)  # Grafiği kontrol et
        if widget_id and widget_id[0] == self.graph_id:
            print("Mouse grafik üzerinde.")
        else:
            print("Mouse grafik dışında.")

    def on_mouse_click(self, event):
        x, y = event.x, event.y
        widget_id = event.widget.find_closest(x, y)  # Grafiği kontrol et
        if widget_id and widget_id[0] == self.graph_id:
            print("Mouse grafik üzerinde tıklama yaptı.")
        else:
            print("Mouse grafik dışında tıklama yaptı.")


polygon_points = [(50, 100), (150, 50), (200, 100), (100, 150)]
root = tk.Tk()
app = FullscreenApp(root, coordinatLists)
root.mainloop()

