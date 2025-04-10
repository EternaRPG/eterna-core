from nicegui import ui

class SVGEnvironment:
    def __init__(self, width=10, height=10, tile_size=32):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tile_fill = '#f0f0f0'
        self.border = '#333'
        self.mount_point = None

    def handle_click(self, x: int, y: int):
        print(f'[SVGEnvironment] Clicked square: ({x}, {y})')

    def render(self):
        svg = f'<svg width="{self.width * self.tile_size}" height="{self.height * self.tile_size}" xmlns="http://www.w3.org/2000/svg">'
        for y in range(self.height):
            for x in range(self.width):
                svg += (
                    f'''<rect x="{x * self.tile_size}" y="{y * self.tile_size}" '
                    width="{self.tile_size}" height="{self.tile_size}" '
                    style="fill:{self.tile_fill};stroke:{self.border};stroke-width:1;" '
                    onclick="fetch('/click/{x}/{y}')"/>'''
                )
        svg += '</svg>'
        self.mount_point = ui.html(svg).classes('border')

    def mount(self):
        self.render()

@ui.page('/click/{x}/{y}')
def handle_click(x: int, y: int):
    print(f'Clicked ({x}, {y})')
