#include <stdio.h>       // Para funciones de entrada/salida como printf
#include <stdlib.h>      // Para funciones generales como exit
#include <pthread.h>     // Para el manejo de hilos POSIX
#include <semaphore.h>   // Para el uso de semáforos
#include <unistd.h>     // Para llamadas al sistema como sleep

sem_t mutex;  // Declaración de un semáforo llamado mutex para controlar el acceso a la sección crítica

void* thread(void* arg) {  // Función que ejecutará cada hilo (corregido el parámetro void* arg)
    // Operación wait (P) - Intenta adquirir el semáforo
    sem_wait(&mutex);
    printf("\nEntro en la SC\n");  // Mensaje indicando que entró a la sección crítica

    // Sección crítica - Código que solo puede ejecutar un hilo a la vez
    printf("\nDuermo\n");    // Mensaje antes de dormir (corregido comillas dobles)
    sleep(4);                // Simula trabajo en la sección crítica (4 segundos)
    printf("\n buenos dias\n");  // Mensaje después de despertar (corregido comillas dobles)

    // Operación signal (V) - Libera el semáforo
    printf("\nSalgo de la SC\n");  // Mensaje indicando que sale de la sección crítica
    sem_post(&mutex);              // Libera el semáforo para que otro hilo pueda entrar
    
    return NULL;  // Retorno necesario para la función del hilo (añadido)
}

int main() {
    // Inicialización del semáforo:
    // - &mutex: dirección del semáforo
    // - 0: indica que el semáforo es para hilos del mismo proceso
    // - 1: valor inicial del semáforo (1 permite que un hilo entre)
    sem_init(&mutex, 0, 1);

    pthread_t t1, t2;  // Variables para almacenar los identificadores de los hilos

    // Creación del primer hilo:
    // - &t1: dirección donde se guardará el ID del hilo
    // - NULL: atributos por defecto
    // - thread: función que ejecutará el hilo
    // - NULL: argumentos para la función (ninguno en este caso)
    pthread_create(&t1, NULL, thread, NULL);
    
    sleep(2);  // Espera 2 segundos antes de crear el segundo hilo (para demostración)

    // Creación del segundo hilo (mismos parámetros que el primero)
    pthread_create(&t2, NULL, thread, NULL);
     
    // Espera a que ambos hilos terminen su ejecución:
    pthread_join(t1, NULL);  // Espera al hilo t1
    pthread_join(t2, NULL);  // Espera al hilo t2

    sem_destroy(&mutex);  // Destruye el semáforo liberando recursos

    return 0;  // Fin del programa
}