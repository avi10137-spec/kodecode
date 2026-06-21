using System;
namespace day1;
class Datatypes
{
    static void Main()
    {
        Console.WriteLine("enter a id");
        string id = Console.ReadLine();
        int newId;
        while (! int.TryParse(id, out newId))
        {
            Console.WriteLine("enter a number");
            id = Console.ReadLine();
        }
        Console.WriteLine("enter a speed");
        double newSpeed;
        string speed = Console.ReadLine();
        while (!double.TryParse(speed, out newSpeed))
        {
            Console.WriteLine("enter a speed");
            speed = Console.ReadLine();
           
                }
        string speedStatus;
        if (newSpeed < 100) speedStatus = "slow";
        else if (newSpeed < 300) speedStatus = "medium";
        else speedStatus = "fast";
        Console.WriteLine($"Status speed is {speedStatus}");
      Console.WriteLine("enter a heding");
        string heading = Console.ReadLine();
        double newHeading;
        while (!double.TryParse(heading, out  newHeading))
        {
            //Console.WriteLine("enter a heading");
            heading = Console.ReadLine();
        }
        if (newHeading < 0 || newHeading > 359)
            Console.WriteLine($"heading {newHeading} is invalid");

        string status = Console.ReadLine();

        int resulta = (int)newSpeed / 60;
        //Console.WriteLine( resulta);

        double resultb = newSpeed / 60;
        //Console.WriteLine(resultb);
        int resultc = (int)newHeading / 30;
        double resultd = newHeading/ 30;

        Console.WriteLine($"===track report===\ntrack ID:" +
         $" {newId}\nSpeed:{newSpeed}\nHeading:{newHeading}degrees\nStatus" +
         $":{status}\nDivision demo 1 {newSpeed}/60 ={resulta} (int) |{resultb} (double)\n" +
         $"division demo 2 {newHeading}/30 = {resultc} (int) | {resultd} (double)");





    }

}
