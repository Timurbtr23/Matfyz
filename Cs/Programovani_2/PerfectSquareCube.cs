using System;

namespace Programovani_2
{
    public static class PerfectSquareCube
    {
        public static void isPerfect(int num)
        {
            int check = 0;
            for (int i = num-1; i > 0; i--) if (num % i == 0) check+=i;
            if (check == num) Console.Write("P");
        }

        public static void isSquare(int num)
        {
            double result = Math.Sqrt(num);
            if (result%1 == 0) Console.Write("C");
        }
        
        public static void isCube(int num)
        {
            double result = Math.Truncate(Math.Cbrt(num) * 100000) / 100000;
            if (result%1 == 0) Console.Write("K");
        }
        
        public static void Main1()
        {
            int number = Convert.ToInt32(Console.ReadLine());
            isPerfect(number);
            isSquare(number);
            isCube(number);
        }
    }
}