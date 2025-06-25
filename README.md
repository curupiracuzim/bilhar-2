esse é o nosso jogo de sinuca com algumas coisas extras, como eu achei que um simplis jogo de sinuca não chamaria a atenção, decidi fazer uma homenagem a um dos memes brasileiros
mais queridos de todos os tempos, o jailson mendes, que infelizmente morreu em 2018, colocamos um site ficticio de simulação de compra, menu, regras, sobre, e algumas animações extras

a utilização dos semaforos ficou detalhadamente explicada ao final desse documento

muito obrigado professora, bom recesso!!

----------------------------------------------------------

As Threads: para o jogo não travar na hora da tacada

Quando o jogador realiza uma tacada, todas as bolas podem começar a se mover ao mesmo tempo. Esse processo envolve muitos cálculos físicos, como posição, colisões e verificação se alguma bola caiu no buraco. Se tudo isso fosse feito na thread principal do jogo, poderia causar travamentos e tornar a experiência ruim.

Para resolver isso, foi utilizada uma thread separada, responsável apenas por calcular os movimentos das bolas. Essa lógica está concentrada no método _atualizar_movimento_bolas, que cuida da movimentação, colisões entre bolas, colisões com as bordas e verificação de bolas que caem nos buracos.

Quando o jogador aplica a força na bola branca (através do método aplicar_forca_bola_branca), o programa inicia essa thread de forma independente, usando threading.Thread. Isso garante que a thread principal, que desenha a tela e trata os eventos do jogador, continue funcionando normalmente, sem travar.

Onde ver isso no código
Importação: no início do arquivo há import threading
Criação da Thread: dentro do método aplicar_forca_bola_branca

if not self.movimento_thread or not self.movimento_thread.is_alive():
    self.thread_ativa = True
    self.movimento_thread = threading.Thread(target=self._atualizar_movimento_bolas)
    self.movimento_thread.start()
    
Função da Thread: o método _atualizar_movimento_bolas executa os cálculos até que todas as bolas parem ou o jogo seja encerrado.

Os Semáforos (Locks): para evitar conflitos de acesso aos dados
Como o jogo utiliza múltiplas threads, pode acontecer de duas delas tentarem acessar a mesma estrutura de dados ao mesmo tempo. Por exemplo, uma thread pode estar atualizando a posição de uma bola enquanto outra tenta desenhá-la. Isso pode causar erros ou comportamentos inesperados.

Para evitar esse tipo de problema, foi utilizado um semáforo, ou mais precisamente, um Lock do Python (threading.Lock). O Lock funciona como um controle de acesso: apenas uma thread pode acessar a lista de bolas por vez. Quando uma thread precisa acessar ou modificar os dados, ela adquire o Lock usando with self.bolas_lock:. Assim, garantimos que as informações não sejam corrompidas por acessos simultâneos.

Onde ver isso no código?

Inicialização do Lock: no construtor da classe JogoBilhar

self.bolas_lock = threading.Lock()

Uso do Lock: aparece nos seguintes métodos

_atualizar_movimento_bolas: para proteger os dados durante a movimentação das bolas

processar_eventos: ao reposicionar a bola branca

desenhar: para garantir que o desenho seja feito com as informações corretas

Dessa forma, as threads funcionam de forma organizada e segura. O uso de threads melhora o desempenho e a fluidez do jogo, e os Locks garantem que os dados não sejam acessados de maneira insegura. Isso mostra na prática a aplicação de conceitos importantes da disciplina de Sistemas Operacionais.









