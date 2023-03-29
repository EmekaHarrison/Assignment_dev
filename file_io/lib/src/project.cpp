#include "project.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
using namespace std;

File_IO::File_IO() {}

File_IO::~File_IO() {}

void File_IO::open()
{
    fstream myFile;
    myFile.open("Harrison.txt", ios::out);
    if (myFile.is_open())
    {
        cout << "File has been opened" << std::endl;
    }
    else if (myFile.fail())
    {
        std::cout << "File doesn't exist.\n";
    }
}

void File_IO::close()
{
    fstream myFile;
    myFile.close();
    std::cout << "File is closed" << std::endl;
}

int File_IO::Read_Line()
{
    std::cout << "Testing the initial function" << std::endl;
    ifstream file;

    string filename;
    int line_number;
    std::cout << "Enter the file name:";
    std::cin >> filename;

    std::cout << "Enter the line number: ";
    std::cin >> line_number;

    if (line_number <= 0)
    {
        std::cout << "Line number must be > 0." << std::endl;

        return 1;
    }
    file.open(filename);

    if (file.fail())
    {
        std::cout << "The file didn't open." << std::endl;

        return 1;
    }
    int current_line = 0;
    string line;
    while (!file.eof())
    {
        current_line++;
        getline(file, line);
        if (current_line == line_number)
            break;
    }
    if (current_line < line_number)
    {
        std::cout << "no line detected!" << std::endl;
        std::cout << " the file has " << current_line;
        std::cout << "total number of line ." << std::endl;
    }
    else
    {
        std::cout << "line: " << line << std::endl;
        file.close();
    }
    return 0;
}

int File_IO::Write_Line()
{
    ofstream myFile;
    if (myFile.is_open())
    {
        cout << "file opened";
        myFile << " Hi everyone. \n";
    }
    else if (myFile.fail())
    {
        std::cout << "opening of file!!!";
    }
    return 0;
}


vector<string> File_IO::read_container(string filename)
{
    ifstream file(filename);
    vector<string> contents;
    const int buffer_size = 256;
    if (file.is_open())
    {
        while (file.good())
        {
            const int buffer_size = 256;
            char buffer[buffer_size];

            file.getline(buffer, buffer_size - 1);
            contents.emplace_back(buffer);
        }
    }

    file.close();
    return contents;
}

void File_IO::write_container(string filename, vector<string> content)
{
    ofstream myfile;
    myfile.open(filename);
    for (string line : content)
        myfile << line << endl;
    myfile.close();
}