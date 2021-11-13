# README

> En este repositorio dejo ciertas notas, a modo de notas de referencias de docker y/o podman.
> Salvo que se indique expresamente, en este repositorio se utiliza principalmente Podman.

## Mover contenedor a otro servidor

**Caso de uso:** Mover contenedor desde el servidor ***A*** al servidor ***B***

Se puede realizar siguiendo la secuencia:

_En el servidor **A**, ejecuto:_

1. `podman ps` (ver los contenedores que están en ejecución).
2. `podman commit -p <ID_CONTAINER> <NAME_IMAGE>` (se crea imagen del contenedor a ser transferido).
3. `podman images` (se verifica que se ha creado la imagen).
4) `podman save -o <PATH>/<NAME_IMAGE>.tar <NAME_IMAGE>` (Se hace un tar del contenedor a transferir).

_En el servidor **B**_

1. `<PATH>/<NAME_IMAGE>.tar` (es copiado a ***B***, donde sera restaurado).
2. `podman load -i <PATH>/<NAME_IMAGE>.tar` (se carga la imagen)
1. `podman images` (se revisa que la imagen que este disponible en ***B***)