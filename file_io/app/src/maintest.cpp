#include "project.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <iterator>

using namespace std;
int main(int argc, char *argv[])
{
    File_IO component;
    component.read_container("test.txt");
    component.close();
}