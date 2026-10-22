# 📝 Gerador de Apresentação

Um pequeno programa de terminal em Python que monta uma apresentação pessoal a partir do seu nome, idade e do que você gosta, mostra uma prévia do texto e, se você quiser, salva o resultado em um arquivo `apresentação.txt`.

## ✨ Funcionalidades

- Pergunta nome, idade e um breve comentário sobre o que você gosta
- Formata o texto automaticamente (nome com a primeira letra maiúscula, assunto em minúsculas)
- Mostra uma prévia antes de salvar
- Permite refazer o comentário até você ficar satisfeito
- Salva o texto em `apresentação.txt`, **acrescentando** novas apresentações ao final do arquivo
- Cria o arquivo automaticamente se ele ainda não existir

## 📋 Requisitos

- Python 3.6 ou superior (usa f-strings)
- Nenhuma biblioteca externa: apenas a biblioteca padrão (`time`)

## ▶️ Como usar

Execute o script:

```bash
python main.py
```

Exemplo de uso:

```
Escreva seu nome: maria
Escreva sua idade: 25
Comente brevemente sobre o que gosta: Séries e Café
Seu texto ficou assim:
 Prazer eu sou Maria, tenho 25 anos, e no geral gosto de séries e café

Gostaria de salvar? s/n
s
..
...
Texto salvo com sucesso!
```

O arquivo `apresentação.txt` passa a conter:

```
Prazer eu sou Maria, tenho 25 anos, e no geral séries e café
```

> Se responder `n` na pergunta de salvar, o programa pede o comentário novamente (nome e idade são mantidos), até você confirmar com `s`.

## ⚙️ Como funciona

1. O programa tenta abrir `apresentação.txt` em modo **append** (`"a"`), que adiciona conteúdo ao final sem apagar o que já existe.
2. Se essa abertura falhar, o bloco `except` abre o arquivo em modo **write** (`"w"`) e repete o mesmo fluxo.
3. Nome e idade são pedidos uma única vez.
4. Dentro de um laço `while True`, o programa pede o assunto, mostra a prévia e pergunta se deseja salvar.
5. Respondendo `s`, grava a linha no arquivo, exibe uma pequena animação (`..` e `...` com `time.sleep`) e encerra o laço.
6. Por fim, o arquivo é fechado com `txt.close()`.

## ⚠️ Limitações conhecidas

- Só a letra minúscula `s` confirma o salvamento: a comparação `ask == "s".lower()` converte o `"s"` fixo, não a resposta do usuário. Assim, `S` é tratado como "não".
- Qualquer resposta diferente de `s` (inclusive `n` ou um erro de digitação) simplesmente repete a pergunta do assunto.
- A idade é aceita como texto, sem validar se é um número.
- O texto salvo não inclui o "gosto de" que aparece na prévia.
- Não há codificação definida na abertura do arquivo, o que pode causar problemas com acentos em alguns sistemas (principalmente Windows).
- O bloco `except` duplica todo o código do `try`.

## 💡 Ideias de melhoria

- Usar `ask.lower() == "s"` (ou `ask.strip().lower()`) para aceitar `S` e espaços extras
- Abrir o arquivo com `open("apresentação.txt", "a", encoding="utf-8")`, que já cria o arquivo se não existir e dispensa o `try/except`
- Usar `with open(...) as txt:` para fechar o arquivo automaticamente
- Validar a idade com `idade.isdigit()`
- Deixar a opção de sair sem salvar
- Manter o mesmo texto na prévia e no arquivo

## 📄 Licença

Projeto de uso livre para estudo e aprendizado.
