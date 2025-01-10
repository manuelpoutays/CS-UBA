package aed;

class Funciones {
    int cuadrado(int x) {
        int res;
        res=x*x;
        return res;
    }

    double distancia(double x, double y) {
        double dist;
        if (x>y){ 
            dist= Math.sqrt((x*x)+(y*y));
        }
        else{
           dist= Math.sqrt((y*y)+(x*x));
        }
        return dist;
    }
    // {} 
    boolean esPar(int n) {
        boolean parOImpar;
        parOImpar= n%2==0;
        return parOImpar ;
    }

    boolean esBisiesto(int n) {
        boolean nEsBiciesto;
        nEsBiciesto=false;
        boolean nDivisiblePor4;
        boolean nDivisiblePor100;
        boolean nDivisiblePor400;
        nDivisiblePor4 = (n%4==0);
        nDivisiblePor100= (n%100==0);
        nDivisiblePor400=(n%400==0);

        if (nDivisiblePor4){
            nEsBiciesto=true;
            if (nDivisiblePor100){
                if (nDivisiblePor400){
                    nEsBiciesto=true;
                }
                else {
                    nEsBiciesto=false;
                }
            }
        }
        return nEsBiciesto;
    }

    int factorialIterativo(int n) {
        int resultado;
        resultado=1;
        if (n==0){
            return resultado;
        }
        for (int i=1;i<=n;i+=1){
            resultado=resultado*i;
        }
        return resultado;
    }

    int factorialRecursivo(int n) {
        int resultado;
        if (n==0)
        {return 1;
        }
        resultado=n*factorialRecursivo(n-1);
        return resultado;
    }

    boolean esPrimo(int n) {
        int contador;
        contador=0;
        for (int i=1;i<=n;i+=1){
            if (n%i==0){
                contador+=1;
            }
        }
        if (contador==2){
            return true;
        }
        else {
            return false;}
    }

    int sumatoria(int[] numeros) {
        int resultado;
        resultado=0;
        for (int i=0;i<numeros.length;i+=1){
            resultado=resultado+numeros[i];
        }
        return resultado;
    }

    int busqueda(int[] numeros, int buscado) {
        for (int i=0;i<numeros.length;i+=1){
            if (numeros[i]==buscado) {
                return i;
            }
        }
        return 0;
    }

    boolean tienePrimo(int[] numeros) {
        for (int i=0;i<numeros.length;i+=1){
            if (esPrimo(numeros[i])) {
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for (int i=0;i<numeros.length;i+=1){
            if (numeros[i]%2!=0) {
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        for (int i=0;i<s1.length();i+=1){
            if (i>=s2.length()){
                return false;
            }
            if (s1.charAt(i)!=s2.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    boolean esSufijo(String s1, String s2) {
        if (s1.length()>s2.length()){
            return false;
        }
        int inicioContador;
        inicioContador=s2.length()-s1.length();
        String nuevaPlabra;
        nuevaPlabra ="";
        for (int i=inicioContador;i<s2.length();i+=1){
            nuevaPlabra+=s2.charAt(i);
        }
        return esPrefijo(s1,nuevaPlabra);
    }
}
