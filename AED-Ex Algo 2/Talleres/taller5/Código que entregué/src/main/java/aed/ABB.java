package aed;

import java.util.*;

// Todos los tipos de datos "Comparables" tienen el método compareTo()
// elem1.compareTo(elem2) devuelve un entero. Si es mayor a 0, entonces elem1 > elem2
public class ABB<T extends Comparable<T>> implements Conjunto<T> {
    // Agregar atributos privados del Conjunto
    private Nodo _raiz;
    // se pudem agregar los atributos cardinal y altura:
    //private _int _cardinal;
    // private int _altura;
    private class Nodo {
        T valor;
        Nodo izq;
        Nodo der;
        Nodo arriba;
        Nodo(T v) {
        valor = v;
        izq = null;
        der = null;
        arriba = null;
        }
    }

    public ABB() {
        _raiz=null;
        // _cardinal = 0;
        // _altura=0;
    }

    public int cardinal() {
        return cantidadDeHijos(_raiz);
    }

    private int cantidadDeHijos(Nodo nodo) {
        if (nodo==null) {
            return 0;
        }
        else {
            return 1+cantidadDeHijos(nodo.izq)+cantidadDeHijos(nodo.der);
        }
    }  

    public T minimo(){
        if (_raiz==null) {
            return null;
        }
        Nodo actual=_raiz;
        while (actual.izq!=null) {
            actual=actual.izq;
        }
        return actual.valor;
    }
    public T maximo(){
        if (_raiz==null) {
            return null;
        }
        Nodo actual=_raiz;
        while (actual.der!=null) {
            actual=actual.der;
        }
        return actual.valor;
    }

    public void insertar(T elem){
        if (!(pertenece(elem))) { 
            Nodo nodoAInsertar= new Nodo(elem);
            if (_raiz==null) {
                _raiz=nodoAInsertar;
            }
            else {
                Nodo ultimoNodoBuscado=ultimoNodoBuscado(elem, _raiz);
                if (ultimoNodoBuscado.valor.compareTo(elem)>0) {
                    nodoAInsertar.arriba=ultimoNodoBuscado;
                    ultimoNodoBuscado.izq=nodoAInsertar;
                }
                else{
                    nodoAInsertar.arriba=ultimoNodoBuscado;
                    ultimoNodoBuscado.der=nodoAInsertar;
                }
            }  
        }
    }
    //el metodo de abajo es la implementacion del algo de las diapos
    //devuelve el nodo en el que hay que insertar el elemento
    private Nodo ultimoNodoBuscado(T elemento, Nodo nodo){
        if (nodo.valor.compareTo(elemento)>0) {
            if (nodo.izq==null) {
                return nodo;
            }
            else{
                return ultimoNodoBuscado(elemento, nodo.izq);
            }
        }
        else{
            if (nodo.der==null) {
                return nodo;
            }
            else{
                return ultimoNodoBuscado(elemento, nodo.der);
            }
        }         
    }
    

    public boolean pertenece(T elem){
        if (_raiz==null) {
            return false;
        }
        else{
            return busquedaRecursiva(elem, _raiz);
        }
    }
    
    
    private boolean busquedaRecursiva(T elem,Nodo nodo){
        if (nodo==null) {
            return false;
        } 
        if (nodo.valor.equals(elem)) {
            return true;
        }
        if (nodo.valor.compareTo(elem)>0) {
                return busquedaRecursiva(elem, nodo.izq);
        }
        else{
                return busquedaRecursiva(elem, nodo.der);
        }
    }

    public void eliminar(T elem) {
        if (!pertenece(elem)) {
            return; //Caso 1
        }
    
        Nodo nodoAEliminar = _raiz;
        Nodo padre = null; //defino padre porque el valor "arriba" no me funciona
    
       
        while (nodoAEliminar != null && !nodoAEliminar.valor.equals(elem)) {
            padre = nodoAEliminar;
            if (elem.compareTo(nodoAEliminar.valor) < 0) {
                nodoAEliminar = nodoAEliminar.izq;
            } else {
                nodoAEliminar = nodoAEliminar.der;
            }
        }
    
        //Caso 2
        if (nodoAEliminar.izq == null && nodoAEliminar.der == null) {
            if (nodoAEliminar == _raiz) {
                _raiz = null;
            } else if (padre.izq == nodoAEliminar) {
                padre.izq = null;
            } else {
                padre.der = null;
            }
        }
        //Caso 3
        else if (nodoAEliminar.izq == null || nodoAEliminar.der == null) {
            Nodo hijo;
            if (nodoAEliminar.izq != null){
                hijo=nodoAEliminar.izq;
            }
            else{
                hijo=nodoAEliminar.der;
            }
            if (nodoAEliminar == _raiz) {
                _raiz = hijo;
            } else if (padre.izq == nodoAEliminar) {
                padre.izq = hijo;
            } else {
                padre.der = hijo;
            }
        }
        //Caso 4 del else para abajo
        else {
            Nodo sucesor = nodoAEliminar.der;
            Nodo padreSucesor = nodoAEliminar;
            while (sucesor.izq != null) {
                padreSucesor = sucesor;
                sucesor = sucesor.izq;
            }
            nodoAEliminar.valor = sucesor.valor;

            if (padreSucesor.izq == sucesor) {
                padreSucesor.izq = sucesor.der;
            } else {
                padreSucesor.der = sucesor.der;
            }
        }
    }

    public String toString(){
        StringBuffer textoADevolver = new StringBuffer();
        textoADevolver.append("{");
        toStringRecursivo(_raiz, textoADevolver);
        return textoADevolver.toString();
    }
    private void toStringRecursivo(Nodo nodo, StringBuffer textoADevolver) {
        if (nodo != null) {
            toStringRecursivo(nodo.izq, textoADevolver);
            if (nodo.valor==maximo()) {
                textoADevolver.append(nodo.valor+"}");
            }
            else{
                textoADevolver.append(nodo.valor+",");
            };
            toStringRecursivo(nodo.der, textoADevolver);
        }
    }

    private class ABB_Iterador implements Iterador<T> {
        private Nodo _actual=nodoMinimo(_raiz);

        private Nodo nodoMinimo(Nodo _raiz){
            Nodo actual=_raiz;
            while (actual.izq!=null) {
                actual=actual.izq;
            }
            return actual;
        }

        private Nodo calcularSucesor(Nodo nodo){
            if (nodo.der!=null) {
                Nodo actual=nodo.der; 
                while (actual.izq!=null) {
                    actual=actual.izq;
                }
                return actual;
            }
            Nodo actual=nodo.arriba;
            while (actual!=null&&nodo==actual.der) {
                nodo=actual;
                actual=actual.arriba;
            }
            return actual;
        }

        public boolean haySiguiente() {            
            return calcularSucesor(_actual)!=null;
        }
    
        public T siguiente() {
            T valorADevolver=_actual.valor;
            _actual=calcularSucesor(_actual);
            return valorADevolver;
        }
    }

    public Iterador<T> iterador() {
        return new ABB_Iterador();
    }

}
