# Criptography Proyect

Nuestra aplicación (Alfa) va a estar inspirada en Sigma, la aplicación de la universidad. Alfa se va a centrar en el 
registro de alumnos dentro del marco de la base de datos de la Universidad Carlos III de Madrid a través de un 
formulario donde introducirán sus datos personales y bancarios, y se les aplicará el cobro de la matrícula correspondiente.

## Cifrado simétrico

Para cifrar datos personales menos comprometidos como la fecha de nacimiento, las asignaturas que cursa, hemos pensado 
que con el objetivo de beneficiarse de la alta velocidad, es mejor utilizar un cifrado simétrico como pueda ser AES 
(Advanced Encryption Standard)para así también aprovecharse de su fácil implementación. 

## Cifrado asimétrico

Para la parte de contenido sensible como las contraseñas, números de cuenta demás o datos comprometidos hemos decidido 
utilizar el método de cifrado asimétrico RSA (Rivest Shamir Adleman) con el objetivo de aprovechar sus características 
claves públicas y claves privadas para así poder evitar la transmisión de los datos sensibles a través del canal inseguro. 
De esta forma nos aseguraremos de que funciones tan delicadas como las transacciones sean hechas de manera fiable.

## Firma digital

Como la firma digital es la transformación (mediante técnicas criptográficas) de un documento que permite probar su 
autoría e integridad, se puede usar como comprobante de pago de la matrícula o la propia matrícula en sí.

## Funciones HASH y HMAC

El sistema debe comprobar previamente que el usuario y la contraseña introducidas son correctas para poder acceder al 
servicio. Para que exista un mayor nivel de seguridad, el sistema no guarda la contraseña, sino que guarda el hash de la 
contraseña. Y, por tanto, cuando introducimos nuestra contraseña para acceder, el sistema calcula el hash de la 
contraseña y lo compara con el guardado en el sistema. Si ambos coinciden, se permitirá el acceso.
Otra de las utilidades de las funciones Hash es determinar de forma rápida la inalterabilidad de un documento o archivo. 
Como cada documento genera un Hash único (como una matrícula de coche), si un documento ha sido alterado su hash será 
diferente al anterior. Esta misma función permite una trazabilidad de los documentos o archivos. Al tener un 
identificador único, se podrán identificar cualquier copia del documento o archivo.
