# Roteiro de extração por visão

Este roteiro é executado por uma sessão do Claude Code, uma página por vez, lendo a imagem diretamente (não é um script automatizado). O objetivo é priorizar rastreabilidade e honestidade sobre incerteza em vez de automação pura — ver a nota de contexto no README do piloto.

## Pré-requisito

Rode `src/pdf_to_images.py` primeiro para gerar `apps/analogico/pilot/data/pages/page-XXXX.jpg`.

## Passo a passo, por página

1. Leia a imagem `pages/page-XXXX.jpg` com o Read tool (visão).
2. Identifique cada verbete na página. Um verbete é tipicamente:
   - **`index`**: uma entrada do índice alfabético remissivo, geralmente uma palavra seguida de uma referência (número de ideia, "V. outro-termo", etc.) — sem definição própria.
   - **`category`**: um bloco temático/ideia, com uma palavra-chave e uma lista de termos relacionados agrupados por analogia de sentido.
   - **`unknown`**: qualquer coisa que não se encaixe claramente nos dois tipos acima (cabeçalho de seção, nota editorial, etc.) — não force a classificação.
3. Para cada verbete, preencha o schema (`schema/entry.schema.json`):
   - `id`: `slug(headword)-p{pdf_page_index:04d}-{seq:02d}` (seq = ordem do verbete na página, começando em 01).
   - `headword`: como transcrito, preservando acentuação e capitalização originais.
   - `raw_text`: transcrição literal do verbete completo.
   - `references` / `related_terms`: conforme o tipo do verbete (nulo se não aplicável).
   - `pdf_page_index`: o índice da página (mesmo número do nome do arquivo da imagem).
   - `printed_page_number`: o número impresso na página, se legível (pode ser romano ou nulo).
   - `page_image`: `pages/page-XXXX.jpg`.
   - `verification_status`: sempre `"unverified"` nesta etapa — a verificação é manual, feita depois no viewer.
   - `verified_by`, `verified_at`: sempre `null` nesta etapa.
   - `extraction_notes`: **obrigatório preencher quando houver qualquer incerteza** — mancha, borrão, página torta, fonte ilegível, corte na margem, dúvida sobre separação de verbetes. Nunca adivinhe silenciosamente; registre a dúvida aqui em vez de omiti-la.

4. Grave o array de verbetes da página em `pilot/data/extracted/page-XXXX.json`.

## Regra de ouro

Se não tiver certeza do que está escrito, **não invente**. Transcreva o que for legível, marque o restante como incerto em `extraction_notes`, e deixe a verificação humana (via `viewer.html`, comparando com a imagem da página) resolver a dúvida. Um verbete com nota de incerteza é muito mais seguro do que um verbete "limpo" mas errado — especialmente dado que isso será usado como referência para redigir documentos jurídicos.

## Depois de extrair todas as páginas

Rode `src/merge_entries.py` para consolidar `extracted/page-*.json` em `pilot/data/index.json`, validando contra o schema. Depois rode `src/validate_index.py` para as checagens de integridade (verbetes duplicados, imagens de página órfãs, etc.) antes de considerar o piloto pronto para amostragem manual.
