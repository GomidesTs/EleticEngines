# EleticEngines
![SoonEletricEngines](https://github.com/GomidesTs/EleticEngines/blob/master/eletric_engines/static/img/logo1.png)

## Estagio do projeto
O mesmo se encontra em construção.

## Objetivo
Este projeto foi desenvolvido com objetivo da Digitalização de uma empresa do ramo prestação de serviço em manutenção de motores elétricos.

## Instalação local
Para executar o projeto, será necessário instalar os seguintes programas e dependências:

* Python 3.8.5
* pip3.8
* Django==3.0.5
* django-braces==1.14.0
* django-crispy==1.8.1
* djongo==1.3.3
* dnspython==2.0.0
* PyGObject==3.36.1
* pymongo==3.11.0
* virtualenv==20.0.31

### 
Aplicações extras necessárias

Para executar o projeto é necessário possuir uma conta no MongoDB Atlas, que pode ser obtida em https://www.mongodb.com/cloud/atlas

Sendo necessário a criação de uma nova Create a New Cluster.
Utilizando este pequeno tutorial fica mais fácil sua criação e configuração:

**Integrating MongoDB Atlas with Django using Djongo**
Escrito por **Hrithvik Sood**\
disponivel em:
https://medium.com/@hrithviksood1/integrating-mongodb-atlas-with-django-using-djongo-962dfd1513eb

Necessário atualizar seus dados na secção DATABASSES do arquivo setting.py

```
DATABASE = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
           "name": <your_database_name>,
           "host": <your_connection_string>,
           "username": <your_database_username>,
           "password": <your_database_password>,
           "authMechanism": "SCRAM-SHA-1",
        }, 
    }
}
```
## Banco de dados

Para execução do projeto fora utilizado banco de dados NoSQL,adotado MongoDB, que é orientado a documentos livre, utilizando documentos semelhantes a JSON com esquemas. É desenvolvido pela MongoDB Inc.

O mongoDB pode ser encontrado em: https://www.mongodb.com/

Possuindo umm grande documentação que esta disponivel: https://docs.mongodb.com/


## Templates

O Bootstrap foi adotado para estilizar os templates, o mesmo trata-se de é um framework web com código-fonte aberto para desenvolvimento de componentes de interface e front-end.
Possuindo uma ampla documentação na página oficial: https://getbootstrap.com/

## Projeto desenvolvido por:
Tulio Gomides 

gomidestulio5@gmail.com

https://www.linkedin.com/in/tulio-gomides-3b21b7171/