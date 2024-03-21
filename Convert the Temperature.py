class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fehren = celsius * 1.80 + 32.00
        ans = [kelvin,fehren]
        return ans
