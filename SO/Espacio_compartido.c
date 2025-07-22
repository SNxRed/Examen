#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>  // Biblioteca para manejo de hilos
#include <unistd.h>   // Biblioteca para funciones POSIX (en este caso no se usa)

// Declaración de un mutex para sincronización entre hilos
pthread_mutex_t fill_mutex;
// Arreglo de 10 enteros que será compartido entre hilos
int arr[10];
// Bandera para indicar cuando el arreglo ha sido llenado
int flag = 0;
// Variable de condición para sincronizar los hilos
pthread_cond_t cond_var = PTHREAD_COND_INITIALIZER;

// Función que será ejecutada por el primer hilo (llenar el arreglo)
void *llenar() {
    int i = 0;
    printf("\n Ingrese valores \n");
    // Solicita al usuario que ingrese 4 valores
    for (i = 0; i < 4; i++) {
        scanf("%d", &arr[i]);
    }
    
    // Bloquea el mutex antes de modificar la bandera compartida
    pthread_mutex_lock(&fill_mutex);
    flag = 1;  // Indica que el arreglo ha sido llenado
    pthread_cond_signal(&cond_var);  // Notifica a los hilos que esperan esta condición
    pthread_mutex_unlock(&fill_mutex);  // Desbloquea el mutex
    
    return NULL;    
}

// Función que será ejecutada por el segundo hilo (leer el arreglo)
void *leer() {
    int i = 0;
    // Bloquea el mutex para verificar la condición
    pthread_mutex_lock(&fill_mutex);
    
    // Espera mientras la bandera no esté activada (arreglo no llenado)
    while (!flag) {
        // Libera el mutex y espera la señal (evita condiciones de carrera)
        pthread_cond_wait(&cond_var, &fill_mutex);
    }
    pthread_mutex_unlock(&fill_mutex);  // Desbloquea el mutex
    
    // Imprime los valores del arreglo
    printf("\n Valores ingresados: \n");
    for (i = 0; i < 4; i++) {
        printf("%d ", arr[i]);    
    }
    
    pthread_exit(NULL);  // Termina el hilo explícitamente
}

int main() {
    pthread_t thread1, thread2;  // Variables para los identificadores de hilo
    int ret;  // Variable para almacenar resultados de funciones
    void *res;  // Variable para almacenar resultados de hilos

    // Inicializa el mutex
    pthread_mutex_init(&fill_mutex, NULL);

    // Crea el primer hilo que ejecutará la función llenar()
    ret = pthread_create(&thread1, NULL, llenar, NULL);
    if (ret != 0) {
        perror("Error al crear thread1");
        exit(EXIT_FAILURE);
    }
    
    // Crea el segundo hilo que ejecutará la función leer()
    ret = pthread_create(&thread2, NULL, leer, NULL);
    if (ret != 0) {
        perror("Error al crear thread2");
        exit(EXIT_FAILURE);
    }

    printf("\n Hilos creados \n");

    // Espera a que ambos hilos terminen su ejecución
    pthread_join(thread1, &res);
    pthread_join(thread2, &res);

    // Destruye el mutex para liberar recursos
    pthread_mutex_destroy(&fill_mutex);
    
    return 0;  // Fin del programa
}