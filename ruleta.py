import tkinter as tk
from tkinter import font as tkfont
import random

class RuletaSorteoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruleta de Sorteo")
        self.root.configure(bg="#2c3e50")  # Dark background color

        # Define color palette
        self.colors = {
            'background': '#2c3e50',
            'primary': '#3498db',
            'secondary': '#2ecc71',
            'text_light': '#ecf0f1',
            'text_dark': '#34495e'
        }

        # Screen dimensions and positioning
        self.window_width = 700
        self.window_height = 650
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - self.window_height / 2)
        position_right = int(screen_width / 2 - self.window_width / 2)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{position_right}+{position_top}')

        # Configure custom fonts
        self.title_font = tkfont.Font(family="Segoe UI", size=28, weight="bold")
        self.subtitle_font = tkfont.Font(family="Segoe UI", size=16)
        self.button_font = tkfont.Font(family="Segoe UI", size=16, weight="bold")

        # Create main container with gradient background
        self.main_container = tk.Frame(self.root, bg=self.colors['background'])
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header Frame
        self.header_frame = tk.Frame(self.main_container, bg=self.colors['background'])
        self.header_frame.pack(pady=(10, 30), fill=tk.X)

        # Title
        self.title_label = tk.Label(
            self.header_frame, 
            text="Ruleta de Sorteo", 
            font=self.title_font, 
            fg=self.colors['text_light'], 
            bg=self.colors['background']
        )
        self.title_label.pack(pady=10)

        # Content Frame
        self.content_frame = tk.Frame(self.main_container, bg=self.colors['background'])
        self.content_frame.pack(expand=True, fill=tk.BOTH, padx=50)

        # Result Label (more prominent)
        self.resultado_label = tk.Label(
            self.content_frame, 
            text="", 
            font=tkfont.Font(family="Segoe UI", size=24, weight="bold"), 
            fg=self.colors['secondary'], 
            bg=self.colors['background']
        )
        self.resultado_label.pack(pady=20)

        # Participants Frame
        self.participants_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        self.participants_frame.pack(fill=tk.X, pady=10)

        # Participants Label
        self.lista_participantes_label = tk.Label(
            self.participants_frame, 
            text="Participantes Restantes:", 
            font=self.subtitle_font, 
            fg=self.colors['text_light'], 
            bg=self.colors['background']
        )
        self.lista_participantes_label.pack()

        # Participants List
        self.participantes = ["Juan", "Ana", "Luis", "Pedro", "Marta", "Carlos", "Sofia", "Tomás", "Laura", "Ricardo"]
        self.lista_participantes = tk.Label(
            self.participants_frame, 
            text=", ".join(self.participantes), 
            font=self.subtitle_font, 
            fg=self.colors['primary'], 
            bg=self.colors['background'], 
            wraplength=600
        )
        self.lista_participantes.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        self.buttons_frame.pack(pady=20)

        # Buttons with improved styling
        self.sorteo_button = self.create_button(
            "Realizar Sorteo", 
            self.colors['primary'], 
            self.realizar_sorteo
        )
        self.reiniciar_button = self.create_button(
            "Reiniciar", 
            self.colors['secondary'], 
            self.reiniciar_sorteo
        )

    def create_button(self, text, color, command):
        """Create a modern, styled button."""
        button = tk.Button(
            self.buttons_frame, 
            text=text, 
            font=self.button_font,
            bg=color, 
            fg=self.colors['text_light'], 
            command=command,
            relief=tk.FLAT,
            activebackground=self.darken_color(color),
            activeforeground=self.colors['text_light'],
            padx=30, 
            pady=10
        )
        button.pack(side=tk.LEFT, padx=10)
        
        # Hover effects
        button.bind("<Enter>", lambda e: button.config(bg=self.darken_color(color)))
        button.bind("<Leave>", lambda e: button.config(bg=color))
        
        return button

    def realizar_sorteo(self):
        """Start the lottery process with a visual delay."""
        if not self.participantes:
            self.resultado_label.config(text="¡Ya no quedan participantes!", fg=self.colors['secondary'])
            return
        
        self.resultado_label.config(text="Sorteando...", fg=self.colors['text_light'])
        self.root.update()
        self.root.after(1500, self.sorteo)

    def sorteo(self):
        """Perform the lottery and show the winner."""
        if not self.participantes:
            return

        ganador = random.choice(self.participantes)
        self.participantes.remove(ganador)
        
        self.resultado_label.config(text=f"¡Ganador: {ganador}!", fg=self.colors['secondary'])
        self.lista_participantes.config(text=", ".join(self.participantes))

        if not self.participantes:
            self.sorteo_button.config(state=tk.DISABLED)
            self.lista_participantes_label.config(text="No quedan participantes.")

    def reiniciar_sorteo(self):
        """Reset the lottery and restore participants."""
        self.participantes = ["Juan", "Ana", "Luis", "Pedro", "Marta", "Carlos", "Sofia", "Tomás", "Laura", "Ricardo"]
        self.resultado_label.config(text="", fg=self.colors['text_light'])
        self.lista_participantes.config(text=", ".join(self.participantes))
        self.sorteo_button.config(state=tk.NORMAL)
        self.lista_participantes_label.config(text="Participantes Restantes:")

    def darken_color(self, color):
        """Darken a color for hover effects."""
        color_rgb = self.hex_to_rgb(color)
        darken_factor = 0.7
        return self.rgb_to_hex(
            int(color_rgb[0] * darken_factor), 
            int(color_rgb[1] * darken_factor), 
            int(color_rgb[2] * darken_factor)
        )

    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, r, g, b):
        """Convert RGB to hex color."""
        return f'#{r:02x}{g:02x}{b:02x}'

def main():
    root = tk.Tk()
    app = RuletaSorteoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()