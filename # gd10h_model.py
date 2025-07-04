# gd10h_model.py

from gp19f_block import GP19FBlock

class GD10HModel:
    def __init__(self, layer_dims):
        self.layers = []
        print("GD10H моделі инициализацияланды!")
        for i in range(len(layer_dims) - 1):
            layer = GP19FBlock(layer_dims[i], layer_dims[i+1])
            self.layers.append(layer)
        print(f"{len(self.layers)} қабатты GP19F құрылымы дайын ✅")

# Мысал: модельді іске қосу
if __name__ == "__main__":
    # Мысалы, 20 қабатты модель: 64 → 128 → 256 → ...
    model = GD10HModel([64, 128, 256])
