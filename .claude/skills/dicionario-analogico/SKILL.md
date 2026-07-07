---
name: dicionario-analogico
description: Consultar o Dicionário Analógico da Língua Portuguesa (Francisco Ferreira dos Santos Azevedo, método Roget). Use quando o usuário escreve, revisa, traduz ou compõe em português e precisa encontrar a palavra exata para uma ideia que consegue descrever mas não consegue nomear ("a palavra na ponta da língua"), quer sinônimos com nuance semântica fina, ou está explorando vocabulário por vizinhança conceitual — em prosa, poesia, letra de canção, palavras cruzadas, tradução literária, ou escolha estilística. Também use quando o usuário mencionar explicitamente "dicionário analógico", "thesaurus", "ideias afins", "palavras análogas", "sinônimo de", "qual a palavra para", "outra forma de dizer", ou pedir para achar uma palavra "mais precisa" / "mais elegante" / "mais forte" / "mais suave" em português. NÃO use para tradução para outros idiomas, definição pura de uma palavra conhecida, ou correção gramatical — para isso use um dicionário de língua comum.
---

# Dicionário Analógico da Língua Portuguesa

Método baseado em Francisco Ferreira dos Santos Azevedo, *Dicionário analógico
da língua portuguesa — ideias afins / thesaurus* (2ª edição, Lexikon), que por sua
vez adapta o método do *Thesaurus* de Peter Mark Roget para o português.

O dicionário comum vai da **palavra ao significado**. O dicionário analógico faz o
inverso: parte de um **significado ou ideia** para achar, numa nuvem de palavras
análogas, a palavra ou expressão que melhor exprime aquilo. É a ferramenta certa
quando o usuário sabe o que quer dizer mas não acha a palavra.

## Quando usar esta skill

Ative quando o pedido do usuário se encaixar em uma destas situações:

- **Palavra na ponta da língua**: descreve um conceito e pergunta "como é que
  chama aquilo que…", "qual é a palavra pra…", "tem uma palavra que significa X?"
- **Sinônimo com nuance**: já tem uma palavra mas quer uma **variação** — mais
  precisa, mais forte, mais suave, mais formal, mais coloquial, mais poética,
  menos batida, arcaica, brasileira, lusitana, técnica.
- **Exploração conceitual**: quer ver o campo semântico ao redor de uma ideia
  (por ex., escrevendo um poema sobre "solidão", quer ver todo o vocabulário
  adjacente).
- **Ideia oposta**: quer o antônimo ou contraste (o dicionário organiza pares
  antagônicos: cada grupo geralmente tem um par oposto).
- **Palavras cruzadas / jogos de palavras** em português.
- **Revisão estilística**: substituir repetições, evitar clichês, achar a palavra
  "de ouro" para um verso, letra, título.
- **Tradução para o português** onde o tradutor tem o sentido mas quer o termo
  mais idiomático ou expressivo.

Não é a ferramenta certa quando o usuário só quer:

- A **definição** de uma palavra conhecida → dicionário comum.
- **Ortografia / gramática** → revisor / gramática.
- Tradução **para outros idiomas** → tradutor.
- Etimologia → dicionário etimológico.

## O método analógico

O universo do léxico português está mapeado em **6 classes** de conceitos, que
se ramificam em **24 divisões**, dezenas de **subdivisões**, e **cerca de 1000
grupos analógicos numerados** (1 a 1000, com alguns intermediários tipo 465a).

As seis grandes classes:

| # | Classe | Grupos | Faixa |
|---|---|---|---|
| I | **Relações abstratas** | Existência, Relação, Quantidade, Ordem, Número, Tempo, Mudança, Causa | 1–179 |
| II | **Espaço** | Espaço em geral, Dimensões, Forma, Movimento | 180–315 |
| III | **Matéria** | Matéria em geral, Inorgânica, Orgânica (inclui vida, sensações, luz e som) | 316–449 |
| IV | **Entendimento** | Formação e Comunicação das ideias | 450–599 |
| V | **Vontade individual** | Vontade em geral, Vontade com referência à sociedade | 600–819 |
| VI | **Afeições** | Em geral, Pessoais, Simpáticas, Morais, Religiosas | 820–1000 |

A árvore completa está em [`references/classificacao.md`](references/classificacao.md).

**Grupos antagônicos**: quase todos os grupos vêm em par oposto. Ex.: 1 Existência ↔
2 Inexistência; 33 Superioridade ↔ 34 Inferioridade; 359 Vida ↔ 360 Morte;
836 Alegria ↔ 837 Tristeza. Se o conceito buscado tem um oposto conceitual claro,
o par está pertinho.

**Formato de um grupo**: dentro de cada grupo, as palavras estão organizadas por
classe gramatical, na sequência:

- **Substantivos** (sem rótulo — vêm primeiro)
- **V.** — Verbos
- **Adj.** — Adjetivos
- **Adv.** — Advérbios
- **FRASES:** — Frases feitas, expressões idiomáticas, provérbios

Termo seguido de número (ex.: `existir 359`) indica **remissão** para outro grupo
onde vale procurar mais analogias.

Marcadores de contexto (abreviaturas do livro): `bras.` brasileirismo, `port.`
português (de Portugal), `fam.` familiar, `pop.` popular, `pej.` pejorativo,
`iron.` irônico, `poét.` poético, `desuso`, `p. us.` pouco usado, `lit.`
literatura, `jur.` jurídico, `teol.` teologia, `mit.` mitologia, etc. Lista
completa em [`references/abreviaturas.md`](references/abreviaturas.md).

## Procedimento

Quando esta skill for ativada:

1. **Leia** [`references/metodo.md`](references/metodo.md) para calibrar o
   raciocínio analógico caso a tarefa seja complexa (poesia, escolha estilística
   fina). Para consultas rápidas, o roteiro abaixo basta.

2. **Identifique o vetor da busca**:
   - Se o usuário deu uma **ideia** ("uma palavra pra quando você espera algo
     bom acontecer") → navegue a árvore (passo 3).
   - Se o usuário deu uma **palavra** ("outra palavra pra 'saudade'") → identifique
     o(s) grupo(s) onde essa palavra provavelmente cai e siga daí.

3. **Navegue a árvore** em [`references/classificacao.md`](references/classificacao.md):
   - Escolha a Classe (I–VI) que abriga o conceito.
   - Desça para a Divisão.
   - Desça para a Subdivisão.
   - Chegue no Grupo numerado.
   - Ex.: "esperança" → Classe VI Afeições → Divisão II Pessoais → 3°) Em projeto
     → Grupo **858 Esperança** (e seu antagônico **859 Desesperança**).

4. **Gere a nuvem de palavras análogas** para esse grupo, organizada por classe
   gramatical. Duas fontes:

   a. **Se o grupo estiver entre 1 e 135**, o texto verbatim das entradas está
      em [`data/entradas-grupos-001-135.md`](data/entradas-grupos-001-135.md)
      (extraído do PDF; use como referência primária, filtrando ruído de OCR).

   b. **Se o grupo estiver entre 136 e 1000**, gere as analogias a partir do
      título do grupo e do seu conhecimento do português, seguindo a
      **granularidade e organização** do método (substantivos primeiro, depois
      V., Adj., Adv., FRASES). Marque registro (bras./port./fam./poét./desuso)
      quando relevante. Este material extraído do PDF do usuário **cobre só até
      o grupo 135**; para grupos posteriores, aplique o método por analogia com
      os grupos que temos.

5. **Ofereça também**:
   - O **grupo antagônico** ao lado, se fizer sentido para o contexto (contraste
     costuma iluminar a escolha).
   - **Remissões** para grupos vizinhos ou correlatos que o consulente talvez
     queira folhear.

6. **Formate a resposta** para leitura rápida:
   - Título do grupo (número + nome + antagônico se houver).
   - Blocos por classe gramatical.
   - Marcadores de registro entre parênteses após a palavra quando relevante.
   - No máximo 15–25 palavras por grupo — nuvem, não lista exaustiva — a menos
     que o usuário peça exaustão.

## Exemplo de resposta

**Pedido do usuário**: "Estou escrevendo uma letra e quero uma palavra pra
'esperar' que não seja tão comum — algo que soe mais poético."

**Resposta esperada**:

> No dicionário analógico, isso cai em **858 Esperança** (Classe VI Afeições,
> Divisão II Pessoais, 3°) Em projeto).
>
> **Verbos**: esperar, aguardar, ter fé, confiar, alentar, alimentar
> esperança, alvorecer no horizonte, avistar, entrever, vislumbrar, contar
> com, presumir, aspirar a, sonhar com, embalar-se em, acalentar.
>
> **Substantivos** (para nominalizar): esperança, alento, fé, confiança,
> alvorecer, presságio favorável, promessa, expectativa, esperar (subst.).
>
> Se quiser o oposto para contraste, o par antagônico é **859 Desesperança**
> (desesperar, desalentar, desanimar, dar tudo por perdido). Se a nuance for
> mais "aguardar passivo/tenso", pode ver também **507 Expectativa**.

## Notas de calibração

- **Idioma**: sempre responda em **português** (a menos que o usuário peça em
  outro idioma) — a skill é sobre léxico português.
- **Registro**: adapte-se ao registro do usuário. Se ele está escrevendo poesia,
  puxe termos poéticos e cultismos. Se está escrevendo um chat, favoreça
  coloquiais.
- **Brasil vs. Portugal**: se o usuário indicou variedade, filtre — marque
  `(bras.)` ou `(port.)` quando o termo é claramente de uma variedade.
- **Não invente** grupos ou numeração que não existam na árvore. Se a busca cai
  entre dois grupos, cite os dois.
- **Copyright**: o material verbatim em `data/` vem do PDF do usuário. Reproduza
  para o próprio usuário como consulta; não republique em massa.

## Arquivos desta skill

- `SKILL.md` — este arquivo (ponto de entrada)
- `references/metodo.md` — o método analógico em profundidade
- `references/classificacao.md` — árvore completa dos 1000 grupos
- `references/abreviaturas.md` — legenda das abreviaturas do dicionário
- `data/entradas-grupos-001-135.md` — texto verbatim dos grupos 1 a 135
  (extraído do PDF fornecido)
