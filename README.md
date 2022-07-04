# pruebaTecnica

1-Para correr el programa se necesita previamente instalar XAMPP

crear una base de datos de nombre "ptecnica" e introducir en su SQL la siguiente linea de codigo para crear la tabla:

CREATE TABLE `ptecnica`.`adsf` (`id` INT NOT NULL AUTO_INCREMENT , `email` VARCHAR(50) NOT NULL , `edad` INT(3) NOT NULL , `sexo` VARCHAR(5) NOT NULL , `fav` CHAR(20) NOT NULL , `fb` INT(25) NOT NULL , `ws` INT(25) NOT NULL , `tw` INT(25) NOT NULL , `ig` INT(25) NOT NULL , `tt` INT(25) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;


2-En la carpeta donde se se guardo los archivos del repositorio de ghitHub. Se debe abrir una consola con el mismo directorio y ejecutar el siguiente comando(previamente se debe tener instalado python):

python -m venv venv

Para generar el entorno virtual y luego entrar en el con el siguiente comando

venv\Scripts\activate

Ya dentro del entorno virtual se ejecutaran los siguientes comandos

python.exe -m pip install --upgrade pip

pip install flask

pip install flask_mysqldb

pip install flask_cors

set FLASK_APP=src/app

flask run

Este ultimo activa el localhost de flask

3- Luego de ejecutar flask, se debe activar el localhost de XAMPP, tambien el de angular. Este ultimo se activa abriendo otra consola, usando este comando (previamente hay que entrar en la carpeta de angular/client desde cmd):

ng serve

Listo, la aplicacion se estara ejecutando en localhost:4200/encuesta

