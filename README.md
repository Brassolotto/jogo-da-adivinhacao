# Jogo da Adivinhação em Python

## 📝 Descrição
Um jogo interativo onde o jogador tenta adivinhar um número aleatório entre 1 e 10. O programa oferece dicas para ajudar o jogador a encontrar o número correto e mantém o controle das tentativas.

## 🎮 Funcionalidades
- Geração aleatória de números
- Sistema de dicas (maior/menor)
- Contador de tentativas
- Opção de jogar novamente
- Interface via linha de comando
- Validação de entradas

## 📋 Pré-requisitos
- Python 3.6 ou superior instalado
- Módulos utilizados:
  - random (biblioteca padrão)

## 🔧 Como executar
1. Clone este repositório:
```bash
git clone https://github.com/Brassolotto/jogo-da-adivinhacao.git
```

2. Navegue até o diretório do projeto:
```bash
cd jogo-da-adivinhacao
```

3. Execute o programa:
```bash
python jogo_da_adivinhacao.py
```

## 📖 Como jogar
1. Digite um número entre 1 e 10
2. O jogo informará se o número é maior ou menor que seu palpite
3. Continue tentando até acertar
4. Após acertar, você pode escolher jogar novamente
5. Para sair, digite 'sair' a qualquer momento

## 🎯 Exemplo de jogada
```
Bem-vindo ao jogo da adivinhação!
Tente adivinhar o número entre 1 e 10

Digite seu palpite: 5
Dica: O número é MAIOR que isso!

Digite seu palpite: 8
Dica: O número é MENOR que isso!

Digite seu palpite: 7
Parabéns! Você acertou em 3 tentativas!
```

## ⚠️ Tratamento de Erros
- Validação de entrada numérica
- Verificação de números fora do intervalo
- Tratamento de comandos especiais
- Proteção contra entradas inválidas

## 🔍 Estrutura do Código
```
jogo_adivinhacao.py
├── Função jogar_adivinhacao()
├── Função main()
└── Sistema de controle de jogo
```

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Melhorias Futuras
- [ ] Adicionar diferentes níveis de dificuldade
- [ ] Implementar sistema de pontuação
- [ ] Adicionar limite de tentativas
- [ ] Criar ranking de jogadores
- [ ] Salvar histórico de partidas
- [ ] Interface gráfica

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por Rick Brassolotto 😊