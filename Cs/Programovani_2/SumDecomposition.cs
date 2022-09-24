using System;
using System.Collections.Generic;

namespace Programovani_2
{
    class SumDecomposition{
        
        static void PrintVector(List<int> arr)
        {
            for (var i = 0; i < arr.Count; i++)
            {
                if (i != arr.Count-1) Console.Write(arr[i] + "+");
                else Console.Write(arr[i]);
            }
            Console.WriteLine();
        }
        
        static void FindWays(List<int> arr, int i, int n)
        {
            if (n == 0) PrintVector(arr);
            
            for(var j = i; j <= n; j++)
            {
                arr.Add(j);
                FindWays(arr, j, n - j);
                arr.RemoveAt(arr.Count - 1);
            }
        }

        public static void Main1(String[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            List<int> arr = new List<int>();
            FindWays(arr, 1, n);
        }
    }
}