using Microsoft.AspNetCore.Mvc;
using AirportFlightLogApi.Models;

namespace AirportFlightLogApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AirportController : ControllerBase
    {
        private static readonly List<FlightLog> _flightLog = new()
     {
         new FlightLog
         {
             Id = 1,
            FlightNumber = "AA101",
            Airline = "American Airlines",
            Destination = "New York JFK",
            PassengerCount = 180,
            ScheduledDeparture = DateTime.UtcNow.AddHours(2),
            Status = "Scheduled"
            },
            new FlightLog
            {
            Id = 2,
            FlightNumber = "BA202",
            Airline = "British Airways",
            Destination = "London Heathrow",
            PassengerCount = 250,
            ScheduledDeparture = DateTime.UtcNow.AddHours(4),
            ActualDeparture = DateTime.UtcNow.AddHours(4).AddMinutes(15),
            Status = "Departed",
            Remarks = "Delayed due to weather"
            },
            new FlightLog
            {
            Id = 3,
            FlightNumber = "LH303",
            Airline = "Lufthansa",
            Destination = "Frankfurt",
            PassengerCount = 200,
            ScheduledDeparture = DateTime.UtcNow.AddHours(6),
            Status = "Scheduled"
            }  
     };
        private static int _nextId = 4;
        [HttpGet]
        public ActionResult<IEnumerable<FlightLog>> GetAllFlight()
        {
            return Ok(_flightLog);
        }
        [HttpGet("{id}")]
        public ActionResult <FlightLog> GetFlightById(int id)
        {
            var result = _flightLog.FirstOrDefault(l => l.Id == id);
            if (result == null)
            {
                return NotFound();
            }
            return Ok(result);
        }
        [HttpPost]
        public ActionResult <FlightLog> CreateFlightLog(FlightLog flightlog)
        {
            flightlog.Id = _nextId++;
            _flightLog.Add(flightlog);
            return CreatedAtAction(nameof(GetFlightById), new { id = flightlog.Id }, flightlog);

        }
        [HttpPut("{id}")]
        public IActionResult UpdateFLightLog(int id,FlightLog updatedLog)
        {
            var existingLog = _flightLog.FirstOrDefault(l => l.Id == id);
            if(existingLog == null)
            {
                return NotFound();
            }
            existingLog.FlightNumber = updatedLog.FlightNumber;
            existingLog.Airline = updatedLog.Airline;
            existingLog.Destination = updatedLog.Destination;
            existingLog.PassengerCount = updatedLog.PassengerCount;
            existingLog.ScheduledDeparture = updatedLog.ScheduledDeparture;
            existingLog.ActualDeparture = updatedLog.ActualDeparture;
            existingLog.Remarks = updatedLog.Remarks;
            existingLog.Status = updatedLog.Status;
            return NoContent();

        }
        [HttpGet("search")]
        public ActionResult<IEnumerable<FlightLog>> GetBySearch([FromQuery] string airline)
        {
            if (string.IsNullOrEmpty(airline))
                {
                return BadRequest("airline parameter cannot be empty");
               }
            var logs = _flightLog.Where(l => l.Airline.Contains(airline, StringComparison.OrdinalIgnoreCase)).ToList();
            return Ok(logs);
        }
        [HttpDelete("{id}")]
        public IActionResult DeleteFlightLog(int id)
        {
            var log = _flightLog.FirstOrDefault(l => l.Id == id);
            {
             if(log == null)
                {
                    return NotFound();
                }
                _flightLog.Remove(log);
                return NoContent();
            }
        }
    }
}
