class AnimaEntity:
    def __init__(
        self,
        name: str,
        description: str = '',
        animus: int = 0,
        animus_max: int = 10,
        affinities: dict[str, int] = None,
        polarities: dict[str, str] = None,
        inventory: list = None
    ):
        self.name = name
        self.description = description
        self.animus = animus
        self.animus_max = animus_max

        # Planar affinities: e.g. {'fire': 2, 'mind': 3}
        self.affinities = affinities or {}

        # Planar polarities: e.g. {'fire': 'chaotic', 'mind': 'fixed'}
        self.polarities = polarities or {}

        # Inventory: e.g. list of item IDs, objects, or strings
        self.inventory = inventory or []

    def adjust_animus(self, delta: int):
        self.animus = max(0, min(self.animus + delta, self.animus_max))

    def set_affinity(self, plane: str, value: int):
        self.affinities[plane] = value

    def set_polarity(self, plane: str, value: str):
        assert value in {'chaotic', 'balanced', 'fixed'}
        self.polarities[plane] = value

    def __repr__(self):
        return f'<AnimaEntity {self.name}: {self.animus}/{self.animus_max} Animus>'
