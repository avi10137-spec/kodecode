
using System.Threading.Channels;

class Trucks 
{
    static List<int> ides = new List<int>();
    static List<double> speeds = new List<double>();
    static List<int> headings = new List<int>();
    static void addTruck(int id, double speed, int heading)
    {
        ides.Add(id);
        speeds.Add(speed);
        headings.Add(heading);

    }

     static void removeTruck(int id)
    {
        for (int i = 0; i < ides.Count; i++)
        {
            if (ides[i] == id)
            {
                ides.Remove(ides[i]);
                speeds.Remove(speeds[i]);
                headings.Remove(headings[i]);
                
            }
        }

    }

    static void printerTrucks(int index)
    {
        Console.WriteLine($"trucks id {ides[index]}  drive in speed {speeds[index]} ,twords to {headings[index]}              ");
    }
    static void findById(int id)
    {
        for (int i = 0; i < ides.Count; i++)
        {
            if (ides[i] == id)
            {
                printerTrucks(i);
            }

        }
    }
    static void prinAll()
    {
        for (int i = 0; i < ides.Count; i++)
        {
            printerTrucks(i);
        }
    }
 static void Main()
    {
        addTruck(1, 150.0, 45);
        addTruck(2, 130.0, 90);
        addTruck(3, 85.0, 180);
        printerTrucks(0);
        //removeTruck(1);
        printerTrucks(1);
        findById(3);
        prinAll();
    }




}



