using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

namespace Drill1
{
    public interface IAnimal
    {
        void PrintToConsole();
        string ToString();
    }

    

    [Serializable()]
    public abstract class Animal : IAnimal, ISerializable
    {



        private static int currentID;
        public int ID { get; set; }
        public string Name { get; set; }
        public string Sound { get; set; }
        public int Weight { get; set; }
        public int Height { get; set; }
        public int Speed { get; set; }
        public string Fly { get; set; }

        


        public Animal()
        {
            ID = 0;
            Name = "";
            Sound = "The sound is unknown";
            Weight = 0;
            Height = 0;
            Speed = 0;
            Fly = "this bird flies";
        }

        public Animal(string name, string sound, int weight, int height, int speed, string fly)
        {
            this.ID = GetNextID();
            this.Name = name;
            this.Sound = sound;
            this.Weight = weight;
            this.Height = height;
            this.Speed = speed;
            this.Fly = fly;
        }

        public Animal(SerializationInfo info, StreamingContext ctxt)
        {
            ID = (int)info.GetValue("ID", typeof(int));
            Name = (string)info.GetValue("Name", typeof(string));
            Sound = (string)info.GetValue("Sound", typeof(string));
            Weight = (int)info.GetValue("Weight", typeof(int));
            Height = (int)info.GetValue("Height", typeof(int));
            Speed = (int)info.GetValue("Speed", typeof(int));
            Fly = (string)info.GetValue("Fly", typeof(string));
        }

        public void GetObjectData(SerializationInfo info, StreamingContext ctxt)
        {
            info.AddValue("ID", ID);
            info.AddValue("Name", Name);
            info.AddValue("Sound", Sound);
            info.AddValue("Weight", Weight);
            info.AddValue("Height", Height);
            info.AddValue("Speed", Speed);
            info.AddValue("Fly", Fly);
        }

        public static void ObjSerial(string file, List<Animal> animals)
        {
            Stream stream = File.Open(file, FileMode.Create);
            BinaryFormatter bformatter = new BinaryFormatter();

            Console.WriteLine("Writing Animal Information");
            
            bformatter.Serialize(stream, animals);
            stream.Close();
        }

        public static List<Animal> ReadObjSerial(string file)
        {
            List<Animal> animals = new List<Animal>();
            Stream stream = File.Open(file, FileMode.Open);
            BinaryFormatter bformatter = new BinaryFormatter();

            Console.WriteLine("... Reading Animal Information...");
            
            animals = (List<Animal>)bformatter.Deserialize(stream);

            return animals;
        }

        static Animal()
        {
            currentID = 0;
        }

        protected internal int GetNextID()
        {
            return ++currentID;
        }

        public override string ToString()
        {
            return string.Format("{0} - {1}\n \t It says {2}\n \t {3} kg\n \t {4} cm\n \t {5} km/h\n \t {6}", this.Name, this.ID, this.Sound, this.Weight, this.Height, this.Speed, this.Fly);
        }

        public void PrintToConsole()
        {
            Console.WriteLine(this.ToString());
        }

        public static void PrintList(List<Animal> list)
        {
            foreach (var animal in list)
            {
                animal.PrintToConsole();
            }
        }

        public static void SearchList(List<Animal> list, int id)
        {
            var result = from animal in list
                         where animal.ID == id
                         select animal;
            foreach (var item in result)
            {
                item.PrintToConsole();
            }
        }

        public static void SearchList(List<Animal> list, string name)
        {
            var result = from animal in list
                         where animal.Name == name
                         select animal;
            foreach (var item in result)
            {
                item.PrintToConsole();
            }
        }
    }

    [Serializable()]
    public class Mammal: Animal
    { 
        public Mammal()
        {
            ID = 0;
            Name = "";
            Sound = "The sound is unknown";
            Weight = 0;
            Height = 0;
            Speed = 0;
            Fly = "this doesn't fly";

        }

        public Mammal(string name, string sound, int weight, int height, int speed, string fly)
        {
            this.ID = GetNextID();
            this.Name = name;
            this.Sound = sound;
            this.Weight = weight;
            this.Height = height;
            this.Speed = speed;
            this.Fly = fly;
        }

        public Mammal(SerializationInfo info, StreamingContext ctxt)
        {
            ID = (int)info.GetValue("ID", typeof(int));
            Name = (string)info.GetValue("Name", typeof(string));
            Sound = (string)info.GetValue("Sound", typeof(string));
            Weight = (int)info.GetValue("Weight", typeof(int));
            Height = (int)info.GetValue("Height", typeof(int));
            Speed = (int)info.GetValue("Speed", typeof(int));
            Fly = (string)info.GetValue("Fly", typeof(string));
        }
    }

        [Serializable()]
    class Bird : Animal
    {
        
        public Bird(string name, string sound, int weight, int height, int speed, string fly)
        {
            this.ID = GetNextID();
            this.Name = name;
            this.Sound = sound;
            this.Weight = weight;
            this.Height = height;
            this.Speed = speed;
            this.Fly = fly;
        }

        public Bird(SerializationInfo info, StreamingContext ctxt)
        {
            ID = (int)info.GetValue("ID", typeof(int));
            Name = (string)info.GetValue("Name", typeof(string));
            Sound = (string)info.GetValue("Sound", typeof(string));
            Weight = (int)info.GetValue("Weight", typeof(int));
            Height = (int)info.GetValue("Height", typeof(int));
            Speed = (int)info.GetValue("Speed", typeof(int));
            Fly = (string)info.GetValue("Fly", typeof(string));
            
        }


        public override string ToString()
        {
            return string.Format("{0} - {1}\n \t It says {2}\n \t {3} kg\n \t {4} cm\n \t {5} km/h \n \t {6}", this.Name, this.ID, this.Sound, this.Weight, this.Height, this.Speed, this.Fly);
        }
    }


    sealed class AnimalCompare
    {
        public static int count { get; set; }

        protected void Count()
        {
            count = 0;
        }



        internal static void printCount()
        {
            ++count;
            Console.WriteLine("You have performed {0} comparisons", count);
        }

        public static void weightCompare(Animal animal1, Animal animal2)
        {
            if (animal1.Weight == animal2.Weight)
            {
                Console.WriteLine("The {0} and the {1} have the same weight", animal1.Name, animal2.Name);
            }
            else
            {
                Console.WriteLine("The {0} and the {1} don't have the same weight", animal1.Name, animal2.Name);
            }
            printCount();

        }

    }

    class UserSearch
    {
        public static void Search(List<Animal> animalList)
        {
            Console.WriteLine("Would you like to search for an animal \n \t by name type 1 \n \t by ID type 2 \n \t or by weight type 3 \n \t Exit Search type 4");
            string response = Console.ReadLine();

            if (response == "1")
            {
                Console.WriteLine("Search for animal name: ");
                string name = Console.ReadLine();
                SearchName(animalList, name);
                Search(animalList);


            } else if (response == "2")
            {
                Console.WriteLine("Search for animal ID: ");
                string name = Console.ReadLine();
                try
                {
                    int Id = Int32.Parse(name);
                    SearchID(animalList, Id);
                } catch (FormatException ex)
                {
                    Console.WriteLine("Invalid Input");
                    string filePath = @"C:\Users\sdorw_000\Documents\Tech Academy\C#\Drills\drill1\Drill1\Error.txt";

                    using (StreamWriter writer = new StreamWriter(filePath, true))
                    {
                        writer.WriteLine("Message :" + ex.Message + "<br/>" + Environment.NewLine + "StackTrace :" + ex.StackTrace +
                           "" + Environment.NewLine + "Date :" + DateTime.Now.ToString());
                        writer.WriteLine(Environment.NewLine + "-----------------------------------------------------------------------------" + Environment.NewLine);
                    }
                } finally
                {
                    Search(animalList);
                }

            } else if (response == "3")
            {
                Console.WriteLine("Search for animal Weight: ");
                string name = Console.ReadLine();

                try
                {
                    int weight = Int32.Parse(name);
                    SearchWeight(animalList, weight);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Invalid Input");
                    string filePath = @"C:\Users\sdorw_000\Documents\Tech Academy\C#\Drills\drill1\Drill1\Error.txt";

                    using (StreamWriter writer = new StreamWriter(filePath, true))
                    {
                        writer.WriteLine("Message :" + ex.Message + "<br/>" + Environment.NewLine + "StackTrace :" + ex.StackTrace +
                           "" + Environment.NewLine + "Date :" + DateTime.Now.ToString());
                        writer.WriteLine(Environment.NewLine + "-----------------------------------------------------------------------------" + Environment.NewLine);
                    }
                }
                finally
                {
                    Search(animalList);
                }
            } else if (response == "4")
            {
                Console.WriteLine("Thanks for Searching!");
            } else
            {
                Console.WriteLine("That is not a valid input");
                Search(animalList);
            }

        }

        public static void SearchName(List<Animal> animalList,string name)
        {
            var result = from animal in animalList
                         where animal.Name == name
                         select animal;
            foreach (var item in result)
            {
                item.PrintToConsole();
            }
        }

        public static void SearchID(List<Animal> animalList, int id)
        {
            var result = from animal in animalList
                         where animal.ID == id
                         select animal;
            foreach (var item in result)
            {
                item.PrintToConsole();
            }
        }

        public static void SearchWeight(List<Animal> animalList, int weight)
        {
            var result = from animal in animalList
                         where animal.Weight == weight
                         select animal;
            foreach (var item in result)
            {
                item.PrintToConsole();
            }
        }

    }

    class Program
    {
        public enum Sign
        {
            Aries,
            Taurus,
            Gemini,
            Cancer,
            Leo,
            Virgo,
            Libra,
            Scorpio,
            Sagittarius,
            Capricorn,
            Aquarius,
            Pisces
        }

        struct Person: IAnimal
        {
            public string Name;
            public string Nationality;
            public double? Height, Weight;
            public Sign? Sign;

            public override string ToString()
            {
                return string.Format("\n {0} \n \t {1} \n \t {2}m \n \t {3}kg\n \t Zodiac Sign: {4}",this.Name, this.Nationality, this.Height, this.Weight, this.Sign);
            }
            public void PrintToConsole()
            {
                Console.WriteLine(this.ToString());
            }

            public static int ListCount(List<Animal> Alist, List<Person> Plist)
            {
                int count = Alist.Count() + Plist.Count();
                

                return count;
            }

        }

        public static void AnimalName(List<Animal> Alist,int i)
        {
            string animalName = string.Format("\nThis Animal is called: {0}",Alist[i].Name);
            Console.WriteLine(animalName);
        }

        public static void AnimalSound(List<Animal> Alist, int i)
        {
            string animalSound = string.Format("\nThis Animal makes the sound: {0}", Alist[i].Sound);
            Console.WriteLine(animalSound);
        }




        delegate int ListCountDelegate(List<Animal> Alist, List<Person> Plist);
        delegate void AnimalInfo(List<Animal> Alist, int i);
        

        public static void Main(string[] args)
        {
            
            List<Animal> Animals = new List<Animal>();
            List<Person> People = new List<Person>();
            List<Animal> Birds = new List<Animal>();
            List<Animal> Mammals = new List<Animal>();

            ListCountDelegate counter = new ListCountDelegate(Person.ListCount);

            AnimalInfo NameAndSound;
            AnimalInfo Named = new AnimalInfo(AnimalName);
            AnimalInfo Call = new AnimalInfo(AnimalSound);

            NameAndSound = Named + Call;


          


            Mammal cat = new Mammal("Cat", "Meow", 5, 20, 15,"It can't fly");
            Mammal dog = new Mammal("Dog", "Bow Wow", 20, 40, 20, "It can't fly");
            Mammal linx = new Mammal("Linx", "Grrrr", 20, 40, 20, "It can't fly");

            Bird owl = new Bird("Owl", "Hoot", 1, 7, 30, "This bird can fly");


            Animals.Add(dog);
            Animals.Add(cat);
            Animals.Add(owl);
            Animals.Add(linx);

            Birds.Add(owl);
            Mammals.Add(dog);
            Mammals.Add(cat);
            Mammals.Add(linx);


            Animal.PrintList(Animals);

            Animal.SearchList(Animals, 2);
            Animal.SearchList(Animals, "Cat");

            AnimalCompare.weightCompare(cat, dog);
            AnimalCompare.weightCompare(linx, dog);

            Person spencer;
            spencer.Name = "Spencer";
            spencer.Nationality = "American";
            spencer.Height = 1.83;
            spencer.Weight = 86;
            spencer.Sign = Sign.Capricorn;

            Person ana;
            ana.Name = "Ana";
            ana.Nationality = "Colombian";
            ana.Height = 1.72;
            ana.Weight = 60;
            ana.Sign = null;

            People.Add(spencer);
            People.Add(ana);

            UserSearch.Search(Animals);

            Animal.ObjSerial("animal.txt", Animals);

            List<Animal> newAnimals = new List<Animal>();

            newAnimals = Animal.ReadObjSerial("animal.txt");

            Animal.PrintList(newAnimals);

            spencer.PrintToConsole();
            ana.PrintToConsole();

            int count = counter(Animals, People);
            string countStr = string.Format("There are {0} Animals and People in the lists", count);
            Console.WriteLine(countStr);

            People.Add(ana);
            count = counter(Animals, People);
            countStr = string.Format("There are {0} Animals and People in the lists", count);
            Console.WriteLine(countStr);



            for(var i =0; i<Mammals.Count();i++)
            {
                Named(Mammals,i);
                Call(Mammals, i);
                
            }

            for(var i=0; i<Birds.Count();i++)
            {
                NameAndSound(Birds, i);
            }

            for (var i = 0; i < Mammals.Count(); i++)
            {
                NameAndSound(Mammals, i);

            }
        }
        
    }
}
