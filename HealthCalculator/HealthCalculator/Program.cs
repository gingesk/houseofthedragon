using System;

namespace HealthCalculator
{
    class Program
    {
        public bool underweight, normal, overweight, obese;
        public float weight;        
        public int heightInCentimeters;

        static void Main(string[] args)
        {
            // TODO: Create menu system

            // need to collect weight & height - imperial
            // need to collect weight & height - metric

            int unitSystem = ImperialOrMetric();

            if (unitSystem == 1) // imperial
            {
                Console.WriteLine("Please enter your height in feet and inches. You will be prompted for feet initally, and then Inches.\n" +
                    "For example, if you are 5 feet 7 inches, you will need to first enter " + 5 + " and then you will enter " + 7 + " after, when prompted.\n");
                int feet = GetIntInput("Please enter the feet."); // 0.3048m
                int inches = GetIntInput("Please now enter the inches."); //0.0254m


                // collect weight
                // pounds, stones and pounds
                int poundsOrStones = GetIntInput("Please indicate if you will be entering your weight in pounds, or stones & pounds.\n Enter 1 for Pounds, or 2 for Stones & pounds\n");
                if (poundsOrStones == 1) // pounds 
                {
                    float pounds = GetFloatInput("Please enter your weight in pounds. For example, you may enter '154.32'\n");
                }

                if (poundsOrStones == 2) // stones and pounds
                {

                }
            }


            /*
             * The health calculator will produce the Body Mass Index (BMI), Basal Metabolic Rate (BMR), 
             * Max Heart Rate (MHR) and Target Heart Rate (THR) of the user based on the information provided by the user to the health calculator.
             * 
             * The BMI can then be used to identify which category the user falls within. If the BMI is below 18.5 they are “underweight”. 
             * If the BMI is between 18.5 and 24.9 (inclusive) they are “normal”. If the BMI is between 25 and 29.9 (inclusive) they are “overweight”. 
             * If the BMI is 30 or over they are “obese”. 
             * A disclaimer should be shown to the user alongside their BMI and category which states that “BMI’s are only an indicator,
             * and do not replace medical advice from a doctor. BMI’s can be inaccurate for some people such as bodybuilders or professional athletes, the elderly, 
             * children and teenagers, lactating or pregnant women and for certain ethnicities. Please seek professional medical advice if you require it” 
             * To calculate MHR for users below 40 years of age:
             * 220 – age
             * To calculate MHR for users 40 and above years of age:
             * 208 – (0.75 * age) 
             * The target heart rate is any number in between the lower heart rate and upper heart rate.
             * To calculate Lower heart rate:
             * MHR * 0.5
             * To calculate Upper heart rate:
             * MHR * 0.85
             * To calculate BMR for men using the Mifflin - St Jeor Formula formulae:
             * (10 * weight in Kilograms + 6.25 * height in centimetres – 5 * age) + 5
             * To calculate BMR for women using the Mifflin - St Jeor Formula formulae:
             * (10 * weight in Kilograms + 6.25 * height in centimetres – 5 * age) – 161
             * No imperial unit formulae are provided with the BMR calculation, but the health calculator should be developed in such a way so that the user 
             * can enter imperial or metric units and still get be shown their BMR.
             * A help menu should be provided within the health calculator that shows the users the formulae used to calculate the different features within the calculator and the program should catch mistakes the users make when entering their details to make the use of the program as user friendly as possible.
             */
        }

        public static int ImperialOrMetric()
        {
            while (true)
            {
                int input = GetIntInput("Please select whether you wish to use this program with an Imperial or Metric unit system.\nEnter 1 for Imperial, or 2 for Metric\n");
            
                if (input != 1 && input != 2)
                {
                    Console.WriteLine("Incorrect input.");
                }
                if (input == 1) // imperial
                {
                    return input;
                }
                if (input == 2) // metric
                {
                    return input;
                }
            }
        }

        public float MetricBMI()
        {
            /*To calculate BMI using metric units:
             *Weight in Kilograms / Height in Meters2*/

            return 0.0f;
        }

        public float ImperialBMI()
        {
            /*
             * To Calculate BMI using imperial units:
             * Weight in Pounds * 703 / height in inches2 */

            return 0.0f;
        }
        static int GetIntInput(string message)
        {
            // initialisation of local variables 
            int parsedValue;
            string rawInput;

            while (true)
            {
                try
                {
                    Console.WriteLine(message); // print out to the user what we're asking for
                    rawInput = Console.ReadLine(); // store whatever we receive in a string 
                    int.TryParse(rawInput, out parsedValue); // attempt to convert that to an integer             
                    break;
                }
                catch
                {
                    Console.WriteLine("Input incorrect. Please enter a number");
                }
            }

            return parsedValue;
        }
        public static float GetFloatInput(string message)
        {
            // initialisation of local variables 
            float parsedValue;
            string rawInput;

            while (true)
            {
                try
                {
                    Console.WriteLine(message); // print out to the user what we're asking for
                    rawInput = Console.ReadLine(); // store whatever we receive in a string 
                    float.TryParse(rawInput, out parsedValue); // attempt to convert that to a number

                    if (parsedValue != 0)
                    {
                        break;
                    }
                    if (parsedValue == 0)
                    {
                        Console.WriteLine("Incorrect input! Please enter a number");
                    }
                }
                catch (Exception)
                {
                    Console.WriteLine("Input incorrect. Please enter a number");
                }
            }
            return parsedValue;
        }


    }
}
