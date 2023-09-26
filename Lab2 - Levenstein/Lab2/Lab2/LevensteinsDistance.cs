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

        static void Run_It_Back(int curr_line, int curr_column, string curr_word, string result, int[,] Matrix)
        {

        }

        static void Main()
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

            //Filling the matrix up using VF method
            for (int column = 1; column < VF_Matrix.Rank(0); ++column)
            {
                for (int line = 1; line < VF_Matrix.Rank[1]; ++line)
                {
                    //Whether we +1 the left-up num in the comparison depends on whether the letters of the current pair are equal
                    VF_Matrix[line, column] = max(VF_Matrix[line - 1, column] + 1, VF_Matrix[line, column - 1] + 1, VF_Matrix[line - 1, column - 1] + 1 * (VF_Matrix[0, column] != VF_Matrix[line, 0]));
                }
            }
            //Got the Matrix, now the most faraway from (0,0) cell contains the Levenstein`s Distance.
            Console.WriteLine("The Levenstein`s Distance for the input pair of words = {0}", VF_Matrix[Word1.Length + 1, Word2.Length + 1]);

            //To trace the path of permutations, we`ll use a recurrent function
            Run_It_Back(0, 0, Word1, Word2, VF_Matrix);

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
