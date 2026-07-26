using Microsoft.AspNetCore.Mvc;
using SensorApi.Models;

namespace SensorApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SensorReading : ControllerBase
    {
        private static readonly List<Sensor> _sensors = new()
        {


            new Sensor
            {
                Id = 1,
                NameSite = "North Plant",
                NameZone = "Production Area 1",
                Status = "Active",
                RecordContact = new DateTime(2026, 7, 26, 10, 15, 0)
            },
            new Sensor
            {
                Id = 2,
                NameSite = "North Plant",
                NameZone = "Raw Materials Warehouse",
                Status = "Active",
                RecordContact = new DateTime(2026, 7, 26, 11, 0, 0)
            },
            new Sensor
            {
                Id = 3,
                NameSite = "North Plant",
                NameZone = "Server Room",
                Status = "Warning",
                RecordContact = new DateTime(2026, 7, 26, 14, 30, 0)
            },
            new Sensor
            {
                Id = 4,
                NameSite = "Central Logistics Hub",
                NameZone = "PackagingZone",
                Status = "Active",
                RecordContact = new DateTime(2026, 7, 26, 9, 45, 0)
            },
            new Sensor
            {
                Id = 5,
                NameSite = "Central Logistics Hub",
                NameZone = "Unloading Dock A",
                Status = "Inactive",
                RecordContact = new DateTime(2026, 7, 25, 18, 20, 0)
            },
            new Sensor
            {
                Id = 6,
                NameSite = "South Branch",
                NameZone = "MainFloor",
                Status = "Active",
                RecordContact = new DateTime(2026, 7, 26, 12, 10, 0)
            },
            new Sensor
            {
                Id = 7,
                NameSite = "South Branch",
                NameZone = "Administrative Offices",
                Status = "Maintenance",
                RecordContact = new DateTime(2026, 7, 24, 8, 0, 0)
            },
            new Sensor
            {
                Id = 8,
                NameSite = "R&D Labs",
                NameZone = "Cleanroom 1",
                Status = "Active",
                RecordContact = new DateTime(2026, 7, 26, 15, 0, 0)
            }

        
        };
        [HttpGet]

        public ActionResult <IEnumerable<Sensor>> GetAllSensors()
        {
            return Ok(_sensors);
        }
        [HttpGet("{id}")]
        public ActionResult<Sensor> GetSensorById (int id)
        {
            var sensor = _sensors.FirstOrDefault(s => s.Id == id);
            if (sensor == null)
            {
                return NotFound();
            }
            return Ok(sensor);
        }
        [HttpGet("zone/{zone}")]
        public ActionResult<IEnumerable<Sensor>> GetByZone(string zone)
        {
            var byzones = _sensors.Where(s => s.NameZone.Equals(zone, StringComparison.OrdinalIgnoreCase)).ToList();
            return Ok(byzones);
        }
        [HttpGet("search")]
        public ActionResult<IEnumerable<Sensor>> GetBySearch(
            [FromQuery] int ? minId)
        {
            var Query = _sensors.AsEnumerable();
            if (minId.HasValue)
            {
                Query = Query.Where(s => s.Id >= minId.Value).ToList();
                return Ok(Query);
                
            }
            return NotFound();
        }


    }

}
