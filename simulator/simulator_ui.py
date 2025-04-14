from nicegui import ui
from components.svg_environment import SVGEnvironment  # your visual layer
from anima_model import AnimaModel

class SimulatorUI:
    def __init__(self, model: AnimaModel):
        self.model = model

        # Mountable visual components
        self.env = SVGEnvironment(
            width=model.width,
            height=model.height
        )

        # placeholder slots for UI elements
        self.entity_panel = None
        self.simulation_controls = None
        self.output_log = None

    def mount(self):
        with ui.column().classes('flex-1 gap-4'):
            self._mount_entity_panel()
            ui.label('🌍 Environment').classes('text-lg font-semibold')
            self.env.mount()
            self._mount_sim_controls()
            self._mount_output_log()

    def _mount_entity_panel(self):
        ui.label('📦 Entities').classes('text-lg font-semibold')
        self.entity_panel = ui.column()
        with self.entity_panel:
            ui.button('+ Add Entity', on_click=self._add_agent).classes('mt-2')
            self.entity_list = ui.column().classes('gap-2')

    def _add_agent(self):
        self.model.spawn_agent()
        self._render_entity_rows()

    def _render_entity_rows(self):
        self.entity_list.clear()
        for agent in self.model.env.agents:
            with self.entity_list:
                with ui.row().classes('flex items-center gap-2'):
                    ui.label(agent.entity.name).classes('w-32')
                    ui.label(f'Animus: {agent.entity.animus}').classes('w-24')
                    ui.number(label='X', value=agent.pos[0], on_change=lambda e, a=agent: self._update_pos(a, 'x', e.value)).classes('w-20')
                    ui.number(label='Y', value=agent.pos[1], on_change=lambda e, a=agent: self._update_pos(a, 'y', e.value)).classes('w-20')

    def _update_pos(self, agent, axis, value):
        x, y = agent.pos
        new_pos = (value, y) if axis == 'x' else (x, value)
        self.model.env.move_to(agent, new_pos)
        agent.pos = new_pos

    def _mount_sim_controls(self):
        ui.label('🎮 Simulation Control').classes('text-lg font-semibold')
        self.simulation_controls = ui.row()
        ui.button('Go', on_click=self._run_simulation)

    def _mount_output_log(self):
        ui.label('📊 Output Log').classes('text-lg font-semibold')
        self.output_log = ui.textarea('').props('readonly').classes('w-full h-64')

    def _run_simulation(self):
        # Stub: replace with model.run(...) or per-step logic
        print('[SimulatorUI] Running simulation...')
        self.output_log.value += 'Simulation started...\n'
