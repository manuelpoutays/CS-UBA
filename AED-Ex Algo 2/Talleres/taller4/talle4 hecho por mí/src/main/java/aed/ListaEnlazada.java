package aed;

import java.util.*;

public class ListaEnlazada<T> implements Secuencia<T> {
    private Nodo cabeza;
    private Nodo cola;
    private class Nodo {
        T valor;
        Nodo siguiente;
        Nodo anterior;
        public Nodo(T v) { valor = v; }
        }

    public ListaEnlazada() {
        cabeza=cola=null;
    }

    public int longitud() {
        int longitud=0;
        Nodo actual=cabeza;
        while (actual!=null) {
            longitud++;
            actual=actual.siguiente;
        }
        return longitud;
    }

    public void agregarAdelante(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (cabeza==null) {
            cabeza=cola=nuevo;            
        }
        else{
            nuevo.siguiente=cabeza;
            cabeza.anterior=nuevo;
            cabeza=nuevo;
        }
    }

    public void agregarAtras(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (cabeza==null) {
            cabeza=cola=nuevo;            
        }
        else{
            cola.siguiente=nuevo;
            nuevo.anterior=cola;
            cola=nuevo;
        }
    }

    public T obtener(int i) {
        Nodo actual=cabeza;
        int contador=0;
        while (contador<i) {
            actual=actual.siguiente;
            contador++;
        }
        return actual.valor;
    }

    public void eliminar(int i) {
        Nodo actual=cabeza;
        int contador=0;
        while (contador<i) {
            actual=actual.siguiente;
            contador++;
        }
        if (actual == cabeza) {
            cabeza = cabeza.siguiente;
            if (cabeza != null) {
                cabeza.anterior = null;}
        } else if (actual == cola) {
            cola = cola.anterior;
            if (cola != null) {
                cola.siguiente = null;
            } 
        }
        else {
            actual.anterior.siguiente=actual.siguiente;
            actual.siguiente.anterior=actual.anterior;
        }
    }

    public void modificarPosicion(int indice, T elem) {
        Nodo actual=cabeza;
        int contador=0;
        while (contador<indice) {
            actual=actual.siguiente;
            contador++;
        }
        actual.valor=elem;
    }

    public ListaEnlazada<T> copiar() {
        ListaEnlazada<T> nuevaLista= new ListaEnlazada<>();
        Nodo actual = cabeza;
        while (actual!=null) {
            nuevaLista.agregarAtras(actual.valor);
            actual=actual.siguiente;
        }
        return nuevaLista;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        Nodo actual=lista.cabeza;
        while (actual != null) {
            this.agregarAtras(actual.valor);
            actual = actual.siguiente;
        }
    }
    
    @Override
    public String toString() {
        Nodo actual=cabeza;
        Integer contador=0;
        StringBuffer sbuffer = new StringBuffer();
        sbuffer.append("[");
        while (actual!=cola){
                sbuffer.append(obtener(contador)+", ");
                actual=actual.siguiente;
                contador +=1;
        }
        sbuffer.append(obtener(contador)+"]"); /*quedo un poco confuso, en el ciclo agrego todos los elementos y al salir agrego el ultimo y cierro el corchete */
        return sbuffer.toString();
    }

    private class ListaIterador implements Iterador<T> {
        private Nodo iteradorApuntaAdelante;
        private Nodo iteradorApuntaAtras;
        public boolean haySiguiente() {
            if (cabeza==null) {
                return false;
            }
            else if (iteradorApuntaAtras==cola) {
                return false;
            }
            else if (iteradorApuntaAdelante==null&&cabeza!=null) {
                iteradorApuntaAdelante=cabeza;
                return true;
            }
            else{
                return true;
            }
        }
        
        public boolean hayAnterior() {
            if (cabeza==null) {
                return false;
            }
            else if (iteradorApuntaAtras==null) {
                return false;
            }
            else {
                return true;
            }
           
        }

        public T siguiente() {
            T valor;
            valor=iteradorApuntaAdelante.valor;
            iteradorApuntaAtras=iteradorApuntaAdelante;
            if (iteradorApuntaAdelante==cola){
                iteradorApuntaAdelante=null;
            }
            else{
                iteradorApuntaAdelante=iteradorApuntaAdelante.siguiente;
                }
            return valor;
        }
        

        public T anterior() {
            T valor=iteradorApuntaAtras.valor;
            iteradorApuntaAdelante=iteradorApuntaAtras;
            if (iteradorApuntaAtras==cabeza){
                iteradorApuntaAtras=null;
            }
            else{
                iteradorApuntaAtras=iteradorApuntaAtras.anterior;
            }
            return valor;
        }
    }

    public Iterador<T> iterador() {
        return new ListaIterador();
    }

}