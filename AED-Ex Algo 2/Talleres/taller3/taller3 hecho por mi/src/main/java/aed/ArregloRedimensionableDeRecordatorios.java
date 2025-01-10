package aed;

class ArregloRedimensionableDeRecordatorios implements SecuenciaDeRecordatorios {
    private Recordatorio[] arregloRecordatorios;
    public ArregloRedimensionableDeRecordatorios() {
        Recordatorio[] nuevoArregloVacio= new Recordatorio[0];
        arregloRecordatorios=nuevoArregloVacio;
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        Recordatorio[] copiaVector=new Recordatorio[vector.longitud()];
        for (int i = 0; i < vector.longitud(); i++) {
            copiaVector[i]=vector.obtener(i);
        }
        arregloRecordatorios=copiaVector;
    }

    public int longitud() {
        return arregloRecordatorios.length;
    }

    public void agregarAtras(Recordatorio i) {
        Recordatorio[] arregloMasUno = new Recordatorio[arregloRecordatorios.length+1];
        for (int j = 0; j < arregloMasUno.length-1; j++) {
            arregloMasUno[j]=arregloRecordatorios[j];
        }
        arregloMasUno[arregloRecordatorios.length]=i;
        arregloRecordatorios=arregloMasUno;
    }

    public Recordatorio obtener(int i) {
        return arregloRecordatorios[i];
    }

    public void quitarAtras() {
        Recordatorio[] arregloMenosUno = new Recordatorio[arregloRecordatorios.length-1];
        for (int j = 0; j < arregloMenosUno.length; j++) {
            arregloMenosUno[j]=arregloRecordatorios[j];
        }
        arregloRecordatorios=arregloMenosUno;
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        arregloRecordatorios[indice]=valor;

    }

    public ArregloRedimensionableDeRecordatorios copiar() {
        ArregloRedimensionableDeRecordatorios copia =new ArregloRedimensionableDeRecordatorios();
        for (int i = 0; i < arregloRecordatorios.length; i++) {
            copia.agregarAtras(obtener(i));
        }
        return copia;
    }

}
