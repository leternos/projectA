# analogico

Ferramenta de consulta ao **Dicionário Analógico da Língua Portuguesa** (thesaurus organizado por ideias/conceitos, não ordem alfabética), para uso como referência ao redigir documentos jurídicos.

- `backend-python/` — pipeline de extração: PDF → imagens de página → verbetes estruturados (`schema/`, `EXTRACTION_GUIDE.md`)
- `pilot/` — piloto de 20-30 páginas: app HTML (`viewer.html`) para buscar verbetes e verificar o texto extraído lado a lado com a imagem da página original
- `frontend-ts/` — scaffold reservado para uma versão com build/backend real, caso o piloto escale para o livro completo (não usado pelo piloto)

## Nota sobre confiabilidade da extração

Nenhum OCR ou leitura por visão é garantidamente 100% precisa. Por isso a extração aqui prioriza **rastreabilidade e verificação humana** em vez de uma alegação de precisão: cada verbete extraído carrega uma referência à imagem da página original, e incertezas de transcrição são registradas explicitamente (`extraction_notes`) em vez de omitidas. Verbetes não devem ser tratados como definitivos até serem verificados manualmente no viewer.

## Nota sobre direitos autorais

O texto original (Francisco Ferreira dos Santos Azevedo, autor falecido em 1942) está em domínio público no Brasil desde 2013. A edição em PDF usada como fonte, porém, pode ser uma versão expandida mais recente com conteúdo editorial adicional de status incerto — por isso os dados derivados (imagens de página, verbetes extraídos) não são commitados neste repositório (`apps/analogico/pilot/data/` está no `.gitignore`), apenas o código do pipeline.
