# 🚀 Projeto de IA

Este repositório contém um projeto de Inteligência Artificial que utiliza um ambiente virtual Python e depende de algumas bibliotecas específicas.

## 📌 Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto corretamente.

### 1️⃣ Criar e ativar um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**Mac/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Instalar dependências

Após ativar o ambiente virtual, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 3️⃣ Criar o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API da IA escolhida:

```
API_KEY=SUA_CHAVE_AQUI
```

### 4️⃣ Executar o projeto

Agora você pode rodar o projeto normalmente:

```bash
python main.py
```

## 🎯 Observação

- Sempre ative o ambiente virtual antes de rodar o projeto.
- O arquivo `.env` **não** deve ser versionado para evitar vazamento de credenciais.

---

💡 *Dúvidas ou sugestões? Fique à vontade para contribuir!* 🚀

