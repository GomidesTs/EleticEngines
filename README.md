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
* virtualenv
* appdirs==1.4.4
* application-utility==1.3.2
* asgiref==3.2.10
* btrfsutil==1.2.0
* CacheControl==0.12.6
* ceph-volume==1.0.0
* cephfs==2.0.0
* cephfs-shell==0.0.1
* chardet==3.0.4
* colorama==0.4.3
* contextlib2==0.6.0.post1
* distlib==0.3.1
* distro==1.5.0
* Django==3.0.5
* django-braces==1.14.0
* django-crispy==1.8.1
* djongo==1.3.3
* dnspython==2.0.0
* docopt==0.6.2
* filelock==3.0.12
* gufw==20.4.0
* html5lib==1.1
* idna==2.10
* keyutils==0.6
* lightdm-gtk-greeter-settings==1.2.2
* menulibre==2.2.1
* msgpack==1.0.0
* mugshot==0.4.2
* npyscreen==4.10.5
* ordered-set==4.0.2
* packaging==20.4
* pacman-mirrors==4.16.4
* pep517==0.8.2
* pexpect==4.8.0
* Pillow==7.2.0
* progress==1.5
* psutil==5.7.2
* ptyprocess==0.6.0
* pycairo==1.19.1
* PyGObject==3.36.1
* pymongo==3.11.0
* pyparsing==2.4.7
* PyQt5==5.15.0
* PyQt5-sip==12.8.1
* python-distutils-extra==2.39
* pytz==2020.1
* pyxdg==0.26
* PyYAML==5.3.1
* rados==2.0.0
* rbd==2.0.0
* requests==2.24.0
* resolvelib==0.4.0
* retrying==1.3.3
* rgw==2.0.0
* sip==4.19.24
* six==1.15.0
* sqlparse==0.2.4
* team==1.0
* toml==0.10.1
* udiskie==2.2.0
* ufw==0.36
* urllib3==1.25.10
* virtualenv==20.0.31
* webencodings==0.5.1

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