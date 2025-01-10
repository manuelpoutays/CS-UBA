package aed;

public class Fecha {
    private Integer nuevoDia;
    private Integer nuevoMes;
    public Fecha(int dia, int mes) {
        this.nuevoDia=dia;
        this.nuevoMes=mes;
    }
/*Acá creo que se distinguen los métodos "Fecha" por los parámetros */
/*no se para que es el segundo metodo fecha */

    public Fecha(Fecha fecha) {
        nuevoDia=fecha.dia();
        nuevoMes=fecha.mes();
    }

    public Integer dia() {
        return nuevoDia;
    }

    public Integer mes() {
        return nuevoMes;
    }

    public String toString() {
        StringBuffer sbuffer = new StringBuffer();
        sbuffer.append(nuevoDia.toString());
        sbuffer.append("/");
        sbuffer.append(nuevoMes.toString());
        return sbuffer.toString();
    }

    @Override
    public boolean equals(Object otra) {
        boolean otraEsNull= (otra==null);
        boolean otraNoEsTipoFecha=(otra.getClass()!=this.getClass());
        if (otraEsNull||otraNoEsTipoFecha){
            return false;
        }
        Fecha otraFecha=(Fecha)otra;
        boolean distintoDia=(otraFecha.dia()!=nuevoDia);
        boolean distintoMes=(otraFecha.mes()!=nuevoMes);
        if (distintoDia||distintoMes){
            return false;
        }
        return true;
    }

    public void incrementarDia() {
        int diaAumentado=nuevoDia+1;
        if (diaAumentado>diasEnMes(nuevoMes)) {
            nuevoDia=1;
            nuevoMes+=1;
        }
        else {
            nuevoDia=nuevoDia+1;
        }
        if (nuevoMes>12){
            nuevoMes=1;
        }
    }
    private int diasEnMes(int mes) {
        int dias[] = {
                // ene, feb, mar, abr, may, jun
                31, 28, 31, 30, 31, 30,
                // jul, ago, sep, oct, nov, dic
                31, 31, 30, 31, 30, 31
        };
        return dias[mes - 1];
    }

}
