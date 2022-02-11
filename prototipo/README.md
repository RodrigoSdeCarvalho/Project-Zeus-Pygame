Nesse diretório, o grupo irá trabalhar em cima do primeiro protótipo do jogo.

A ideia do protótipo não é que ele seja uma versão demo do jogo completo, mas sim que o principal mecanismo do jogo esteja implementado com certo grau de sucesso. Exemplo: em um jogo do tipo plataforma 2D, basta mostrar um retângulo colidindo com objetos e saltando/destruindo com alguma comando do usuário. A interface gráfica (com sprites) é opcional nessa etapa.

Instruções (para iniciar):
    Para iniciar o jogo, basta executar o arquivo 'Game.py', após executado basta clicar no botão 'Play' do menu.

Instruções (para jogar):
    O jogador (bloco vermelho) se move utilizando as teclas W (cima), A (esquerda), S (baixo) e D (direita) e ataca com a tecla E. Para atacar, o personagem deve estar em frente ao inimigo (bloco azul). A tecla LSHIFT aumenta a velocidade do personagem.
    O inimigo é estático e ocasionalmente lança um poder (bloco branco) contra o jogador, que o segue durante um tempo e some. Caso o poder atinja o personagem antes de desaparecer, causa dano e some. O poder deixa de ser lançado caso o inimigo seja destruído.
    As barras de vida do jogador (Computatus) e do inimigo (Zeus) estão no topo da tela.