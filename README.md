<p align="center">

  <h2 align="center">Infraestrutura de Comunicação - 2023.2</h2>
  <h3 align="center">Programação utilizando sockets</h3>

  <p align="center">
    Projeto de Programação utilizando sockets apresentado como requisito à obtenção de aprovação na disciplina de Infraestrutura de Comunicação do Curso de ciência da computação da Universidade Federal de Pernambuco. <br/>
    <a href="https://www.overleaf.com/2158362258mqtsmkmtdysf#94bc6c">Link do relatório</a><br>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Sumário</h2></summary>
  <ol>
    <li><a href="#">Implementação</a></li>
    <li><a href="#intrucoes">Instruções de execução</a></li>
  </ol>
</details>

<br/> 

## Implementação

Quando cada nó é instanciado, ele envia para envia uma mensagem para a autoridade
certificadora pedindo para se registrar. Quando isso acontece, a autoridade cria a chave pública e
privada e envia a chave privada de maneira criptografada utilizando o RSA. Se o PC1 quiser se
comunicar com o PC2, PC1 irá solicitar a chave pública de PC2 para poder enviar de maneira
segura a chave simétrica que foi estabelecida previamente pelo PC1. PC2 então guarda essa
chave e os dois podem trocar mensagens de maneira segura. Esse processo ocorre em todos nos
nós, resultando em 15 chaves assimetricas totais para a comunicação geral.

## Instruções de execução
<br/>
<p id="instrucoes">
  Para a execução, o usuário deve ter o Python 3 devidamente instalado, bem como uma IDE capaz de interpretá-lo.
</p>
<br/> 

1. Clone o repositório

   ```sh
   git clone https://github.com/EllianRodrigues/projeto-infracom.git
   ```

2. Abra a pasta /AC no VScode

3. Abra Barra de Menus e Ferramentas do VScode e clique em Novo Terminal

4. Execute a linha de comando:

   ```sh
   python AC.py
   ```
   Mensagens como "AC iniciado", "Chave privada enviada para o PC 1" e "Chave pública de PC 2 enviada para o PC 1" indicam êxito do processo.

6. Em seguida, execute uma linha de comando para cada um dos PCs:

   ```sh
   python PC_1.py
   ```
   . <br>
   . <br>
   . <br>
   ```sh
   python PC_6.py
   ```
   Cada execução deve enviar uma mensagem e um endereço ao PC. O usuário receberá mensagens dos outros dispositivos na rede, confirmações quando uma mensagem é enviada com sucesso e quando uma mensagem é recebida de outro dispositivo

<br/> 

## Contatos

<br/>

- ARIEL RODRIGUES - arss5@cin.ufpe.br
- ELLIAN RODRIGUES - ers2@cin.ufpe.br
- FRANCISCO GABRIEL - fglb@cin.ufpe.br
- MIGUEL OLIVEIRA - mgo@cin.ufpe.br
