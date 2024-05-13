import numpy as np
import matplotlib.pyplot as plt
import time

class Robot:
    def __init__(self, grid_size=(21, 21), start_pos=(0, 0), orientation=(1, 0)):
        self.grid_size = grid_size
        self.pos = start_pos
        self.orientation = orientation 

        # Pontos a serem percorridos

        self.targets = [(5, 0), (-5, 0), (-5, 5), (5, 0), (5, 5), (5, -5), (-5, 5)]

    def move_to_target(self, target):
       
        dx = np.sign(target[0] - self.pos[0])
        dy = np.sign(target[1] - self.pos[1])

        
        if (dx, dy) == (0, 0): # Verifica se o robô já está no ponto alvo
            return False  

            
        if dx != 0: # Movimenta o robô na direção do próximo ponto
            self.move(dx, 0)
        elif dy != 0:
            self.move(0, dy)

        return True

    def move(self, dx, dy):
        
        new_pos = (self.pos[0] + dx, self.pos[1] + dy) # Atualiza a posição do robô

        
        if -10 <= new_pos[0] <= 10 and -10 <= new_pos[1] <= 10: # Verifica se a nova posição é válida
            self.pos = new_pos

       
        self.orientation = (dx, dy) # Atualiza a orientação do robô

    def visualize(self):
        
        plt.clf() # Limpa o gráfico

        # Desenha os eixos x e y
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)

        # Desenha o grid
        for i in range(-10, 11):
            plt.plot([i, i], [-10, 10], 'k', linewidth=0.5)
            plt.plot([-10, 10], [i, i], 'k', linewidth=0.5)

        # Desenha o robô como um quadrado preenchido
        robot_x, robot_y = self.pos
        plt.fill([robot_x - 0.5, robot_x + 0.5, robot_x + 0.5, robot_x - 0.5], 
                 [robot_y - 0.5, robot_y - 0.5, robot_y + 0.5, robot_y + 0.5], 
                 'green')

        # Define limites do gráfico
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        # Exibi o gráfico
        plt.pause(0.1)

# Cria o robô e definir sua posição inicial e orientação
robot = Robot(start_pos=(0, 0), orientation=(1, 0))  # Orientação padrão: frente para a direita

# Defini o tempo total de simulação
total_time = 30

# Inicia a contagem do tempo
start_time = time.time()

# Simula o movimento do robô até o tempo total
while time.time() - start_time < total_time:
    for target in robot.targets:
        while robot.move_to_target(target):
            robot.visualize()

# Fecha a visualização
plt.show()
