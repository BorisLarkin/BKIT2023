using System;
using System.Text;

namespace LevensteinApp
{
    class LevensteinDistance
    {
        static string GetInput (string prompt)
        {
            Console.Write(prompt);
            string Inp = Console.ReadLine();
            int count = 0;
            foreach (var el in Inp) if (char.IsLetter(el)) count++;
            while (count == 0) {
                Console.WriteLine("Enter a non-empty string");
                Inp = Console.ReadLine();
                foreach (var el in Inp) if (char.IsLetter(el)) count++;
            }
            //Having taken in a string with letters, delete everything non-letter
            StringBuilder Result = new StringBuilder('a'*count);
            int curr_index = 0;
            foreach (var x in Inp) if (char.IsLetter(x)) { Result[curr_index] = x; curr_index++; };
            return Result.ToString();
        }

        static void Main(string[] args)
        {
            Console.WriteLine("### Levenstein`s Distance Calculation Algorithm ###\n");
            string Word1 = GetInput("Enter the first word: ");
            string Word2 = GetInput("Enter the second word: ");

            Console.WriteLine(Word1 + " " + Word2);

            int[,] VF_Matrix = new int[Word1.Length + 1, Word2.Length + 1]; //Creating a Vagner-Fischer`s Matrix

            //Initializing the first line of the Matrix
            for (int i = 0; i < Word2.Length + 1; ++i)
            {
                VF_Matrix[0, i] = i;
            }

            //Initializing the first column of the Matrix
            for (int j = 0; j < Word1.Length + 1; ++j)
            {
                VF_Matrix[j, 0] = j;
            }

            for (int i = 0; i < VF_Matrix.GetLength(0); i++)
            {
                for (int j = 0; j < VF_Matrix.GetLength(1); j++)
                {
                    Console.Write(VF_Matrix[i, j] + "\t");
                }
                Console.WriteLine();
            }

            Console.Write("\nProgram finished. Press any key to terminate . . .");
            Console.ReadKey();
            return;
        }
    }
}
