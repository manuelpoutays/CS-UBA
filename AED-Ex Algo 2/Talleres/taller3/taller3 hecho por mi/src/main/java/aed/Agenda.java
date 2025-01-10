package aed;

public class Agenda {
    private Fecha fechaAgenda;
    private ArregloRedimensionableDeRecordatorios recordatoriosDelDia;
    public Agenda(Fecha fechaActual) {
        fechaAgenda=fechaActual;
        recordatoriosDelDia= new ArregloRedimensionableDeRecordatorios();
    }

    public void agregarRecordatorio(Recordatorio recordatorio) {
        recordatoriosDelDia.agregarAtras(recordatorio);
    }

    @Override
    public String toString() {
        StringBuffer sbuffer = new StringBuffer();
        sbuffer.append(fechaActual().toString()+"\n");
        sbuffer.append("=====\n");
        for (int i = 0; i < recordatoriosDelDia.longitud(); i++) {
            if ((recordatoriosDelDia.obtener(i)).fecha().equals(fechaActual())) {
                sbuffer.append(recordatoriosDelDia.obtener(i)+"\n");
            }
        }
        return sbuffer.toString();
    }

    public void incrementarDia() {
        fechaAgenda.incrementarDia();;

    }

    public Fecha fechaActual() {
        Fecha fechaActual=new Fecha(fechaAgenda);
        return fechaActual;
    }

}
