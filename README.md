# API GATEWAY - Componente C

Este componente centraliza os requests para os outros componentes, ele conecta ao microserviço de login e de produtos e redireciona os requests para o respectivo serviço.

## Instalação

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---

## Antes da execução

Antes de executar o projeto é necessário ter um arquivo `.env` na raiz do projeto com a seguinte estrutura:

```
LOGIN_SERVICE=http://localhost:5003
PRODUCT_SERVICE=http://localhost:5004
```

Estes valores são as rotas do serviço de login e de produtos

### Executando o servidor

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5003
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5003 --reload
```

---

### Acesso no browser

Abra o [http://localhost:5003/#/](http://localhost:5003/#/) no navegador para verificar o status da API em execução.

---

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t product-service .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5003:5003 login-service
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5003/#/](http://localhost:5003/#/) no navegador.

### Alguns comandos úteis do Docker

> **Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
> ```
> $ docker images
> ```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>
> ```
> $ docker rmi <IMAGE ID>
> ```
>
> Subistituindo o `IMAGE ID` pelo código da imagem
>
> **Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
> ```
> $ docker container ls --all
> ```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>
> ```
> $ docker stop <CONTAINER ID>
> ```
>
> Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>
> ```
> $ docker rm <CONTAINER ID>
> ```
>
> Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).
