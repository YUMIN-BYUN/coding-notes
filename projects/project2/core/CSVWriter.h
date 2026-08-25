#ifndef CSV_WRITER_H
#define CSV_WRITER_H

#include <fstream>
#include <iostream>

class CSVWriter
{
private:
    std::ofstream file;

public:
    CSVWriter(const std::string& filename);
    ~CSVWriter();

    void writeHeader(const std::string& header);
    void writeRow(const std::string& row);
};

#endif