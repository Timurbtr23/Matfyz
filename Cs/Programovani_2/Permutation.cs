using System;

namespace Programovani_2
{
    public static class Permutation
    {
        public static void Main()
        {
            int N = Convert.ToInt32(Console.ReadLine());
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(), s => Convert.ToInt32(s));
            
            int max = arr[..N].Max();
            Console.WriteLine(max);
            for (int i = 0; i < N; i++)
            {
                if (arr[i] == max) Console.Write((i+1) + " ");
            }
        }
    }
}