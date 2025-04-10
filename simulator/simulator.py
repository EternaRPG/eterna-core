from nicegui import ui
from anima_model import AnimaModel
from simulator_ui import SimulatorUI

if __name__ in {"__main__", "__mp_main__"}:

    model = AnimaModel()
    layout = SimulatorUI(model)

    with ui.row():
        layout.mount()

    ui.run(title='Anima Simulation', reload=True)
