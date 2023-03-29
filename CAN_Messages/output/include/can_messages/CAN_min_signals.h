#ifndef HEADER_CAN_MIN_SIGNALS_H
#define HEADER_CAN_MIN_SIGNALS_H
#include <string>
class CAN_min_signals
{
public:
	CAN_min_signals();
	/*
	get the ambient temperature
	*/
	std::string get_temperature();
	/*
	set the ambient temperature
	*/
	std::string set_temperature(float newValue);
	/*
	get the ambient humidity percentage
	*/
	std::string get_humidity();
	/*
	set the ambient humidity percentage
	*/
	std::string set_humidity(uint8_t newValue);

private:
	uint8_t m_startMsgId;
	uint8_t m_temperatureGetMsGid;
	uint8_t m_temperatureSetMsGid;
	uint8_t m_humidityGetMsGid;
	uint8_t m_humiditySetMsGid;
};
#endif // HEADER_CAN_MIN_SIGNALS_H