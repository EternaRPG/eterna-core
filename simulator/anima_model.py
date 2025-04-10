from agentpy import Model, Grid
from anima_agent import AnimaAgent
from anima_entity import AnimaEntity

class AnimaModel(Model):
    def __init__(self, width=10, height=10):
        super().__init__()
        self.width = width
        self.height = height
        self.env = AnimaTerrain(self, (height, width), torus=False)

    def setup(self):
        """ Initiate a list of new agents. """
        pass

    def spawn_agent(self, entity: AnimaEntity = AnimaEntity(), position: tuple = (0, 0)):
            """ Creates an agent with a given entity and places it on the grid. """
            agent = AnimaAgent(self, p={'entity': entity})  # Pass the entity as a parameter
            self.env.add_agents([agent],[position])  # Store the agent in the model
            return agent

class AnimaTerrain(Grid):
    def __init__(self, model, shape, torus=False):
        super().__init__(model, shape, torus=torus)
        self.add_field('terrain', '')  # field[y][x] = terrain type

    def get_terrain(self, x: int, y: int) -> str:
        return self.fields['terrain'][y][x]

    def set_terrain(self, x: int, y: int, terrain_type: str):
        self.fields['terrain'][y][x] = terrain_type

    def toggle_terrain(self, x: int, y: int):
        terrain_types = ['empty', 'grass', 'water', 'wall']
        current = self.get_terrain(x, y)
        next_type = terrain_types[(terrain_types.index(current) + 1) % len(terrain_types)]
        self.set_terrain(x, y, next_type)

    def get_all_terrain(self):
        return self.fields['terrain']

    def reset_terrain(self, fill='empty'):
        self.fields['terrain'] = [[fill for _ in range(self.shape[1])] for _ in range(self.shape[0])]
