from fastapi import FastAPI
from typing import List
import minimalmodbus

app = FastAPI()

# Configure the serial port
client = minimalmodbus.Instrument('COM1', 1) # port name, slave address
client.serial.baudrate = 9600 # Baud
client.serial.bytesize = 8
client.serial.parity = minimalmodbus.serial.PARITY_NONE
client.serial.stopbits = 1
client.serial.timeout = 0.1 # seconds

@app.get("/read_registers/{start_address}/{count}")
def read_registers(start_address: int, count: int) -> List[int]:
    """Read multiple registers from a Modbus slave device"""
    return client.read_registers(start_address, count)

@app.post("/write_register/{address}/{value}")
def write_register(address: int, value: int) -> int:
    """Write a single register to a Modbus slave device"""
    return client.write_register(address, value)

@app.get("/read_bits/{start_address}/{count}")
def read_bits(start_address: int, count: int) -> List[bool]:
    """Read multiple bits from a Modbus slave device"""
    return client.read_bits(start_address, count)

@app.post("/write_bit/{address}/{value}")
def write_bit(address: int, value: bool) -> int:
    """Write a single bit to a Modbus slave device"""
    return client.write_bit(address, value)
