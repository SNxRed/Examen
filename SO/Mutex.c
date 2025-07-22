#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h> 

// Declaración de variables globales
pthread_t tid[2];       // Array para almacenar los identificadores de 2 hilos
int counter;            // Variable contador compartida entre hilos
pthread_mutex_t lock;   // Mutex para sincronización de hilos

// Función que ejecutará cada hilo
void* funcionThread() {
    // Bloqueamos el mutex para asegurar acceso exclusivo a la sección crítica
    pthread_mutex_lock(&lock);
    
    unsigned long i = 0;
    counter += 1;  // Incrementamos el contador compartido
    
    // Imprimimos mensaje de inicio (NOTA: hay un error aquí, debería ser comillas dobles)
    printf('\n Inicia job %d', counter);
    
    // Simulamos trabajo con un bucle vacío que consume tiempo
    for(i = 0; i < (0xFFFFFFFF); i++);
    
    // Imprimimos mensaje de finalización (mismo error con las comillas)
    printf('\n Termina job %d', counter);
    
    // Desbloqueamos el mutex para permitir que otro hilo entre
    pthread_mutex_unlock(&lock);
    
    return NULL;
}