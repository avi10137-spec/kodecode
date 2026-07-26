namespace SensorApi.Models
{
    public class Sensor
    {
        public int Id { get; set; }
        public string NameSite { get; set; } = string.Empty;
        public string NameZone { get; set; } = string.Empty;

        public string Status { get; set; } = string.Empty;
        public DateTime RecordContact { get; set; }

    }
}
