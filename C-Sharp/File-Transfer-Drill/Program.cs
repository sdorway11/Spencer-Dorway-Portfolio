using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace FileTransferDrill
{
    class FileTransfer
    {
        static void Main(string[] args)
        {
            FileTransfer FT = new FileTransfer();

            string dirFromPath = "C:/Users/sdorw_000/Desktop/Folder 7";
            string dirToPath = "C:/Users/sdorw_000/Desktop/Folder B";


            FT.FileTrans(dirFromPath, dirToPath);

        }

        public string[] FindFiles(string path)
        {
            
            if (Directory.Exists(path))
            {
                string[] files = Directory.GetFiles(path);
                for (var i = 0; i < files.Length; i++)
                {
                    files[i] = Path.GetFileName(files[i]);
                }
                return files;
            }
            else
            {
                Console.WriteLine("The Directory Doesn't exist");
                string[] files = { "error" };
                return files;
            }

            
        }

        public List<DateTime> CheckFiles(string path)
        {
            List<DateTime> modifyDates = new List<DateTime>();
            DateTime modDate = new DateTime();
            string[] files = Directory.GetFiles(path);

            foreach(var file in files)
            {
                modDate = File.GetLastWriteTime(file);
                modifyDates.Add(modDate);
            }
            return modifyDates;
        }

        public void FileTrans(string dirFrom, string dirTo)
        {
            FileTransfer p = new FileTransfer();

            DateTime today = DateTime.Now;
            DateTime yesterday = today.AddDays(-1);

            if (Directory.Exists(dirFrom) && Directory.Exists(dirTo))
            {
                Console.WriteLine("Transfered files: ");
                string[] files = FindFiles(dirFrom);
                List<DateTime> modDates = CheckFiles(dirFrom);
                

                for (var i = 0; i < files.Length; i++)
                {
                    DateTime modDate = modDates[i];
                    int result = DateTime.Compare(yesterday, modDate);
                    if (result <= 0)
                    {
                        string pathFrom = dirFrom + "/" + files[i];
                        string pathTo = dirTo + "/" + files[i];
                        File.Move(pathFrom, pathTo);
                        DirectoryInfo dir = new DirectoryInfo(dirTo);
                        string dirName = dir.Name;
                        Console.WriteLine(String.Format("{0} has been Transfered to {1}", files[i], dirName));
                    }
                    else
                    {

                    }
                }
            }
            else
            {
                Console.WriteLine("One of your file paths is invalid");
            }
        }
    }
}
