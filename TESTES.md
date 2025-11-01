# 📋 Relatório de Testes do Sistema

[cite_start]Este documento registra os testes realizados para garantir que todas as funções do `gerenciador.py` operam corretamente, conforme solicitado na atividade[cite: 29].

---

### Teste 1: Execução e Listagem (Biblioteca Vazia)

* **Ação:** Executei `python gerenciador.py` e escolhi a opção "1. Listar".
* **Resultado Esperado:** O sistema deve informar que "Nenhum documento encontrado".
* **Resultado Obtido:** **[Sucesso]** O sistema exibiu "Nenhum documento encontrado na biblioteca."

---

### Teste 2: Adicionar Novo Documento

* **Ação:** Escolhi a opção "2. Adicionar".
    * Usei um arquivo local (ex: `C:/temp/meu_artigo.pdf`).
    * Informei o tipo: `ARTIGO`
    * Informei o ano: `2024`
* [cite_start]**Resultado Esperado:** O sistema deve copiar o arquivo para `biblioteca/ARTIGO/2024/meu_artigo.pdf`[cite: 23].
* **Resultado Obtido:** **[Sucesso]** O sistema criou as pastas e exibiu a mensagem: "Sucesso: Arquivo 'meu_artigo.pdf' adicionado em 'biblioteca/ARTIGO/2024'."

---

### Teste 3: Listar Documento Adicionado

* **Ação:** Escolhi a opção "1. Listar" novamente.
* **Resultado Esperado:** O sistema deve mostrar o arquivo adicionado na sua estrutura de pastas.
* **Resultado Obtido:** **[Sucesso]** O sistema listou:
    ```
    [Pasta: biblioteca/ARTIGO/2024]
      - meu_artigo.pdf
    ```

---

### Teste 4: Renomear Documento

* [cite_start]**Ação:** Escolhi a opção "3. Renomear"[cite: 24].
    * Caminho antigo: `ARTIGO/2024/meu_artigo.pdf`
    * Novo nome: `artigo_final.pdf`
* **Resultado Esperado:** O arquivo deve ser renomeado dentro da sua pasta.
* **Resultado Obtido:** **[Sucesso]** O sistema exibiu: "Sucesso: Arquivo renomeado para 'biblioteca/ARTIGO/2024/artigo_final.pdf'."

---

### Teste 5: Remover Documento

* [cite_start]**Ação:** Escolhi a opção "4. Remover"[cite: 24].
    * Caminho: `ARTIGO/2024/artigo_final.pdf`
    * Confirmação: `s`
* **Resultado Esperado:** O arquivo deve ser apagado.
* **Resultado Obtido:** **[Sucesso]** O sistema exibiu: "Sucesso: Arquivo removido."