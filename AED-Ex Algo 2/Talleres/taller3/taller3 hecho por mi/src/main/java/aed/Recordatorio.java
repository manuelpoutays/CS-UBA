package aed;

public class Recordatorio {
    private String nMensaje;
    private Fecha nFecha;
    private Horario nHorario;
    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
        nMensaje=mensaje;
        nFecha= new Fecha(fecha.dia(),fecha.mes());
        nHorario=horario;
    }

    public Horario horario() {
        return nHorario;
    }

    public Fecha fecha() {
        Fecha fechaADevolver= new Fecha(nFecha.dia(),nFecha.mes());
        return fechaADevolver;
    }

    public String mensaje() {
        return nMensaje;
    }

    @Override
    public String toString() {
        StringBuffer sbuffer = new StringBuffer();
        sbuffer.append(nMensaje.toString());
        sbuffer.append(" @ ");
        sbuffer.append(nFecha.toString());
        sbuffer.append(" ");
        sbuffer.append(nHorario.toString());
        return sbuffer.toString();
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull= (otro==null);
        boolean otroNoEsTipoRecordatorio=(otro.getClass()!=this.getClass());
        if (otroEsNull||otroNoEsTipoRecordatorio){
            return false;
        }
        Recordatorio otroRecordatorio=(Recordatorio)otro;
        boolean distintoMensaje=!(otroRecordatorio.mensaje().equals(nMensaje));
        boolean distintoHorario=!(otroRecordatorio.horario().equals(nHorario));
        boolean distintaFecha=!(otroRecordatorio.fecha().equals(nFecha));
        if (distintoMensaje||distintoHorario||distintaFecha){
            return false;
        }
        return true;
    }

}
