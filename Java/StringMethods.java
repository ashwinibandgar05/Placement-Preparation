public class StringMethods {
    public static void main(String[] args) {
        String Name="Harry";
        System.out.println(Name.length());
        System.out.println(Name.toUpperCase());
        System.out.println(Name.toLowerCase());
        String Name2=   "   Harry123   " ;
        System.out.println(Name2.trim());
        System.out.println(Name.substring(2));
        System.out.println(Name.substring(3,5));
        System.out.println(Name.replace("r","p"));
        System.out.println(Name.replace("rry","ir"));
        System.out.println(Name.startsWith("Ha"));
        System.out.println(Name.endsWith("ry"));
        System.out.println(Name.charAt(3));
        System.out.println(Name.indexOf("r"));
        System.out.println(Name.indexOf('r',3));
        System.out.println(Name.lastIndexOf("r"));
        System.out.println(Name.lastIndexOf("r",2));
        System.out.println(Name.equals("Harry"));
        System.out.println(Name.equalsIgnoreCase("harry"));

    }
}
