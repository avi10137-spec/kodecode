using System;
using System.Net.NetworkInformation;
namespace day3;

enum Statuses { Friendly, Hostile, Uniidentified }
class Intelligence
{
  
    static void addMassege( List<int> ides,List <Statuses> status,List<double?> signal)

    {
        int newId;
        Console.WriteLine("enter id");
        string myid=Console.ReadLine();
        if (!int.TryParse(myid , out newId))
        {
            Console.WriteLine("id invalid input");
            return;
        }
        if (ides.Contains(newId))
            {
            Console.WriteLine("id is exist");
            return;
        }
            ides.Add(newId);
        Statuses newStatus;
        Console.WriteLine("enter status");
        string myStatus = Console.ReadLine();
        if (!Statuses.TryParse(myStatus, out newStatus))
        {
            Console.WriteLine("status invalid input");
            return;
        }

        status.Add(newStatus);
        double ? newSignal=null;

        Console.WriteLine("enter signal");
        string mySignal = Console.ReadLine();
        if (!string.IsNullOrWhiteSpace(mySignal))
        {
            if (!double.TryParse(mySignal, out double newSignal1))
            {
                Console.WriteLine("signal invalid input");
                return;
            }
            newSignal = newSignal1;  
       
        }


        signal.Add(newSignal);

    }
    static int findById(int id,List<int> ides, List<Statuses> status, List<double?>signal)
    {
        for (int i = 0; i < ides.Count; i++)
        {
            if (ides[i] == id)
            {
                return i;
            }

        }
        return -1;
    }
    
    static void update(List<int> ides, List<Statuses> status, List<double?>signal)
        
    {
        int newId;
        Console.WriteLine("enter id");
        string myid = Console.ReadLine();
        if (!int.TryParse(myid, out newId))
        {
            Console.WriteLine("id invalid input");
            return;
        }
        if (!ides.Contains(newId))
        {
            Console.WriteLine("id is not exist");
        }
         int index = findById(newId, ides, status, signal);
        double? newSignalForUp = null;

        Console.WriteLine("enter  new signal");
        string mySignal = Console.ReadLine();
        if (!string.IsNullOrWhiteSpace(mySignal))
        {
            if (!double.TryParse(mySignal, out double newSignal1))
            {
                Console.WriteLine("signal invalid input");
                return;
            }
            newSignalForUp = newSignal1;
            signal[index] = newSignalForUp;

        }
    }
     static void printerMassege(int index,List<int> ides, List<Statuses> status, List<double?> signal)


    //    int newId;
    //Console.WriteLine("enter id");
    //    string myid = Console.ReadLine();
    //    if (!int.TryParse(myid, out newId))
    //    {
    //        Console.WriteLine("id invalid input");
    //        return;
    //    }
    //    if (!ides.Contains(newId))
    //    {
    //        Console.WriteLine("id is not exist");
    //        return;
    //    }
    //    int index = findById(newId, ides, status, signal);//{
    { 

Console.WriteLine($"massege id {ides[index]}  status is {status[index]} ,value signal is {signal[index]} ");
      }
    static void printAll(List<int> ides, List<Statuses> status, List<double?> signal)
    {
      
        {
            for (int i = 0; i < ides.Count; i++)
            {
                printerMassege(i, ides, status, signal);
            }
        }
    }
    static void Main()
    {
     
    List<int> ides = new List<int>();
    List<Statuses> status = new List<Statuses>();
    List<double?> signal = new List<double?>();
        string choice = "-1";

        while (choice != "4")
        {
            Console.WriteLine("=== Signal Intercept Log ===");
            Console.WriteLine("1. Add new transmission");
            Console.WriteLine("2. Calibrate existing signal");
            Console.WriteLine("3. List all transmissions");
            Console.WriteLine("4. Quit");
            Console.Write("Choose option: ");

            choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    addMassege(ides, status, signal);
                    break;
                case "2":
                    update(ides, status, signal);
                    break;
                case "3":
                    printAll(ides, status, signal);
                    break;
                case "4":
                    break;
                default:
                    Console.WriteLine("There is no such option, try again.");
                    break;
            }
        }
        

      
        //printerMassege(ides, status, signal);
        
    }
}


