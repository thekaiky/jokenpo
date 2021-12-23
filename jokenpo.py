import random;
from time import sleep;

escolhaJogador = int(input(
    "Escolha uma opção\n[1] - Pedra [2] - Papel [3] - Tesoura: \n"
));
escolhaMaquina = random.randint(1,3);

print(f"\nJO");
sleep(.3);
print(f"KEN");
sleep(.3);
print(f"PO\n");
sleep(.3);

# 1
if escolhaJogador == 1 and escolhaMaquina == 1:
    print(f"Você escolheu Pedra e a Máquina Papel\nEMPATE!");  
elif escolhaJogador == 1 and escolhaMaquina == 2:
    print(f"Você escolheu Pedra e a Máquina Papel\nVitória da máquina!");
elif escolhaJogador == 1 and escolhaMaquina == 3:
    print(f"Você escolheu Pedra e a Máquina Tesoura\nVitória sua!");
# 2
elif escolhaJogador == 2 and escolhaMaquina == 1:
    print(f"Você escolheu Papel e a Máquina Pedra\nVitória sua!");
elif escolhaJogador == 2 and escolhaMaquina == 2:
    print(f"Você escolheu Papel e a Máquina Papel\nEMPATE!");
elif escolhaJogador == 2 and escolhaMaquina == 3:
    print(f"Você escolheu Papel e a Máquina Tesoura\nVitória sua!");
# 3
elif escolhaJogador == 3 and escolhaMaquina == 1:
    print(f"Você escolheu Tesoura e a Máquina Pedra\nVitória da máquina!");
elif escolhaJogador == 3 and escolhaMaquina == 2:
    print(f"Você escolheu Tesoura e a Máquina Papel\nVitória sua!");
elif escolhaJogador == 3 and escolhaMaquina == 3:
    print(f"Você escolheu Tesoura e a Máquina Tesoura\nEMPATE!");
else:
    print(f"Jogada inválida!");

print("\nBom jogo!");
