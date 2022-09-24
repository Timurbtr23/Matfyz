using System;

namespace Programovani_2
{
    public static class Division
    {
        public static void Main1()
        {
            string[] numbers = Console.ReadLine().Split();
            if (Convert.ToInt32(numbers[1]) == 0) Console.WriteLine("NELZE");
            else Console.WriteLine(Convert.ToInt32(numbers[0]) / Convert.ToInt32(numbers[1]));
        }
    }
}