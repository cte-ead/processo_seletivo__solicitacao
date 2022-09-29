# Solicitação de processo seltivo

Descrever o que o sistema faz.

> Neste projeto usamos o [Docker](https://docs.docker.com/engine/install/) e o [Docker Compose Plugin](https://docs.docker.com/compose/install/compose-plugin/#:~:text=%20Install%20the%20plugin%20manually%20%F0%9F%94%97%20%201,of%20Compose%20you%20want%20to%20use.%20More%20) (não o [docker-compose](https://docs.docker.com/compose/install/) 😎). O setup foi todo testado usando o Linux.


## Como funciona

Descrever isso aqui também.

## Como iniciar o desenvolvimento

```bash
# Baixe o projeto
git clone git@github.com:cte-zl-ifrn/processo_seletivo__solicitacao.git processo_seletivo__solicitacao

cd processo_seletivo__solicitacao

# Instala o sistema
_/deploy
```

> O **portal** estará disponível em http://localhost:8000/, o primeiro usuário a acessar será declarado como superusuário e poderá fazer tudo no sistema.

> O **SUAP Fake** estará disponível em http://localhost:8001/, o primeiro usuário a acessar será declarado como superusuário e poderá fazer tudo no sistema.

> O **AVA ZL** estará disponível em http://localhost:8011/, o usuário/senha do administrador serão admin/admin.

> O **AVA Presencial** estará disponível em http://localhost:8021/, o usuário/senha do administrador serão admin/admin.

Caso você deseje fazer debug da AVA-Portal, tente:

```bash
_/portalapp/down
_/portalapp/debug
```


## Tipo de commits

- `feat:` novas funcionalidades.
- `fix:` correção de bugs.
- `refactor:` refatoração ou performances (sem impacto em lógica).
- `style:` estilo ou formatação de código (sem impacto em lógica).
- `test:` testes.
- `doc:` documentação no código ou do repositório.
- `env:` CI/CD ou settings.
- `build:` build ou dependências.
