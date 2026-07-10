# Piloto — Dicionário Analógico

Piloto de 20-30 páginas para validar o fluxo de extração + verificação antes de escalar para o livro completo. Ver o plano completo e o contexto de direitos autorais em `apps/analogico/README.md`.

## Como rodar

1. **Renderizar páginas do PDF em imagens:**
   ```
   cd apps/analogico/backend-python
   python -m src.pdf_to_images /caminho/para/dicionario.pdf ../pilot/data/pages --start 10 --end 39
   ```
   (`--start`/`--end` são índices 0-based no PDF, não o número impresso na página.)

2. **Extrair os verbetes de cada página** seguindo `apps/analogico/backend-python/EXTRACTION_GUIDE.md` — uma sessão do Claude Code lê cada imagem e grava `pilot/data/extracted/page-XXXX.json`.

3. **Consolidar e validar:**
   ```
   python -m src.merge_entries ../pilot/data/extracted ../pilot/data/index.json --schema schema/entry.schema.json
   python -m src.validate_index ../pilot/data/index.json ../pilot/data --schema schema/entry.schema.json
   ```

4. **Abrir o viewer** (precisa de um servidor local por causa de CORS no `fetch` de arquivos locais):
   ```
   cd apps/analogico/pilot
   python -m http.server 8000
   ```
   Abra `http://localhost:8000/viewer.html`, busque por palavra/conceito, compare o texto extraído com a imagem da página, e marque verbetes como verificados/sinalizados.

5. **Aplicar as verificações de volta aos dados:** no viewer, clique em "Exportar patch de verificação" para baixar `verification-patch.json`, depois:
   ```
   cd apps/analogico/backend-python
   python -m src.apply_verification ../pilot/data/index.json ~/Downloads/verification-patch.json
   ```

## Checklist de qualidade antes de escalar

- `validate_index.py` passa sem erros.
- Amostragem manual de pelo menos ~15 verbetes (ou ~10% do total, o que for maior) comparados com a imagem da página original.
- A taxa de verbetes sinalizados (`flagged`) na amostragem é o sinal real de confiabilidade da extração — não uma alegação de precisão do pipeline.
- Busca testada com e sem acentuação, e por substring parcial.

## Limitação conhecida

Verbetes do tipo `index` costumam referenciar uma categoria/ideia que provavelmente está fora do intervalo de páginas deste piloto. Isso é esperado e não é um bug — só faz sentido resolver ao processar o livro completo.
