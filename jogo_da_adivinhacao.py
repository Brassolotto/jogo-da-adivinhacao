import random

def jogar_adivinhacao():
    numero_aleatorio = random.randint(1, 10)
    tentativas = 0
    
    print("\nBem-vindo ao jogo da adivinhação!")
    print("Tente adivinhar o número entre 1 e 10")
    
    while True:
        palpite = input("\nDigite seu palpite ou 'sair' para encerrar: ")
        
        if palpite.lower() == 'sair':
            print(f"\nO número era: {numero_aleatorio}")
            print("Obrigado por jogar!")
            return
            
        try:
            palpite = int(palpite)
            
            if palpite < 1 or palpite > 10:
                print("Por favor, digite um número entre 1 e 10!")
                continue
                
            tentativas += 1
            
            if palpite == numero_aleatorio:
                print(f"\nParabéns! Você acertou em {tentativas} tentativas!")
                print("Quer jogar novamente?")
                if input("Digite 's' para sim: ").lower() != 's':
                    print("Obrigado por jogar!")
                    return
                else:
                    numero_aleatorio = random.randint(1, 10)
                    tentativas = 0
                    print("\nNovo jogo iniciado!")
                    continue
                    
            elif palpite < numero_aleatorio:
                print("Dica: O número é MAIOR que isso!")
            else:
                print("Dica: O número é MENOR que isso!")
                
        except ValueError:
            print("Por favor, digite apenas números ou 'sair'!")

def main():
    while True:
        jogar_adivinhacao()
        break

if __name__ == "__main__":
    main()
