package aed;

public class Horario {
    private Integer nuevaHora;
    private Integer nuevosMinutos;
    public Horario(int hora, int minutos) {
        nuevaHora=hora;
        nuevosMinutos=minutos;
    }

    public int hora() {
        return nuevaHora;
    }

    public int minutos() {
        return nuevosMinutos;
    }

    @Override
    public String toString() {
        StringBuffer sbuffer = new StringBuffer();
        sbuffer.append(nuevaHora.toString());
        sbuffer.append(":");
        sbuffer.append(nuevosMinutos.toString());
        return sbuffer.toString();
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull= (otro==null);
        boolean otroNoEsTipoHorario=(otro.getClass()!=this.getClass());
        if (otroEsNull||otroNoEsTipoHorario){
            return false;
        }
        Horario otroHorario=(Horario)otro;
        boolean distintaHora=(otroHorario.hora()!=nuevaHora);
        boolean distintoMinuto=(otroHorario.minutos()!=nuevosMinutos);
        if (distintaHora||distintoMinuto){
            return false;
        }
        return true;
    }
    }


