# 💬 Relatório de Feedback e Melhorias

[cite_start]Este documento registra o feedback (simulado) recebido dos bibliotecários e as ações tomadas para incorporá-lo ao projeto, conforme solicitado.

---

### Feedback Recebido (Simulação)

* **Feedback 1:** "O sistema é muito útil! Mas quando digito o caminho do arquivo para adicionar, às vezes eu erro e o programa mostra um erro estranho e 'quebra'."
* **Feedback 2:** "Adorei a organização por tipo e ano. Seria possível, no futuro, uma função de *buscar* um arquivo pelo nome?"

---

### Ações Incorporadas ao Projeto

* **Ação (Feedback 1):** O código das funções `adicionar_documento`, `renomear_documento` e `remover_documento` foi revisado e colocado dentro de blocos `try...except`.
* **Melhoria:** O sistema agora verifica ativamente se o arquivo de origem existe (`os.path.exists`) antes de tentar copiá-lo. Se o arquivo não for encontrado, o sistema exibe uma mensagem de erro clara (ex: "Erro: O arquivo ... não foi encontrado.") em vez de "quebrar" e parar o programa. Esta melhoria já está no código `gerenciador.py`.

* **Ação (Feedback 2):** O feedback sobre a função de "Busca" foi anotado. Esta é uma excelente sugestão para a "Versão 2.0" do sistema, que pode ser implementada em um ciclo de desenvolvimento futuro.