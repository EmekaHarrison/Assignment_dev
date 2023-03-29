#ifndef PROJECT_H
#define PROJECT_H
#include <iostream>
#include <vector>

class File_IO
{
public:
    File_IO();
    ~File_IO();
    void open();
    void close();
    int Read_Line();
    int Write_Line();
    std::vector<std::string> read_container(std::string filename);
    void write_container(std::string filename, std::vector<std::string> content);
};

#endif /* PROJECT_H */