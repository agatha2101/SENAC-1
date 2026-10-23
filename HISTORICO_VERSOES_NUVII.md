# Nuvii — Histórico de versões do Mascot Playground

**Versão aprovada como final:** `Nuvii_Mascot_Playground_FINAL.html`  
**Data de consolidação:** 23/10/2026  
**Escopo:** playground isolado do mascote. O front-end principal e o backend do Nuvii não fazem parte destas alterações.

> Este histórico foi reconstruído a partir das versões e decisões registradas na conversa. Alguns arquivos intermediários foram entregues como ZIPs e outros como HTML único; por isso, a sequência abaixo registra as mudanças solicitadas e as versões identificáveis, sem afirmar que cada tentativa intermediária representa uma versão visual aprovada.

## Linha do tempo

### V1 — Playground inicial
- Criação de uma página isolada para experimentar o mascote sem alterar o aplicativo principal.
- Base visual com cabeça branca arredondada, visor turquesa, olhos expressivos, braços laterais e fundo claro.
- Primeiras animações de flutuação e controles para alternar estados.

### V2 — Primeira evolução do playground
- Iteração de estrutura e apresentação do playground.
- Arquivo registrado: `Nuvii_Mascot_Playground_v2.zip`.
- Esta versão foi uma etapa de exploração; não é a versão final aprovada.

### V3 — Base escolhida para refinamentos
- A V3 foi escolhida como base para os ajustes seguintes do mascote.
- Foram testadas aproximações dos olhos e diversas posições dos braços.
- Arquivo-base registrado: `Nuvii_Mascot_Playground_v3.zip`.

### V3 — Ajuste de distância dos olhos
- Os olhos foram aproximados levemente, preservando o formato geral do rosto.
- Arquivo registrado: `Nuvii_Mascot_Playground_v3_olhos_mais_proximos.zip`.

### V3 — Refinamento dos braços
- Ajustes na posição dos braços para que ficassem próximos ao corpo, mas separados durante o repouso.
- Foi reforçada a regra de que os braços só devem tocar o rosto durante a animação de tampar os olhos.
- Arquivos de iteração registrados: `Nuvii_Mascot_Playground_v3_bracos_ajustados.zip` e `Nuvii_Mascot_Playground_v3_bracos_sem_contato.zip`.

### V3 — Braços associados às expressões
- **Curioso:** um braço próximo à boca, sem cobri-la.
- **Preciso entender melhor / concentrado:** experimentos de posicionamento dos braços na região superior da cabeça; após revisões, essa posição foi descartada para a versão final.
- **Triste:** inclusão de lágrima e refinamento das sobrancelhas e dos olhos.
- Arquivo registrado: `Nuvii_Mascot_Playground_v3_bracos_emocoes.zip`.

### V3 — Aceno, conquista e tristeza
- **Boas-vindas:** aceno com trajetória para cima, em vez de um movimento que parecesse baixar o braço.
- **Conquista:** proposta de uma pequena dança, com a cabeça acompanhando o movimento dos braços.
- **Triste:** sobrancelhas levemente curvadas e olhos um pouco fechados para transmitir tristeza sem parecer raiva.
- Arquivo registrado: `Nuvii_Mascot_Playground_v3_aceno_dancinha_triste.zip`.

### V3 — Pensando e concentrado
- **Pensando:** inclusão de uma fumacinha acima da cabeça.
- **Concentrado:** olhos levemente fechados e experimentos com as mãos próximas à parte superior da cabeça.
- Depois, a posição das mãos foi alterada conforme a orientação do usuário.
- Arquivo registrado: `Nuvii_Mascot_Playground_v3_concentrado_pensando_dancinha.zip`.

### V4, V5 e V6 — Explorações alternativas
- Foram geradas versões de exploração para avaliar variações visuais e expressões.
- Arquivos registrados: `Nuvii_Mascot_Playground_v4.zip`, `Nuvii_Mascot_Playground_v5.zip` e `Nuvii_Mascot_Playground_v6.zip`.
- Essas versões não substituem a base V3 escolhida para os refinamentos finais.

### HTML — Expressões refinadas
- **Neutro:** leve sorriso de boca fechada.
- **Concentrado:** mãos reposicionadas ao lado do corpo e olhos levemente fechados.
- **Feliz:** olhos fechados para expressar uma comemoração muito alegre.
- **Braços:** aproximação geral dos braços ao corpo, mantendo uma pequena separação visual quando não estão encostando nele.
- Arquivos de iteração registrados: `Nuvii_Mascot_Playground_atualizado.html`, `Nuvii_Mascot_Playground_concentrado_ajustado.html`, `Nuvii_Mascot_Playground_concentrado_mais_proximo.html` e `Nuvii_Mascot_Playground_bracos_felizes_ajustados.html`.

## Versão final aprovada

Arquivo canônico: **`Nuvii_Mascot_Playground_FINAL.html`**

A última decisão aprovada pelo usuário foi:
- Manter os dois braços da expressão **Concentrado ao lado do corpo** — não na cabeça.
- Manter os olhos do estado **Concentrado levemente fechados**.
- No estado **Feliz**, fechar os olhos para demonstrar alegria intensa.
- Manter os braços em geral um pouco mais próximos do corpo, sem contato constante; o contato com o rosto é reservado à expressão **Tampar os olhos**.
- Preservar as demais expressões e animações do playground.

## Estados e comportamentos planejados no playground

- **Neutro/repouso:** posição relaxada e sorriso discreto fechado.
- **Boas-vindas:** um braço acena para cima e depois retorna à posição de repouso.
- **Curioso:** um braço se aproxima da boca, sem cobri-la.
- **Conquista:** pequena dança com movimento sincronizado da cabeça e dos braços.
- **Pensando:** fumacinha animada acima da cabeça.
- **Concentrado:** olhos levemente fechados e braços ao lado do corpo.
- **Triste:** sobrancelhas suaves, olhos parcialmente fechados e lágrima.
- **Feliz:** olhos fechados e braços em gesto comemorativo.
- **Confuso, explicando e surpreso:** expressões próprias para cada estado.
- **Tampar os olhos:** única expressão em que os braços se aproximam e cobrem a região dos olhos.

## Observações de manutenção

1. `Nuvii_Mascot_Playground_FINAL.html` é a cópia de referência aprovada e deve ser preservada como versão final.
2. Para mudanças futuras, criar uma nova cópia versionada antes de editar o arquivo final.
3. Este projeto é um playground visual independente; não representa integração com o front-end principal nem com o backend.
4. O histórico documenta as solicitações e os arquivos identificados na conversa. Nem todas as versões intermediárias foram validadas por captura real de navegador.
