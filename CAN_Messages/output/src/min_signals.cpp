#include "../include/can_messages/CAN_min_signals.h"
#include <sstream>
CAN_min_signals::CAN_min_signals()
{
    m_startMsgId = 100;
    m_temperatureGetMsGid = m_startMsgId + 2;
    m_temperatureSetMsGid = m_startMsgId + 3;
    m_humidityGetMsGid = m_startMsgId + 4;
    m_temperatureSetMsGid = m_startMsgId + 5;
}
std::string CAN_min_signals::get_temperature()
{
    std::stringstream sstream;
    sstream << "{\"ID\": " << m_temperatureGetMsGid
            << ", \"length\":0 "
            << ", \"value\": \"\" }";
    return sstream.str();
}
std::string CAN_min_signals::get_humidity()
{
    std::stringstream sstream;
    sstream << "{\"ID\": " << m_humidityGetMsGid
            << ", \"length\":0 "
            << ", \"value\": \"\" }";
    return sstream.str();
}
std::string CAN_min_signals::set_temperature(float newValue)
{
    std::stringstream sstream;
    sstream << "{\"ID\": " << m_temperatureSetMsGid
            << ", \"length\":10"
            << ", \"value\":\""
            << newValue
            << "\" }";
    return sstream.str();
}
std::string CAN_min_signals::set_humidity(uint8_t newValue)
{
    std::stringstream sstream;
    sstream << "{\"ID\": " << m_humiditySetMsGid
            << ", \"length\":8"
            << ", \"value\":\""
            << newValue
            << "\" }";
    return sstream.str();
}
